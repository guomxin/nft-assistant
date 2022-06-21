# coding: utf-8
import sys
from datetime import datetime

from tpcommon import contract

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <nft_name> <ranges>.".format(sys.argv[0]))
        sys.exit(1)

    nft_name = sys.argv[1]
    ranges_str = sys.argv[2]
    ranges = [[int(item) for item in range_str.split(",")] for range_str in ranges_str.split(";")]
    dump_file_name = "data/_tokenid2name_conflux_{}_result_{}.csv".format(
        nft_name, datetime.strftime(datetime.now(), '%Y%m%d')
    )
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    contract.dump_contract_tokenid2name(
        contract_address, 
        contract_ABI, 
        dump_file_name,
        ranges)