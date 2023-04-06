import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

INFURA_PROVIDER = os.getenv("MAINNET_INFURA")

# Connect to blockchain
web3 = Web3(Web3.HTTPProvider(INFURA_PROVIDER))
print(f"Connected: {web3.isConnected()}")

# Connect to contract
target_address = web3.toChecksumAddress("0x6dfc34609a05bC22319fA4Cce1d1E2929548c0D7")

print(
    f"Wallet ETH balance: {web3.fromWei(web3.eth.get_balance(target_address), 'ether')}"
)
is_contract = "Yes" if web3.eth.get_code(target_address) else "No"

print(f"{target_address} is a contract: {is_contract}")
