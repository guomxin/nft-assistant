# coding: utf-8

import sys

from tpcommon import contract
from tpcommon import idrange

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <nft_name> <detail_tag>.".format(sys.argv[0]))
        print("nft_name: liuangel, aprilkaozai, atsj, chaohu, dunhuang, lt, qiannian, taopainft, guizi, shangshi.")
        sys.exit(1)
    
    nft_name = sys.argv[1]
    min_tid, max_tid = idrange.get_range_by_nftname(nft_name)
    print("min_token_id:{}, max_token_id:{}.".format(min_tid, max_tid))
    detail_tag = sys.argv[2]
    dump_file_name = "data/_details_conflux_{}_result_{}.csv".format(
        nft_name, detail_tag
    )
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    contract.dump_contract_details(
        contract_address, 
        contract_ABI, 
        dump_file_name,
        min_tid, max_tid)