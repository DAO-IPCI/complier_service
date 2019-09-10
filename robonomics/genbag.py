# -*- coding: utf-8 -*-

from rosbag import Bag
from std_msgs.msg import String

emission_factor = 0.430 # gramm CO2 emitted by one Watt * hour of energy consumption
co2_on_vcu = 1_000 # kilogramm CO2 consumption represented by one VCU


bag = Bag('./mybag.bag', 'w')

bag.write('/geo', String("Russia"))
bag.write('/power_kwh', String(str(co2_on_vcu/emission_factor)))
bag.close()

bag_tmu_200 = Bag('./objective_tmu_200.bag', 'w')
bag_tmu_200.write('/co2_volume', String("200"))
bag_tmu_200.close()

bag_tmu_1500 = Bag('./objective_tmu_1500.bag', 'w')
bag_tmu_1500.write('/co2_volume', String("1500"))
bag_tmu_1500.close()

bag_vcu_1000 = Bag('./objective_vcu_1000.bag', 'w')
bag_vcu_1000.write('/co2_volume', String("1000"))
bag_vcu_1000.close()

bag_vcu_200 = Bag('./objective_vcu_200.bag', 'w')
bag_vcu_200.write('/co2_volume', String("200"))
bag_vcu_200.close()

