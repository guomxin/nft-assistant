# coding: utf-8
# ContractName: COCAFE
# 潮虎

from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "_details_conflux_chaohu_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.COCAFE_Contract_Address, 
        contract.COCAFE_ABI, 
        dump_file_name)