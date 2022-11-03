from constants import * 


acc1 = "0x9dfcD196a899E755ff05644D1c045A1981F411C8"

acc2 = "0xa547CcD4f7bB7E84d6b6ca5C4C01Fe193f0eAccE"


b1 = web3.fromWei(web3.eth.get_balance(acc1),"ether")
b2 = web3.fromWei(web3.eth.get_balance(acc2), "ether")

print("acc1 balance: ", b1, "ETH")
print("acc2 balance: ", b2, "ETH")

