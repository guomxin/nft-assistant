# coding: utf-8

import sys
import os

from gycommon import commoninfo
from gycommon import utils

BLACK8_NICK_NAME = "s*****"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <tag>".format(sys.argv[0]))
        sys.exit(1)
    tag = sys.argv[1]

    black82info = {}

    for casting_id in commoninfo.CastingId2MetaInfo:
        casting_name = commoninfo.CastingId2MetaInfo[casting_id][0]
        casting_ch_name = commoninfo.CastingId2MetaInfo[casting_id][1]
        result_file_name = "data/_grab_nft_price_result_{}_{}.csv".format(
            casting_name, tag
        )
        #print(result_file_name)
        cnt = 0
        b8_min_price = None
        b8_max_price = None
        b8_total_price = 0
        b8_cnt = 0
        #if not os.path.exists(result_file_name):
        #    continue
        with open(result_file_name,  encoding="utf-8-sig") as result_file:
            for line in result_file:
                cnt += 1
                if cnt <= 2:
                    # 忽略总结行和标题行
                    continue
                items = line.strip().split(",")
                buyer_nickname = items[2]
                price = float(items[4])
                if buyer_nickname == BLACK8_NICK_NAME:
                    b8_cnt += 1
                    if not b8_min_price:
                        b8_min_price = price
                    if not b8_max_price:
                        b8_max_price = price
                    if price < b8_min_price:
                        b8_min_price = price
                    if price > b8_max_price:
                        b8_max_price = price
                    b8_total_price += price
            black82info[casting_ch_name] = [b8_cnt, b8_min_price, b8_max_price, 
                b8_total_price / b8_cnt if b8_cnt > 0 else None, b8_total_price]
    
    black8_infos = []
    for casting_ch_name in black82info:
        info = [casting_ch_name]
        info.extend(black82info[casting_ch_name])
        black8_infos.append(info)
    black8_infos.sort(key=lambda i: i[-1], reverse=True)
    
    # 输出
    content = "**黑8:{}**\n".format(tag)
    for (casting_ch_name, cnt, min_price, max_price, avg_price, total_price) in black8_infos:
        if cnt > 0:
            content += "{}\n>数量:{}\n>最低价:{}\n>最高价:{}\n>均价:{}\n>合计:{}\n\n".format(
                casting_ch_name, cnt, min_price,
                max_price, avg_price, total_price)
    utils.send_workwx_msg("markdown", content)
            
        