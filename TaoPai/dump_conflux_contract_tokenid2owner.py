# coding: utf-8
import sys
from datetime import datetime

from tpcommon import contract

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <nft_name>.".format(sys.argv[0]))
        sys.exit(1)

    nft_name = sys.argv[1]
    dump_file_name = "data/_tokenid2owner_conflux_{}_result_{}.csv".format(
        nft_name, datetime.strftime(datetime.now(), '%Y%m%d')
    )
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    contract.dump_contract_tokenid2owner(
        contract_address, 
        contract_ABI, 
        dump_file_name)