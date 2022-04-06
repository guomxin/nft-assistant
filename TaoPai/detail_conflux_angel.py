# coding: utf-8
# ContractName: XY
# 六天使

from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "_details_conflux_liuangel_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.XY_Contract_Address, 
        contract.XY_ABI, 
        dump_file_name,
        20001,
        23000)