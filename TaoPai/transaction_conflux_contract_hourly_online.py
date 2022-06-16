# coding: utf-8

import sys
import os

from tpcommon import (trans, contract, idrange)

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("{} <nft_name> <date> <hour> <token_id_ranges>(min1,max1;min2,max2;...) \
            <trans_tags>(tag1;tag2;...) <result_tag>".format(sys.argv[0]))
        sys.exit(1)
    nft_name = sys.argv[1]
    date_str = sys.argv[2]
    hour_str = sys.argv[3]
    ranges_str = sys.argv[4]
    tags_str = sys.argv[5]
    result_tag= sys.argv[6]

    tags = tags_str.split(";")
    ranges = [[int(item) for item in range_str.split(",")] for range_str in ranges_str.split(";")]

    result_file_name = "data/hourly/_transaction_conflux_{}_{}_result_{}.csv".format(
        nft_name, "+".join(tags), result_tag
    )
    
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    trans.multi_analyze_transaction_logs_hourly_online(
        contract_address, 
        contract_ABI,
        date_str,
        hour_str,
        ranges,tags,
        result_file_name)
    