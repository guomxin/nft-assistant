# coding: utf-8
# ContractName: TaopaiNFT

from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "data/_details_conflux_taopainft_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_details(
        contract.TaopaiNFT_Contract_Address, 
        contract.TaopaiNFT_ABI, 
        dump_file_name)