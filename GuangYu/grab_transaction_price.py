# coding: utf-8

import sys
import datetime
import requests
import time
import os

from gycommon import commoninfo

GET_ON_SALE_LIST_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/onSale"
PAGE_SIZE = 10000
TIME_OUT = 3
GET_PRODUCT_DETAIL_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/collectionDetails"
GET_TRANS_INFO_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/transactionInfo"

TRAN_STATUS_SALED = 1

PROD_ID_INDEX = 0
TOKEN_ID_INDEX = 1
PRICE_INDEX = 2
CREATE_TINE_INDEX = 3

DETAIL_SELLER_ID_INDEX = 0
DETAIL_SELLER_INDEX = 1
DETAIL_BUYER_INDEX = 2
DETAIL_SALE_TIME_INDEX = 3
DETAIL_PRICE_INDEX = 4
DETAIL_TOKEN_ID_INDEX = 5
DETAIL_PROD_ID_INDEX = 6
DETAIL_DETAIL_ID_INDEX = 7
DETAIL_ITEM_COUNT = 8

def post_requests_json(url, data, timeout):
    for _ in range(10):
        try:
            res = requests.post(url, data=data, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(0.5)
            print(e)

def get_saled_products(casting_id):
    saled_prods = []
    data = {
        "castingId": casting_id,
        "page":1,
        "pageSize":PAGE_SIZE,
        "sort":2,
        "transactionStatus": TRAN_STATUS_SALED,
    }
    res = post_requests_json(GET_ON_SALE_LIST_URL, data=data, timeout=TIME_OUT)
    if not res:
        return (1, None)
    if res["code"] != 0:
        return (res["code"], None)
    else:
        for pinfo in res["obj"]["list"]:
            saled_prods.append(
                [pinfo["id"], pinfo["viewSort"], float(pinfo["resalePrice"])])
        total = res["obj"]["total"]
        for pindex in range(2, total // PAGE_SIZE + 2):
            data = {
                "castingId": casting_id,
                "page":pindex,
                "pageSize":PAGE_SIZE,
                "sort":2,
                "transactionStatus": TRAN_STATUS_SALED,
            }
            res = post_requests_json(GET_ON_SALE_LIST_URL, data=data, timeout=3)
            if res["code"] != 0:
                return (res["code"], None)
            else:
                for pinfo in res["obj"]["list"]:
                    saled_prods.append(
                        [pinfo["id"], pinfo["viewSort"], float(pinfo["resalePrice"])])
    return (0, saled_prods)

def get_product_detail(prod_id):
    detail_info = [None] * DETAIL_ITEM_COUNT

    # Get detail data
    data = {
        "transactionRecordId": prod_id,
    }
    detail_id = None
    user_id = None
    created_time = None
    while True:
        try: 
            res = requests.post(GET_PRODUCT_DETAIL_URL, data=data, timeout=TIME_OUT).json()
            if res["code"] != 0:
                return None
            else:
                detail_id = res["obj"]["detailId"]
                user_id = res["obj"]["userId"]
                created_time = datetime.datetime.strptime(res["obj"]["created"], "%Y-%m-%d %H:%M:%S")
                #print(detail_id, user_id, created_time)
                break
        except Exception as e:
            time.sleep(0.5)
            print(e)
    if not detail_id:
        return None
    
    # Get all recent transaction data
    data = {
        "detailId": detail_id,
        "page": 1,
        "pageSize": PAGE_SIZE,
    }
    while True:
        try: 
            res = requests.post(GET_TRANS_INFO_URL, data=data, timeout=TIME_OUT).json()
            if res["code"] != 0:
                return None
            else:
                trans = res["obj"]["history"]["list"]
                if len(trans) < 2:
                    print("detailId:{} 未获取到足够的交易信息!".format(detail_id))
                    return None
                # 找到相应的挂单记录，与detail接口的时间一致
                target_sell_index = None
                for i in range(len(trans)):
                    tinfo = trans[i]
                    if created_time == datetime.datetime.strptime(tinfo["created"], "%Y-%m-%d %H:%M:%S") and \
                        tinfo["sellPrice"]:
                        target_sell_index = i
                        break
                if target_sell_index == None:
                    print("productId:{}, detailId:{} 未发现匹配的交易记录!".format(prod_id, detail_id))
                    return None
                
                sell_price = trans[target_sell_index]["sellPrice"]
                target_buy_index = target_sell_index - 1
                
                # 如果买入和挂单时间一样，有时顺序会被打乱
                if target_buy_index < 0 or (not trans[target_buy_index]["buyPrice"]):
                    target_buy_index = target_sell_index + 1
                if target_buy_index >= len(trans): # ProdId:119695, DetailId:97124
                    return None

                buy_price = trans[target_buy_index]["buyPrice"]
                if sell_price != buy_price:
                    print("detailId:{} 买入{}和卖出{}价格不匹配".format(detail_id, buy_price, sell_price))
                    return None
                buyer_name = trans[target_buy_index]["nickName"]
                seller_name = trans[target_sell_index]["nickName"]
                
                detail_info[DETAIL_SELLER_ID_INDEX] = user_id
                detail_info[DETAIL_BUYER_INDEX] = buyer_name
                detail_info[DETAIL_SELLER_INDEX] = seller_name
                detail_info[DETAIL_SALE_TIME_INDEX] = datetime.datetime.strptime(trans[target_buy_index]["created"], "%Y-%m-%d %H:%M:%S")
                detail_info[DETAIL_PRICE_INDEX] = float(buy_price)
                detail_info[DETAIL_PROD_ID_INDEX] = prod_id
                detail_info[DETAIL_DETAIL_ID_INDEX] = detail_id
                break
        except Exception as e:
            time.sleep(0.5)
            print(e)
    
    return detail_info

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <casting_id> <tag>(YYYYmmdd)".format(sys.argv[0]))
        sys.exit(1)
    casting_id = int(sys.argv[1])
    if casting_id not in commoninfo.CastingId2MetaInfo:
        print("CastingId:{} not exist!")
        sys.exit(1)
    casting_name = commoninfo.CastingId2MetaInfo[casting_id][0]
    tag = sys.argv[2]
    start_time = datetime.datetime.strptime(tag + " 0:0:0", "%Y%m%d %H:%M:%S")
    end_time = datetime.datetime.strptime(tag + " 23:59:59", "%Y%m%d %H:%M:%S")

    (res_code, saled_prods) = get_saled_products(casting_id)
    if res_code != 0:
        print("获取在售列表信息失败, res_code={}".format(res_code))
        sys.exit(1)
    print("{} saled info in total.".format(len(saled_prods)))
    
    # 如果已存在交易信息文件，加载
    prodid2detailinfo = {}
    trans_logs_file_name = "data/" + commoninfo.Transaction_Logs_File_Name.format(casting_name)
    if os.path.exists(trans_logs_file_name):
        with open(trans_logs_file_name, encoding="utf-8-sig") as trans_logs_file:
            # 加载已有的交易信息
            for line in trans_logs_file:
                dinfo = [None] * DETAIL_ITEM_COUNT
                items = line.strip().split(",")
                dinfo[DETAIL_SELLER_ID_INDEX] = int(items[DETAIL_SELLER_ID_INDEX])
                dinfo[DETAIL_SELLER_INDEX] = items[DETAIL_SELLER_INDEX]
                dinfo[DETAIL_BUYER_INDEX] = items[DETAIL_BUYER_INDEX]
                dinfo[DETAIL_SALE_TIME_INDEX] = datetime.datetime.strptime(
                    items[DETAIL_SALE_TIME_INDEX], "%Y/%m/%d %H:%M:%S")
                dinfo[DETAIL_PRICE_INDEX] = float(items[DETAIL_PRICE_INDEX])
                dinfo[DETAIL_TOKEN_ID_INDEX] = int(items[DETAIL_TOKEN_ID_INDEX])
                dinfo[DETAIL_PROD_ID_INDEX] = int(items[DETAIL_PROD_ID_INDEX])
                dinfo[DETAIL_DETAIL_ID_INDEX] = int(items[DETAIL_DETAIL_ID_INDEX])
                prodid2detailinfo[dinfo[DETAIL_PROD_ID_INDEX]] = dinfo
    
    scan_cnt = 0
    selluser2cnt = {}
    detail_info_list = []
    for (prod_id, token_id, _) in saled_prods:
        if prod_id in prodid2detailinfo:
            detail_info = prodid2detailinfo[prod_id]
        else:
            detail_info = get_product_detail(prod_id)
            if not detail_info:
                print("无法获取ProdId:{}的详细信息!".format(prod_id))
                continue
            detail_info[DETAIL_TOKEN_ID_INDEX] = token_id
            prodid2detailinfo[prod_id] = detail_info
        scan_cnt += 1
        if scan_cnt % 100 == 0:
            print("{} saled info scanned.".format(scan_cnt))
        
        #print(prod_id, detail_info)
        if detail_info[DETAIL_SALE_TIME_INDEX] < start_time or detail_info[DETAIL_SALE_TIME_INDEX] > end_time:
            # 超出时间范围，忽略
            continue
        detail_info_list.append(detail_info)
        selluser = detail_info[DETAIL_SELLER_ID_INDEX]
        if selluser not in selluser2cnt:
            selluser2cnt[selluser] = 0
        selluser2cnt[selluser] += 1
    

    # 刷新交易信息文件
    with open(trans_logs_file_name, "w", encoding="utf-8-sig") as trans_logs_file:
        for (_, dinfo) in prodid2detailinfo.items():
            trans_logs_file.write("{},{},{},{},{},{},{},{}\n".format(
                dinfo[DETAIL_SELLER_ID_INDEX], dinfo[DETAIL_SELLER_INDEX], dinfo[DETAIL_BUYER_INDEX],
                dinfo[DETAIL_SALE_TIME_INDEX].strftime("%Y/%m/%d %H:%M:%S"), dinfo[DETAIL_PRICE_INDEX],
                dinfo[DETAIL_TOKEN_ID_INDEX], dinfo[DETAIL_PROD_ID_INDEX], dinfo[DETAIL_DETAIL_ID_INDEX]
            ))

    # 按成交时间倒序排序，输出
    detail_info_list.sort(key=lambda dinfo: dinfo[DETAIL_SALE_TIME_INDEX], reverse=True)
    result_file_name = "data/_grab_nft_price_result_{}_{}.csv".format(
        casting_name, tag
    )
    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        result_file.write("{},{},{},{},{},{},{},{}\n".format(
            "卖出者Id", "卖出者昵称", "买入者昵称", "买入时间", "价格", "TokenID", "DEBUG1", "DEBUG2"
        ))
        for dinfo in detail_info_list:
            result_file.write("{},{},{},{},{},{},{},{}\n".format(
                dinfo[DETAIL_SELLER_ID_INDEX], dinfo[DETAIL_SELLER_INDEX], dinfo[DETAIL_BUYER_INDEX],
                dinfo[DETAIL_SALE_TIME_INDEX].strftime("%Y/%m/%d %H:%M:%S"), dinfo[DETAIL_PRICE_INDEX],
                "#"+ str(dinfo[DETAIL_TOKEN_ID_INDEX]),
                dinfo[DETAIL_PROD_ID_INDEX], dinfo[DETAIL_DETAIL_ID_INDEX]
            ))

    # 输出卖出者信息
    sellers_info = []
    for s in selluser2cnt:
        sellers_info.append([s, selluser2cnt[s]])
    sellers_info.sort(key=lambda s: s[1], reverse=True)
    result_file_name = "data/_grab_nft_price_result_{}_{}.csv.sellersinfo.csv".format(
        casting_name, tag
    )
    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        for (sid, cnt) in sellers_info:
            result_file.write("{},{}\n".format(
                sid, cnt
            ))