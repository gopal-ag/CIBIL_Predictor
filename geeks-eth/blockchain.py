import json
from web3 import Web3, HTTPProvider

# The address for the blockchain node, replace if you're using a testnet or mainnet node
blockchain_address = 'http://127.0.0.1:9545/'

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

# Check the connection to the blockchain
if web3.is_connected():
    print("Connected to the blockchain")
else:
    print("Not connected to the blockchain")

# Setting the default account
web3.eth.default_account = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/InfoStorage.json'

# Deployed contract address (this should be the address of your deployed InfoStorage contract)
deployed_contract_address = '0x2e3f6095194846Bd8644eB29f95b38E5342b4BE3'

# Load the contract's ABI
with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # Load the contract's ABI and other info
    contract_abi = contract_json['abi']  # Get the ABI

# Create a contract object using the ABI
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Function to add information to the blockchain
def add_info(info_data):
    try:
        # Build the transaction to estimate gas
        transaction = contract.functions.addInfo(info_data).build_transaction({
            'from': web3.eth.default_account,
            'nonce': web3.eth.get_transaction_count(web3.eth.default_account),
            'gasPrice': web3.to_wei('50', 'gwei')  # Adjust gas price if needed
        })

        # Estimate gas for the transaction
        gas_estimate = web3.eth.estimate_gas(transaction)
        print(f"Estimated gas: {gas_estimate}")

        # Update the transaction with the gas estimate
        transaction.update({ 'gas': gas_estimate })

        # Sign the transaction
        #signed_tx = web3.eth.account.sign_transaction(transaction, private_key='cb7f5df99e31a752f7684de11b1ffbb1d8c4b5abeab4bead5246fff8274d308d')

        # Send the transaction
        tx_hash = web3.eth.send_transaction(transaction)

        # Wait for the transaction to be mined and get the transaction receipt
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(tx_receipt)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# receipt = add_info("hello")
# receipt = add_info("her3r34o")
#
# # Function to retrieve information from the blockchain
def get_info(info_id):
    info = contract.functions.getInfo(info_id).call()
    return info
#
# # Example usage: Add information
# info_to_add = "Example info"
# try:
#     receipt = add_info(info_to_add)
#     print(f"Transaction receipt: {receipt}")
# except Exception as e:
#     print(f"An error occurred while adding info: {e}")
#
# # Example usage: Get information
# info_id = 0  # Assuming you want to get the first entry
# add_info("hello aryan")
retrieved_info = get_info(89)
print(f"Retrieved info: {retrieved_info}")
