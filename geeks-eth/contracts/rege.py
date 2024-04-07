from web3 import Web3

# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:9545/'))

# Set up the contract
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = 'YOUR_CONTRACT_ABI'

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Set your default account
w3.eth.default_account = w3.eth.accounts[0]

# Function to save a string to the blockchain
def save_string_to_blockchain(input_string):
    tx_hash = contract.functions.setString(input_string).transact()
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

# Example usage
receipt = save_string_to_blockchain('Hello, Blockchain!')
print(receipt)
