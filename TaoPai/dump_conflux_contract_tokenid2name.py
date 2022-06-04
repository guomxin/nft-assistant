# coding: utf-8
import sys
from datetime import datetime

from tpcommon import contract

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <nft_name>.".format(sys.argv[0]))
        sys.exit(1)

    nft_name = sys.argv[1]
    dump_file_name = "data/_tokenid2name_conflux_{}_result_{}.csv".format(
        nft_name, datetime.strftime(datetime.now(), '%Y%m%d')
    )
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    filterout_ranges = [(60001,70000), (10001,10999), (20001,20127), (30001,32022), (100001,109628), (200001,200360), \
        (300001,300012), (2001,2052)]
    contract.dump_contract_tokenid2name(
        contract_address, 
        contract_ABI, 
        dump_file_name,
        filterout_ranges)