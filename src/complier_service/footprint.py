def get_emission_factor(geo: str) -> float:
    emission_factor = 0.430 # g CO2 / W*h
    # one VCU == 1 tCO2; 1 W*h => 0.430 gCO2
    return emission_factor

def calc_footprint(consumption: float, emission_factor: float) -> float:
    return consumption * emission_factor

def offset_footprint(cumulative_consumption_wh, geo):
    """Offset carbon footprint for given amount of energy consumption in region
    """
    print('going to offset {} from {}'.format(cumulative_consumption_wh, geo))

    emission_factor = get_emission_factor(geo)
    footprint_g_co2 = calc_footprint(cumulative_consumption_wh, emission_factor)

    if not (footprint_g_co2 % 1_000_000): # tonn of CO2
        raise ValueError('Possible to offset only multiplies of ton CO2 (1000000 gram)')

    def burn_credits(volume):
        print('going to burn {}'.format(volume))
        #account = KeyfileHelper(rospy.get_param('~keyfile'),
        account = KeyfileHelper(keyfile,
                #keyfile_password_file=rospy.get_param('~keyfile_password_file')
                keyfile_password_file=keyfile_password_file
                ).get_local_account_from_keyfile()
        http_provider = HTTPProvider(web3_http_provider)
        web3 = Web3(http_provider)

        vcu_token = web3.eth.contract(VCU.address, abi=VCU.abi)
        # vcu_delimiter = (10 ** vcu_token.functions.decimals().call()) # for VCU should be 1

        balance = vcu_token.functions.balanceOf(account).call()
        print('VCU balance: {}'.format(balance))

        if volume > balance:
            raise ValueError('Volume exceed balance')

        complier = web3.eth.contract(COMPLIER.address, abi=COMPLIER.abi)
        print('will burn {}'.format(volume))
        # complier.functions.burn(VCU.address, volume).call()
        print('burned')

    burn_credits(footprint_g_co2 / 1_000_000) # 1VCS means tCO2
    print('offsetted {} g co2'.format(footprint_g_co2))

