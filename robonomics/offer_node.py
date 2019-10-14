#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standart, System and Third Party
from threading import Thread
import sys

# ROS
import rospy

# Robonomics communication
from robonomics_msgs.msg import Offer, Demand
from ethereum_common.msg import Address, UInt256
from ethereum_common.srv import Accounts, BlockNumber
from ipfs_common.msg import Multihash



class OfferNode:

    DAI_PRICE = 1   # $1
    LIGHTHOUSE = '0x202a09A451DE674d2d65Bf1C90968a8d8F72cf7b'

    def __init__(self, model, token):

        rospy.init_node('trader')
        rospy.loginfo('Launching trader node...')

        self.MODEL = model
        self.TOKEN = token

        rospy.wait_for_service('/eth/current_block')
        rospy.wait_for_service('/eth/accounts')
        self.accounts = rospy.ServiceProxy('/eth/accounts', Accounts)()
        rospy.loginfo(str(self.accounts)) # AIRA ethereum addresses

        rospy.Subscriber('/liability/infochan/incoming/offer', Offer, self.on_incoming_offer)

        self.signing_demand = rospy.Publisher('/liability/infochan/eth/signing/demand', Demand, queue_size=128)

        rospy.loginfo('Offer node is ready!')

    def on_incoming_offer(self, offer: Offer):
        rospy.loginfo('Incoming offer...\n{}'.format(offer))
        if offer.model.multihash == self.MODEL and offer.token.address == self.TOKEN:
            rospy.loginfo('For my model and token!')
            self.make_demand(offer.objective, offer.cost)
        else:
            rospy.loginfo('It does not fit my model or token, skip it.')

    def get_deadline(self) -> UInt256:
        lifetime = int(200)
        deadline = rospy.ServiceProxy('/eth/current_block', BlockNumber)().number + lifetime
        return UInt256(str(deadline))

    def make_demand(self, objective: Multihash, cost: UInt256):
        rospy.loginfo('Making demand...')

        demand = Demand()
        demand.model = Multihash()
        demand.model.multihash = self.MODEL
        demand.objective = objective
        demand.token = Address()
        demand.token.address = self.TOKEN
        demand.cost = cost
        demand.lighthouse = Address()
        demand.lighthouse.address = self.LIGHTHOUSE
        demand.validator = Address()
        demand.validator.address = '0x0000000000000000000000000000000000000000'
        demand.validatorFee = UInt256()
        demand.validatorFee.uint256 = '0'
        demand.deadline = self.get_deadline()
        demand.nonce = UInt256('0')

        self.signing_demand.publish(demand)
        rospy.loginfo(demand)

    def spin(self):
        rospy.spin()

if __name__ == '__main__':
    '''
        ./script <model> <token>
    '''
    model = sys.argv[1]
    token = sys.argv[2]
    OfferNode(model, token).spin()

