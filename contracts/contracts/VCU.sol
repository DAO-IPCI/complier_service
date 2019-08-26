pragma solidity ^0.5.0;

import '../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Detailed.sol';
import '../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Mintable.sol';
import '../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Burnable.sol';

contract VCU is ERC20Detailed, ERC20Mintable, ERC20Burnable {
    constructor() ERC20Detailed("Verified Carbon Units", "VCU", 0) public {

    }
}
