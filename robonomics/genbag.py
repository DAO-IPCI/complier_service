# -*- coding: utf-8 -*-

import rosbag
from std_msgs.msg import String

emission_factor = 0.430 # gramm CO2 emitted by one Watt * hour of energy consumption
co2_on_vcu = 1_000 # kilogramm CO2 consumption represented by one VCU


bag = rosbag.Bag('./mybag.bag', 'w')

bag.write('/geo', String("Russia"))
bag.write('/power_kwh', String(str(co2_on_vcu/emission_factor)))
bag.close()

