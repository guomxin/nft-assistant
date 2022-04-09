# coding: utf-8

import sys

from tpcommon import (trans, contract, idrange)

if __name__ == "__main__":
    if len(sys.argv) < 9:
        print("{} <nft_name> <trans_file_name> <start_date> <end_date> <min_tid> <max_tid> <trans_tag> <result_tag>".format(sys.argv[0]))
        sys.exit(1)
    nft_name = sys.argv[1]
    trans_file_name = sys.argv[2]
    start_date_str = sys.argv[3]
    end_date_str = sys.argv[4]
    min_tid = int(sys.argv[5])
    max_tid = int(sys.argv[6])
    trans_tag = sys.argv[7]
    result_tag= sys.argv[8]

    result_file_name = "data/_transaction_conflux_{}_{}_result_{}.csv".format(
        nft_name, trans_tag, result_tag
    )
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    trans.analyze_transaction_logs(
        trans_file_name, 
        contract_address, 
        contract_ABI,
        start_date_str,
        end_date_str,
        result_file_name,
        min_tid, max_tid)
    