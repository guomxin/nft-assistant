# coding: utf-8

import sys
import os

from gycommon import commoninfo
from gycommon import utils

BLACK8_NICK_NAME = "s*****"
HONG_NICK_NAME = "翃*" # 翃翾

SELLER_NAME_INDEX = 1
BUYER_NAME_INDEX = 2
TRANS_PRICE_INDEX = 4

def analyze_users(target_nick_name, name_index, tag, head, only_match_len_and_start=False):
    target2info = {}

    for casting_id in commoninfo.CastingId2MetaInfo:
        casting_name = commoninfo.CastingId2MetaInfo[casting_id][0]
        casting_ch_name = commoninfo.CastingId2MetaInfo[casting_id][1]
        result_file_name = "data/{}/{}/_grab_nft_price_result_{}_{}.csv".format(
            tag, casting_name,
            casting_name, tag
        )
        cnt = 0
        target_min_price = None
        target_max_price = None
        target_total_price = 0
        target_cnt = 0
        #if not os.path.exists(result_file_name):
        #    continue
        with open(result_file_name,  encoding="utf-8-sig") as result_file:
            for line in result_file:
                cnt += 1
                if cnt <= 2:
                    # 忽略总结行和标题行
                    continue
                items = line.strip().split(",")
                nickname = items[name_index]
                if only_match_len_and_start and len(nickname) > 0:
                    nickname = nickname[0] + "*"*(len(nickname)-1)
                #print(nickname)
                price = float(items[TRANS_PRICE_INDEX])
                if nickname == target_nick_name:
                    target_cnt += 1
                    if not target_min_price:
                        target_min_price = price
                    if not target_max_price:
                        target_max_price = price
                    if price < target_min_price:
                        target_min_price = price
                    if price > target_max_price:
                        target_max_price = price
                    target_total_price += price
            target2info[casting_ch_name] = [target_cnt, target_min_price, target_max_price, 
                target_total_price / target_cnt if target_cnt > 0 else None, target_total_price]
    
    target_infos = []
    for casting_ch_name in target2info:
        info = [casting_ch_name]
        info.extend(target2info[casting_ch_name])
        target_infos.append(info)
    target_infos.sort(key=lambda i: i[-1], reverse=True)
    
    # 输出
    content = "**{}:{}**\n".format(head, tag)
    for (casting_ch_name, cnt, min_price, max_price, avg_price, total_price) in target_infos:
        if cnt > 0:
            content += "{}\n>数量:{}\n>最低价:{}\n>最高价:{}\n>均价:{}\n>合计:{}\n\n".format(
                casting_ch_name, cnt, min_price,
                max_price, avg_price, total_price)
    utils.send_workwx_msg("markdown", content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <tag>".format(sys.argv[0]))
        sys.exit(1)
    tag = sys.argv[1]

    ## 黑8
    analyze_users(BLACK8_NICK_NAME, BUYER_NAME_INDEX, tag, "黑8-买入")
    analyze_users(BLACK8_NICK_NAME, SELLER_NAME_INDEX, tag, "黑8-卖出", True)

    ## 翃翾
    analyze_users(HONG_NICK_NAME, BUYER_NAME_INDEX, tag, "翃翾-买入")
    analyze_users(HONG_NICK_NAME, SELLER_NAME_INDEX, tag, "翃翾-卖出", True)