from web3.auto import w3
from web3 import Web3
from web3.constants import MAX_INT
import os
from abi import EIP20_ABI
from abi_conditional import EIP20_ABI_CON
import dotenv

dotenv.load_dotenv()

w3 = Web3(Web3.HTTPProvider("https://rpc-mumbai.maticvigil.com"))
private_key = os.getenv("PK")
address = "0xBC241BB040fAd5e3841Df947031494AaE7d81b6c"
usdc_contract = w3.eth.contract(
    address="0x2E8DCfE708D44ae2e406a1c02DFE2Fa13012f961", abi=EIP20_ABI)
ctf = w3.eth.contract(
    address="0x7D8610E9567d2a6C9FBf66a5A13E9Ba8bb120d43", abi=EIP20_ABI_CON)

nonce = w3.eth.get_transaction_count(
    '0xBC241BB040fAd5e3841Df947031494AaE7d81b6c')

MAX_INT = int(MAX_INT[2:], 16)
print(MAX_INT)
'''
usdc_contract_txn = usdc_contract.functions.mint(address, 1000000000000000,).buildTransaction(
    {'chainId': 80001, 'gas': 200000, 'maxFeePerGas': w3.toWei('2', 'gwei'), 'maxPriorityFeePerGas': w3.toWei('1', 'gwei'), 'nonce': nonce, "from": address})
# print(usdc_contract_txn)
'''

lop = "0x6D486b31b5c0f724828Aff07c88606b213B0D196"
executor = "0x6b0ab7A1E65ea6AE9072f6c45B4261ACDfB30827"
"""
usdc_contract_txn = usdc_contract.functions.approve(lop, MAX_INT).buildTransaction(
    {'chainId': 80001, 'gas': 200000, 'maxFeePerGas': w3.toWei('2', 'gwei'), 'maxPriorityFeePerGas': w3.toWei('1', 'gwei'), 'nonce': nonce, "from": address})
signed_txn = w3.eth.account.sign_transaction(usdc_contract_txn, private_key)
w3.eth.send_raw_transaction(signed_txn.rawTransaction)

usdc_contract_txn = usdc_contract.functions.approve(executor, MAX_INT).buildTransaction(
    {'chainId': 80001, 'gas': 200000, 'maxFeePerGas': w3.toWei('2', 'gwei'), 'maxPriorityFeePerGas': w3.toWei('1', 'gwei'), 'nonce': nonce + 1, "from": address})
signed_txn = w3.eth.account.sign_transaction(usdc_contract_txn, private_key)
w3.eth.send_raw_transaction(signed_txn.rawTransaction)
"""


ctf_txn = ctf.functions.setApprovalForAll(executor, True).buildTransaction(
    {'chainId': 80001, 'gas': 20000000, 'maxFeePerGas': w3.toWei('2', 'gwei'), 'maxPriorityFeePerGas': w3.toWei('1', 'gwei'), 'nonce': nonce})
signed_txn = w3.eth.account.sign_transaction(ctf_txn, private_key)
w3.eth.send_raw_transaction(signed_txn.rawTransaction)

ctf_txn = ctf.functions.setApprovalForAll(lop, True).buildTransaction(
    {'chainId': 80001, 'gas': 20000000, 'maxFeePerGas': w3.toWei('2', 'gwei'), 'maxPriorityFeePerGas': w3.toWei('1', 'gwei'), 'nonce': nonce})
signed_txn = w3.eth.account.sign_transaction(ctf_txn, private_key)
w3.eth.send_raw_transaction(signed_txn.rawTransaction)
