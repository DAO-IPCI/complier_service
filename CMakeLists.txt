cmake_minimum_required(VERSION 2.8.3)
project(offsetting_agent)

find_package(catkin REQUIRED COMPONENTS
  rospy
  robonomics_liability
  ethereum_common
  ipfs_common
)

catkin_python_setup()

catkin_package()

catkin_install_python(
    PROGRAMS
        scripts/trader_node
        scripts/worker_node
    DESTINATION
        ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
    FILES
        launch/agent.launch
    DESTINATION
        ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

install(
    FILES
       db/countries.db
    DESTINATION
        ${CATKIN_PACKAGE_SHARE_DESTINATION}/db
)

