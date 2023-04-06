import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

INFURA_PROVIDER = os.getenv("MAINNET_INFURA")

# Connect to blockchain
web3 = Web3(Web3.HTTPProvider(INFURA_PROVIDER))
print(f"Connected: {web3.isConnected()}")

# Connect to Chainlink token contract
target_address = web3.toChecksumAddress("0x514910771AF9Ca656af840dff83E8264EcF986CA")

# separating these so I can remember the functions separately
contract_code = web3.eth.get_code(target_address)
contract_hex = web3.toHex(contract_code)
print(contract_hex)

### Course version
# print(web3.toHex(web3.eth.get_code(target_address)))

#############
##  Resources
#############
#   1. Convert function string to keckack256 hash (only first 4 bytes)
#       https://keccak-256.4tools.net/
#   2. Guess likely functions for 8-bit hash
#       https://www.4byte.directory/
