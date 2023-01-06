# coding: utf-8
import sys
from tpcommon import contract

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <nft_name> <tokenid2name_file>".format(sys.argv[0]))
        sys.exit(1)

    nft_name = sys.argv[1]
    tokenid2name_file_name = sys.argv[2]
    dump_file_name = "{}.refined.csv".format(
        tokenid2name_file_name
    )
    contract_address, _ = contract.get_contract_address_ABI_from_name(nft_name)
    no_name_token_cnt_before = 0
    no_name_token_cnt_after = 0
    with open(dump_file_name, "w", encoding="utf-8-sig") as dump_file:
        for line in open(tokenid2name_file_name, encoding="utf-8-sig"):
            items = line.strip().split(",")
            token_id = int(items[0])
            token_name = items[1]
            if token_name == "None":
                no_name_token_cnt_before += 1
                print("Get token name for {} ...".format(token_id))
                token_name = contract.get_token_name(contract_address, token_id)
            if token_name == None:
                no_name_token_cnt_after += 1
            dump_file.write("{},{}\n".format(token_id, token_name))
    print("{} tokens without name, after refining {} tokens without name.".format(
        no_name_token_cnt_before, no_name_token_cnt_after
    ))