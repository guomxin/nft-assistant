# coding: utf-8
# ContractName: ConFashion

from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "data/_details_conflux_aprilkaozai_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.ConFashion_Contract_Address, 
        contract.ConFashion_ABI, 
        dump_file_name,
        80001,
        82444)