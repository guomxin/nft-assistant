# coding: utf-8

import sys
import os

from tpcommon import (trans, contract, idrange)

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("{} <nft_name> <start_date> <end_date> <token_id_ranges>(min1,max1;min2,max2;...) \
            <trans_tags>(tag1;tag2;...) <result_tag>".format(sys.argv[0]))
        sys.exit(1)
    nft_name = sys.argv[1]
    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]
    ranges_str = sys.argv[4]
    tags_str = sys.argv[5]
    result_tag= sys.argv[6]

    tags = tags_str.split(";")
    ranges = [[int(item) for item in range_str.split(",")] for range_str in ranges_str.split(";")]

    nodup_tags = []
    for tag in tags:
        if tag not in nodup_tags:
            nodup_tags.append(tag)
    result_file_name = "data/_transaction_conflux_{}_{}_result_{}({}-{}).csv".format(
        nft_name, "+".join(nodup_tags), result_tag,
        start_date_str.replace("/",""), end_date_str.replace("/", "")
    )

    # 如果价格文件存在则加载
    traceprice_dict = {}
    tradeprice_file_name = "data/_crawl_{}_trade_{}.csv".format(
        nft_name, result_tag
    )
    if os.path.exists(tradeprice_file_name):
        with open(tradeprice_file_name) as tradeprice_file:
            for line in tradeprice_file:
                items = line.strip().split(",")
                token_id = float(items[0])
                plist = [float(p) for p in items[1].split(";")]
                traceprice_dict[token_id] = plist
    
    contract_address, contract_ABI = contract.get_contract_address_ABI_from_name(nft_name)
    trans.multi_analyze_transaction_logs_online(
        traceprice_dict,
        contract_address, 
        contract_ABI,
        start_date_str,
        end_date_str,
        ranges,tags,
        result_file_name)
    