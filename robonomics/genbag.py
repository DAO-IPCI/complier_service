# -*- coding: utf-8 -*-

import rosbag
from ethereum_common.msg import UInt256


emission_factor = 0.430 # gramm CO2 emitted by one Watt * hour of energy consumption
co2_on_vcu = 1_000_000 # gramm CO2 consumption represented by one VCU


bag = rosbag.Bag('./mybag.bag', 'w')
topic = '/packet_size'
msg = UInt256(uint256=str(co2_on_vcu/emission_factor))


try:
    bag.write(topic, msg)
finally:
    bag.close()
