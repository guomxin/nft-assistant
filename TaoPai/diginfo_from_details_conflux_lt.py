# coding: utf-8

import sys
from datetime import datetime

LT_IdRange2Name = {
    (8382,8680): '19 野餐',
    (8083,8381): '18 未来',
    (7784,8082): '17 梦想',
    (7485,7783): '16 春天',
    (7186,7484): '15 我爱吃水果',
    (6887,7185): '14 亲爱的一家人',
    (6588,6886): '13 星空中的我们',
    (6289,6587): '12 呐喊',
    (5990,6288): '11 海蛞蝓',
    (5691,5989): '10 人与自然2',
    (5392,5690): '9 花开',
    (5093,5391): '8 日出',
    (4794,5092): '7 梦想起航机',
    (4495,4793): '6 宇航员登月球',
    (4196,4494): '5 和蓝天做游戏',
    (3897,4195): '4 丸子公主',
    (3598,3896): '3 布老虎',
    (3299,3597): '2 小陆宇宙探险之回归地球',
    (3000,3298): '1 虎年大吉'
}

def dig_a_nftinfo_from_details(details_file_name, min_tid, max_tid, dump_file_name):
    owner2tidcnt = {}
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        tokenids = [int(i) for i in items[2].split(":")]
        target_tid_cnt = 0
        for tid in tokenids:
            if (tid >= min_tid) and (tid <= max_tid):
                target_tid_cnt += 1
        if target_tid_cnt > 0:
            owner2tidcnt[owner] = target_tid_cnt
    
    # sort the info
    owner_tidcnt_list = []
    for (owner, tidcnt) in owner2tidcnt.items():
        owner_tidcnt_list.append((owner, tidcnt))
    owner_tidcnt_list.sort(key=lambda p: p[1], reverse=True)

    dump_file = open(dump_file_name, "w")
    for (owner, tidcnt) in owner_tidcnt_list:
        dump_file.write("{},{}\n".format(owner, tidcnt))
    dump_file.close()    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <function_id>(1:dig_a_nft_info)".format(sys.argv[0]))
        sys.exit(1)
    func_id = int(sys.argv[1])
    if func_id == 1:
        # dig_a_nftinfo_from_details
        details_file_name = sys.argv[2]
        min_tid = int(sys.argv[3])
        max_tid = int(sys.argv[4])
        dump_file_name = "_dig_a_nftinfo_conflux_lt_result_{}.csv".format(
            datetime.strftime(datetime.now(), '%Y%m%d%H%M'))
        dig_a_nftinfo_from_details(details_file_name, min_tid, max_tid, dump_file_name)