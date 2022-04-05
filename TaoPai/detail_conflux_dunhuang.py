# coding: utf-8
# ContractName: SDQH

from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "_details_conflux_dunhuang_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.SDQH_Contract_Address, 
        contract.SDQH_ABI, 
        dump_file_name,
        10001, 40000)