const TMUKhimprom = artifacts.require("TMUKhimprom");
const TMUSwisskrono = artifacts.require("TMUSwisskrono")

module.exports = async (deployer, network, accounts) => {
    await deployer.deploy(TMUKhimprom);
    await deployer.deploy(TMUSwisskrono);

    const tmukhimprom = await TMUKhimprom.deployed();
    await tmukhimprom.mint(accounts[0], 200000000);

    const tmuswisskrono = await TMUSwisskrono.deployed();
    await tmuswisskrono.mint(accounts[0], 1400000000);
};
