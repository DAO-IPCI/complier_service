const VCU = artifacts.require("VCU");

module.exports = async (deployer, network, accounts) => {
    await deployer.deploy(VCU);

    const vcu = await VCU.deployed();
    await vcu.mint(accounts[0], 1000);
};
