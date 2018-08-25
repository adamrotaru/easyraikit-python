from time import sleep, time
from easyraikit_ext import *

print("--- RaiBlocks RPC Library for Python ---")

raiblocks_account_balance('xrb_1115zhctqdbznohjwajyss9ipq9wszpt3sxxjcdb5uyh19d9a48ob3ztmxwi')

unlocked = raiblocks_unlock()

balances = raiblocks_balance_wallet()
print("balances", balances)
