# coding: utf-8
# 20220402离碳（儿童作品）
from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "_details_conflux_lt_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.LT_Contract_Address, 
        contract.LT_ABI, 
        dump_file_name,
        3000, 8680)