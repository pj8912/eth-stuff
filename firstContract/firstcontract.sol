//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FirstContract{
	
	address private owner;
	uint public blockNumber;
	
	constructor(){
	
		owner = msg.sender; //contract creator address
		blockNumber = block.number; //latest block in the network
	
	}


	function getOwnerBalance() public view returns(uint256){
		
		return owner.balance;
	}
	
	function getOwnerAddress() public view returns(address){
		return owner; 
	}
	
	function latestMinedBlock() public view returns(uint256){
		return blockNumber;
	}
}
