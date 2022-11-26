# coding: utf-8

import sys
import datetime
import requests
import time

from gycommon import commoninfo
from gycommon import utils

TIME_OUT = 3
CASTING_INFO_COLL_AMOUNT_INDEX = 0
CASTING_INFO_CIRCU_INDEX = 1
CASTING_INFO_ONSALE_AMOUNT_INDEX = 2
CASTING_INFO_ITEM_COUNT = 3
GET_CASTING_INFO_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/collectionDetailsByCastingId"

def get_casting_info(casting_id):
    casting_info = [None] * CASTING_INFO_ITEM_COUNT

    # Get detail data
    data = {
        "castingId": casting_id,
    }

    while True:
        try:
            data = utils.decorate_api_data(data) 
            res = requests.post(GET_CASTING_INFO_URL, data=data, timeout=TIME_OUT).json()
            if res["code"] != 0:
                return None
            else:
                casting_info[CASTING_INFO_COLL_AMOUNT_INDEX] = res["obj"]["collectionAmount"]
                casting_info[CASTING_INFO_CIRCU_INDEX] = res["obj"]["collectionCirculation"]
                casting_info[CASTING_INFO_ONSALE_AMOUNT_INDEX] = res["obj"]["collectionSale"]
                break
        except Exception as e:
            time.sleep(0.5)
            print(e)
    return casting_info

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <casting_id> <tag>".format(sys.argv[0]))
        sys.exit(1)
    
    tag = sys.argv[1]

    result_file_name = "data/_scan_casts_result_{}.csv".format(
        tag
    )
    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        result_file.write("{}\n".format(datetime.datetime.now()))
        result_file.write("{},{},{},{}\n".format(
            "名称", "发行量", "流通量", "在售量"
        ))
        for casting_id in commoninfo.CastingId2MetaInfo:
            casting_name = commoninfo.CastingId2MetaInfo[casting_id][1]
            print("获取[{}]的信息...".format(casting_name))
            casting_info = get_casting_info(casting_id)
            time.sleep(1)
            if not casting_info:
                print("获取[{}]的信息失败！".format(casting_name))
                continue
            result_file.write("{},{},{},{}\n".format(
               casting_name,
               casting_info[CASTING_INFO_COLL_AMOUNT_INDEX], 
               casting_info[CASTING_INFO_CIRCU_INDEX],
               casting_info[CASTING_INFO_ONSALE_AMOUNT_INDEX]
            ))
