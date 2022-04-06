# coding: utf-8

from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":

    dump_file_name = "data/_tokenid2owner_conflux_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    )
    contract.dump_contract_tokenid2owner(
        contract.TaopaiNFT_Contract_Address, 
        contract.TaopaiNFT_ABI, 
        dump_file_name)