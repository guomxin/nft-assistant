# coding: utf-8
import sys
sys.path.append("../TaoPai")
from conflux import (
    Conflux,
    HTTPProvider
)

from tpcommon import contract

provider = HTTPProvider('https://main.confluxrpc.com')
c = Conflux(provider)

my_c = c.contract(contract.ConFashion_Contract_Address, contract.ConFashion_ABI)
tx = c.cfx.getTransactionByHash("0x379f9c9165599d43eafd41be01681415b5454ca2c0271d5f461742c0a6808d40")

print(tx)
decode_result = my_c.decode_function_input(tx.data)
#print(decode_result[1])
print(contract.get_base32addr_from_hexaddr(decode_result[1]["from"]))
print(contract.get_base32addr_from_hexaddr(decode_result[1]["to"]))
print(decode_result[1]["tokenId"])