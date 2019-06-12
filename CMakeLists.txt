cmake_minimum_required(VERSION 2.8.3)
project(complier_service)

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
        launch/trader.launch
        launch/worker.launch
        launch/sidechain_trader.launch
        launch/sidechain_worker.launch
        launch/testnet_trader.launch
        launch/testnet_worker.launch
        launch/testnet_erc20.launch
        launch/testnet_liability.launch
    DESTINATION
        ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
