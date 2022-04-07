# coding: utf-8
# ContractName: JYY

from datetime import datetime
import sys

from tpcommon import (trans, contract)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("{} <trans_file_name> <start_date> <end_date>".format(sys.argv[0]))
        sys.exit(1)
    trans_file_name = sys.argv[1]
    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]

    result_file_name = "data/_transaction_conflux_qiannian_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    trans.analyze_transaction_logs(
        sys.argv[1], 
        contract.JYY_Contract_Address, 
        contract.JYY_ABI,
        start_date_str,
        end_date_str,
        result_file_name,
        11001, 11500)
    