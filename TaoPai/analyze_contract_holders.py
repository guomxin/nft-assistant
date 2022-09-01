# coding: utf-8
import sys
from datetime import datetime
from tpcommon import contract

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("{} <nft_name> <tokenid2name_file> <snapshot_time>(e.g. 2022/9/1 12:00)".format(sys.argv[0]))
        sys.exit(1)

    nft_name = sys.argv[1]
    tokenid2name_file_name = sys.argv[2]
    snapshot_time = datetime.strptime(sys.argv[3], "%Y/%m/%d %H:%M")
    print("snapshot time: {}.".format(snapshot_time))
    tokenid2name = {}
    noname_token_cnt = 0
    for line in open(tokenid2name_file_name):
        items = line.strip().split(",")
        token_id = int(items[0])
        token_name = items[1]
        if token_name == "None":
            print("Token:{} without token name.".format(token_id))
            noname_token_cnt += 1
        tokenid2name[token_id] = token_name
    print("{} tokens without name.".format(noname_token_cnt))

    dump_file_name = "data/_contractholders_info_conflux_{}_result_{}.csv".format(
        nft_name, datetime.strftime(datetime.now(), "%Y%m%d")
    )
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    contract.analyze_contract_holders(contract_address, contract_ABI, tokenid2name, snapshot_time, dump_file_name)