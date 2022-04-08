# coding: utf-8
# ContractName: SDQH
import sys

from tpcommon import (trans, contract)

if __name__ == "__main__":
    if len(sys.argv) < 8:
        print("{} <trans_file_name> <start_date> <end_date> <min_tid> <max_tid> <trans_tag> <result_tag>".format(sys.argv[0]))
        sys.exit(1)
    trans_file_name = sys.argv[1]
    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]
    min_tid = int(sys.argv[4])
    max_tid = int(sys.argv[5])
    trans_tag = sys.argv[6]
    result_tag= sys.argv[7]

    result_file_name = "data/_transaction_conflux_dunhuang_{}_result_{}.csv".format(
        trans_tag, result_tag
    )
    trans.analyze_transaction_logs(
        trans_file_name, 
        contract.SDQH_Contract_Address, 
        contract.SDQH_ABI,
        start_date_str,
        end_date_str,
        result_file_name,
        min_tid, max_tid)
    