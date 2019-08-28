const DAI = artifacts.require("DAI");

module.exports = async (deployer, network, accounts) => {
    await deployer.deploy(DAI);

    const dai = await DAI.deployed();
    await dai.mint(accounts[0], 100000000000);
};
