# coding: utf-8
import sys
from datetime import datetime

from tpcommon import contract

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <nft_name> <existing_tokenid2name_file>.".format(sys.argv[0]))
        sys.exit(1)

    nft_name = sys.argv[1]
    existing_tokenid2name = {}
    for line in open(sys.argv[2]):
        items = line.strip().split(",")
        token_id = int(items[0])
        token_name = items[1]
        existing_tokenid2name[token_id] = token_name
    dump_file_name = "data/_tokenid2name_conflux_{}_result_{}.csv".format(
        nft_name, datetime.strftime(datetime.now(), '%Y%m%d')
    )
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    contract.dump_contract_all_tokenid2name(
        contract_address, 
        contract_ABI, 
        existing_tokenid2name,
        dump_file_name)