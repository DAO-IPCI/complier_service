import rospy
import sqlite3
import urllib.request
import json
from web3 import Web3, HTTPProvider
from ethereum_common.eth_keyfile_helper import KeyfileHelper
from ethereum_common.srv import Accounts, BlockNumber
from complier_service.contracts import TOKEN_TO_BURN

TOKEN_PRICE = 7.5     # $7.5 for 1 VCU token

WEB3_HTTP_PROVIDER = rospy.get_param('/liability/listener/web3_http_provider')

KEYFILE = rospy.get_param('/liability/infochan/eth/signer/keyfile')
KEYFILE_PASSWORD_FILE = rospy.get_param('/liability/infochan/eth/signer/keyfile_password_file')

def get_token_price() -> float:
    # Temporary let's assume it's a constant
    # TODO grab the price from coincap.io for example
    return TOKEN_PRICE

def sign_and_send(fn, account="", web3=""):
    nonce = web3.eth.getTransactionCount(account.address)

    fn_tx = fn.buildTransaction({
        'from': account.address,
        'gasPrice': web3.toWei('0', 'gwei'), # Sidechain only
        'nonce': nonce
    })
    signed_tx = web3.eth.account.signTransaction(fn_tx, account.privateKey)
    tx = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx

def ton_to_tokens(ton: float, decimals: int) -> int:
    return round(ton * (10 ** decimals))

def offset_footprint(kilos: float, geo: str):
    """Offset carbon footprint for given amount of energy consumption in region
    """
    rospy.loginfo('going to offset {} kg from {}'.format(kilos, geo))

    def burn_credits(volume: float):
        rospy.loginfo('going to burn {} ton'.format(volume))
        account = KeyfileHelper(KEYFILE,
                keyfile_password_file=KEYFILE_PASSWORD_FILE
                ).get_local_account_from_keyfile()
        http_provider = HTTPProvider(WEB3_HTTP_PROVIDER)
        web3 = Web3(http_provider)

        rospy.loginfo("Token to burn address {}".format(TOKEN_TO_BURN.address))
        token_contract = web3.eth.contract(TOKEN_TO_BURN.address, abi=TOKEN_TO_BURN.abi)

        decimals = token_contract.functions.decimals().call()
        amount = ton_to_tokens(volume, decimals)

        rospy.loginfo("My account is {}".format(account.address))

        rospy.wait_for_service('/eth/accounts')
        accounts = rospy.ServiceProxy('/eth/accounts', Accounts)()

        balance = token_contract.functions.balanceOf(accounts.accounts[0].address).call()
        rospy.loginfo('Token to burn balance: {}'.format(balance))

        if amount > balance:
            raise ValueError('Volume exceed balance')

        rospy.loginfo('will be burned {} tokens'.format(amount))

        burn_call = token_contract.functions.burn(amount)
        tx = sign_and_send(burn_call, account=account, web3=web3)
        rospy.loginfo("Tx is {}".format(tx.hex()))

        rospy.loginfo('burned')

    volume = kilos / 1000

    burn_credits(volume) # 1VCS means tCO2
    rospy.loginfo('offsetted {} kg co2'.format(kilos))
    return volume

