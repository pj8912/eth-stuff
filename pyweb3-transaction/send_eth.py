from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
web3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

account_from = { 
        "private_key": "6d3d68bae5c11ccdc3f1e6d3e96c1a026dbf432ff80d6b252f1d9209af691e8e" , 
        "address": "0x9dfcD196a899E755ff05644D1c045A1981F411C8"
        }


address_to = "0xa547CcD4f7bB7E84d6b6ca5C4C01Fe193f0eAccE"

tx_create = web3.eth.account.sign_transaction(
        { 
            "nonce": web3.eth.get_transaction_count(account_from["address"]),
            "gasPrice": web3.eth.generate_gas_price(), 
            "gas": 21000,  
            "to": address_to, 
            "value": web3.toWei("1", "ether"), },
        account_from["private_key"],
        )




print(f' sending transaction from { account_from["address"] } to { address_to }')

tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print('transaction hash: ', tx_receipt.transactionHash.hex())

