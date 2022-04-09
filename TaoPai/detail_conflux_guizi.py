# coding: utf-8
# ContractName: UXON

import sys

from tpcommon import contract

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <detailfile_tag>.".format(sys.argv[0]))
        sys.exit(1)
    
    file_tag = sys.argv[1]
    dump_file_name = "data/_details_conflux_guizi_result_{}.csv".format(
        file_tag
    )
    contract.dump_contract_details(
        contract.UXON_Contract_Address, 
        contract.UXON_ABI, 
        dump_file_name)