# coding: utf-8
# ContractName: JYY

from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "data/_details_conflux_qiannian_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.JYY_Contract_Address, 
        contract.JYY_ABI, 
        dump_file_name,
        11001, 11500)