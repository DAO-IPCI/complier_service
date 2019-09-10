const TMU = artifacts.require("TMU");

module.exports = async (deployer, network, accounts) => {
    await deployer.deploy(TMU);

    const tmu = await TMU.deployed();
    await tmu.mint(accounts[0], 200000000);
};
