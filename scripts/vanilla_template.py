import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

INFURA_PROVIDER = os.getenv("MAINNET_INFURA")

# Connect to blockchain
web3 = Web3(Web3.HTTPProvider(INFURA_PROVIDER))
print(f"Connected: {web3.isConnected()}")

# Connect to contract
target_address = web3.toChecksumAddress("")
target_abi = ""
target_contract = web3.eth.contract(address=target_address, abi=target_abi)
