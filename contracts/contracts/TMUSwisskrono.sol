pragma solidity ^0.5.0;

import '../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Detailed.sol';
import '../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Mintable.sol';
import '../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Burnable.sol';

// Let's pretend this is the DAI token
contract TMUSwisskrono is ERC20Detailed, ERC20Mintable, ERC20Burnable {
    constructor() ERC20Detailed("TMUSwisskrono", "TMU", 3) public {

    }
}
