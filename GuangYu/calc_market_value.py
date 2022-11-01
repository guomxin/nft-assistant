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

GET_ON_SALE_LIST_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/onSale"
PRICE_INDEX = 2

def post_requests_json(url, data, timeout):
    for _ in range(10):
        try:
            res = requests.post(url, data=data, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(0.5)
            print(e)

def get_top_saling_products(casting_id):
    saling_prods = []
    data = {
        "castingId": casting_id,
        "page":1,
        "pageSize":10,
        "sort":2,
        "transactionStatus": 2,
    }
    res = post_requests_json(GET_ON_SALE_LIST_URL, data=data, timeout=TIME_OUT)
    if not res:
        return (1, None)
    if res["code"] != 0:
        return (res["code"], None)
    else:
        for pinfo in res["obj"]["list"]:
            saling_prods.append(
                [pinfo["id"], pinfo["viewSort"], float(pinfo["resalePrice"])])
    return (0, saling_prods)

def get_casting_info(casting_id):
    casting_info = [None] * CASTING_INFO_ITEM_COUNT

    # Get detail data
    data = {
        "castingId": casting_id,
    }
    
    while True:
        try: 
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
        print("{} <tag>".format(sys.argv[0]))
        sys.exit(1)
    tag = sys.argv[1]

    casting2value = {}
    total_value = 0
    for casting_id in commoninfo.CastingId2MetaInfo:
        if casting_id == 87:
            # 忽略凤图腾
            continue
        time.sleep(2)
        casting_name = commoninfo.CastingId2MetaInfo[casting_id][1]
        print("获取[{}]的信息...".format(casting_name))
        casting_info = get_casting_info(casting_id)
        if not casting_info:
            print("获取[{}]的信息失败！".format(casting_name))
            sys.exit(1)
        if casting_info[CASTING_INFO_CIRCU_INDEX] != "":
            circu_cnt = int(casting_info[CASTING_INFO_CIRCU_INDEX])
            (res_code, saling_prods) = get_top_saling_products(casting_id)
            if res_code != 0:
                print("获取在售列表信息失败, res_code={}, casting={}".format(res_code, casting_name))
                sys.exit(1)
            if len(saling_prods) == 0:
                # 按已退市，按最高限额计算
                print("\t无在售信息, casting={}".format(casting_name))
                min_price = commoninfo.HighestValue_Products_Info[casting_id][1]
            else:
                min_price = saling_prods[0][PRICE_INDEX]
        else:
            # 已退市或关闭寄售
            if casting_id in commoninfo.HighestValue_Products_Info:
                # 已退市，按最高限价计算
                print("\t已退市, casting={}".format(casting_name))
                circu_cnt = commoninfo.HighestValue_Products_Info[casting_id][0]
                min_price = commoninfo.HighestValue_Products_Info[casting_id][1]
            else:
                # 已关闭寄售，暂不处理
                print("\t已关闭寄售, casting={}".format(casting_name))
                continue

        casting2value[casting_name] = [circu_cnt, min_price, circu_cnt * min_price]
        total_value += circu_cnt * min_price
    
    casting_value_infos = []
    for casting_name in casting2value:
        casting_value_infos.append([
            casting_name,
            casting2value[casting_name][0], 
            casting2value[casting_name][1],
            casting2value[casting_name][2] 
        ])
    # 按最低挂单价倒序排序
    casting_value_infos.sort(key=lambda ci: ci[2], reverse=True)

    # 输出
    content = "**{} 光予市值:{:.2f}万**\n".format(tag, total_value / 10000)
    for (casting_name, circu_cnt, min_price, mvalue) in casting_value_infos:
        content += "{}\n>流通量:{}\n>挂牌最低价:{}\n>市值:{:.2f}万\n\n".format(
            casting_name, circu_cnt, 
            min_price, mvalue / 10000)
    utils.send_workwx_msg("markdown", content)

    result_file_name = "data/_calc_market_value_{}.csv".format(
        tag
    )
    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        result_file.write("总市值: {:.2f}万\n".format(total_value / 10000))
        result_file.write("{},{},{},{}\n".format(
            "名称", "流通量", "挂牌最低价", "市值(万)"
        ))
        for (casting_name, circu_cnt, min_price, mvalue) in casting_value_infos:
            result_file.write("{},{},{},{:.2f}\n".format(
               casting_name,
               circu_cnt, 
               min_price,
               mvalue / 10000
            ))
