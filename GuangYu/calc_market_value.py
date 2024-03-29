# coding: utf-8

import sys
import datetime
import requests
import time

from gycommon import commoninfo
from gycommon import utils
from holdingshare import MyHoldingShare

TIME_OUT = 3
CASTING_INFO_COLL_AMOUNT_INDEX = 0
CASTING_INFO_CIRCU_INDEX = 1
CASTING_INFO_ONSALE_AMOUNT_INDEX = 2
CASTING_INFO_ITEM_COUNT = 3
GET_CASTING_INFO_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/collectionDetailsByCastingId"

GET_ON_SALE_LIST_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/onSale"
PRICE_INDEX = 2

def get_top_saling_products(casting_id):
    saling_prods = []
    data = {
        "castingId": casting_id,
        "page":1,
        "pageSize":10,
        "sort":2,
        "transactionStatus": 2,
    }
    data = utils.decorate_api_data(data)
    res = utils.post_requests_json(GET_ON_SALE_LIST_URL, headers=commoninfo.GanDart_Headers, data=data, timeout=TIME_OUT, decorate=True)
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
            data = utils.decorate_api_data(data)
            res = requests.post(GET_CASTING_INFO_URL, headers=commoninfo.GanDart_Headers, data=data, timeout=TIME_OUT).json()
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
    casting2holding = {}
    total_value = 0
    total_fourth_value = 0
    total_sixth_value = 0
    total_11th_value = 0
    my_share_value = 0
    for casting_id in commoninfo.CastingId2MetaInfo:
        #if casting_id == 87 or casting_id == 75:
        #    # 忽略凤图腾和龙凤筷
        #    continue
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
                fourth_price = commoninfo.HighestValue_Products_Info[casting_id][1]
                sixth_price = commoninfo.HighestValue_Products_Info[casting_id][1]
                eleth_price = commoninfo.HighestValue_Products_Info[casting_id][1]
            else:
                min_price = saling_prods[0][PRICE_INDEX]
                if len(saling_prods) > 3:
                    fourth_price = saling_prods[3][PRICE_INDEX]
                else:
                    fourth_price = saling_prods[-1][PRICE_INDEX]
                if len(saling_prods) > 5:
                    sixth_price = saling_prods[5][PRICE_INDEX]
                else:
                    sixth_price = saling_prods[-1][PRICE_INDEX]
                if len(saling_prods) > 10:
                    eleth_price = saling_prods[10][PRICE_INDEX]
                else:
                    eleth_price = saling_prods[-1][PRICE_INDEX]
        else:
            # 已退市或关闭寄售
            if casting_id in commoninfo.HighestValue_Products_Info:
                # 已退市，按最高限价计算
                print("\t已退市, casting={}".format(casting_name))
                circu_cnt = commoninfo.HighestValue_Products_Info[casting_id][0]
                min_price = commoninfo.HighestValue_Products_Info[casting_id][1]
                fourth_price = commoninfo.HighestValue_Products_Info[casting_id][1]
                sixth_price = commoninfo.HighestValue_Products_Info[casting_id][1]
                eleth_price = commoninfo.HighestValue_Products_Info[casting_id][1]
            else:
                # 已关闭寄售，暂不处理
                print("\t已关闭寄售, casting={}".format(casting_name))
                continue

        casting2value[casting_name] = [circu_cnt, min_price, circu_cnt * min_price]
        my_holding_cnt = 0
        if casting_id in MyHoldingShare:
            my_holding_cnt = MyHoldingShare[casting_id][2]
        if my_holding_cnt > 0:
            casting2holding[casting_name] = [my_holding_cnt, min_price, min_price * my_holding_cnt]
        total_value += circu_cnt * min_price
        total_fourth_value += circu_cnt * fourth_price
        total_sixth_value += circu_cnt * sixth_price
        total_11th_value += circu_cnt * eleth_price
        my_share_value += my_holding_cnt * min_price
    
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

    share_value_infos = []
    for casting_name in casting2holding:
        share_value_infos.append([
            casting_name,
            casting2holding[casting_name][0],
            casting2holding[casting_name][1],
            casting2holding[casting_name][2],            
        ])
    share_value_infos.sort(key=lambda si: si[3], reverse=True)

    # 输出
    content = "**{} 光予市值:{:.2f}万**\n".format(tag, total_value / 10000)
    for (casting_name, circu_cnt, min_price, mvalue) in casting_value_infos:
        content += "{}\n>流通量:{}\n>挂牌最低价:{}\n>市值:{:.2f}万\n\n".format(
            casting_name, circu_cnt, 
            min_price, mvalue / 10000)
    utils.send_workwx_msg_agg(utils.StockValue_MSG, "markdown", content)

    content = "**{} 我的持仓:{:.2f}万**\n".format(tag, my_share_value / 10000)
    for (casting_name, holding_cnt, min_price, hvalue) in share_value_infos:
        content += "{}\n>持仓量:{}\n>当前最低价:{}\n>当前价值:{:.2f}万\n\n".format(
            casting_name, holding_cnt, 
            min_price, hvalue / 10000)
    utils.send_workwx_msg_agg(utils.HoldingShare_MSG, "markdown", content)

    result_file_name = "data/_calc_market_value_{}.csv".format(
        tag
    )
    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        result_file.write("总市值: {:.2f}万\n".format(total_value / 10000))
        result_file.write("总市值(4th): {:.2f}万\n".format(total_fourth_value / 10000))
        result_file.write("总市值(6th): {:.2f}万\n".format(total_sixth_value / 10000))
        result_file.write("总市值(11th): {:.2f}万\n".format(total_11th_value / 10000))
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
