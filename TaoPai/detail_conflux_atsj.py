# coding: utf-8
# ContractName: ATSJ
# 凹凸世界
from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "data/_details_conflux_atsj_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.ATSJ_Contract_Address, 
        contract.ATSJ_ABI, 
        dump_file_name)