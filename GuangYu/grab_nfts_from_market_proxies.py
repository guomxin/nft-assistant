# coding: utf-8
from datetime import datetime
import requests
import time
import sys
import random

from gycommon import commoninfo
from gycommon import utils

GET_ON_SALE_LIST_URL = "https://api2.gandart.com/market/api/v2/resaleManage/resale/onSale"
PAGE_SIZE = 50
TIME_OUT = 3
GET_PRODUCT_DETAIL_URL = "https://api2.gandart.com/market/api/v2/resaleManage/resale/collectionDetails"
BUY_URL = "https://api.gandart.com/base/v2/resaleManage/resale/buy/v2"

TRAN_STATUS_SALING = 2

PROD_ID_INDEX = 0
PRICE_INDEX = 2
TRANS_STATUS_INDEX = 3
#WALLET_LIST_INDEX = 4

"""
    [{
    "http": "http://7408150:se3cvgbh@121.42.177.10:16818/",
    "https": "http://7408150:se3cvgbh@121.42.177.10:16818/"
    }, 0.1],

    [{
    "http": "http://7408150:se3cvgbh@42.51.39.88:16818/",
    "https": "http://7408150:se3cvgbh@42.51.39.88:16818/"
    }, 0.1],

    [{
    "http": "http://7408150:se3cvgbh@122.114.234.157:16817/",
    "https": "http://7408150:se3cvgbh@122.114.234.157:16818/"
    }, 0.1],
"""

Proxies_List = [
    [{
    "http": "http://7408150:se3cvgbh@123.56.246.33:16817/",
    "https": "http://7408150:se3cvgbh@123.56.246.33:16817/"
    }, 0.5],

    [{
    "http": "http://7408150:se3cvgbh@114.215.174.49:16817/",
    "https": "http://7408150:se3cvgbh@114.215.174.49:16817/"
    }, 0.3],

    [{
    "http": "http://7408150:se3cvgbh@121.41.8.23:16816/",
    "https": "http://7408150:se3cvgbh@121.41.8.23:16816/"
    }, 0.3],
]

Targets_List = [
    #{4642: 30, 4644: 148},
    #{4575: 38, 4642: 30},
    #{4805: 500, 3457: 30},
    #{4716: 20, 4824: 68},
    #{4716: 20},
    #{4654: 238},
    #{4655:48},
    {4833:58},
    {4678: 100, 4833:58},
    #{4228: 5, 4412:30},
    #{4708:428},
    #{4723: 5},
    #{4667:100},
    #{4642: 30, 4577: 200},
]

def post_requests_json(url, headers, data, proxies, timeout, decorate=False):
    for _ in range(10):
        try:
            if decorate:
                data = utils.decorate_api_data(data)
            res = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(3)
            print(e)

def get_top_saling_products(casting_id, proxies):
    saling_prods = []
    data = {
        "castingId": casting_id,
        "page":1,
        "pageSize":PAGE_SIZE,
        "sort":2,
        "transactionStatus": TRAN_STATUS_SALING,
    }
    data = utils.decorate_api_data(data)
    res = post_requests_json(GET_ON_SALE_LIST_URL, commoninfo.GanDart_Headers, data, proxies, TIME_OUT, decorate=True)
    if not res:
        return (1, None)
    if res["code"] != 0:
        return (res["code"], None)
    else:
        #print(res)
        for pinfo in res["obj"]["list"]:
            walletList = pinfo["walletList"]
            # 忽略只能用C钱包购买的商品
            if len(walletList) == 1 and walletList[0] == 'C':
                continue
            saling_prods.append(
                [pinfo["id"], pinfo["viewSort"], float(pinfo["resalePrice"]), pinfo["transactionStatus"], pinfo["walletList"]])
    return (0, saling_prods)

def get_product_detail_id(prod_id, proxies):
    data = {
        "transactionRecordId": prod_id,
    }
    detail_id = None
    user_id = None
    #created_time = None
    while True:
        try:
            data = utils.decorate_api_data(data) 
            res = requests.post(GET_PRODUCT_DETAIL_URL, data=data, headers= commoninfo.GanDart_Headers, proxies=proxies, timeout=TIME_OUT).json()
            if res["code"] != 0:
                return (None, None)
            else:
                detail_id = res["obj"]["detailId"]
                user_id = res["obj"]["id"]
                #created_time = datetime.datetime.strptime(res["obj"]["created"], "%Y-%m-%d %H:%M:%S")
                break
        except Exception as e:
            time.sleep(3)
            print(e)
    return (detail_id, user_id)

def buy_product(casting_id, prod_id, token, proxies):
    data = {
        #"castingId": casting_id,
        #"detailId": detail_id,
        "transactionRecordId": prod_id,
        #"userId": user_id,
    }

    headers = {
    }
    headers["token"] = token

    while True:
        try: 
            data = utils.decorate_api_data(data)
            res = requests.post(BUY_URL, data=data, headers=headers, proxies=proxies, timeout=TIME_OUT).json()
            if not res["success"]:
                print("下单失败: {} casting_id={},prod_id={},msg={}".format(
                    datetime.now(), casting_id, prod_id, res["msg"]))
                return False
            else:
                return True
        except Exception as e:
            time.sleep(3)
            print(e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <proxies_id> <target_id> <crazy_mode>(缺省为1).".format(sys.argv[0]))
        sys.exit(1)
    proxy_id = int(sys.argv[1])
    target_id = int(sys.argv[2])
    crazy_mode = True
    if len(sys.argv) >= 4:
        crazy_mode = (int(sys.argv[3]) > 0)
    token = commoninfo.Home_Token
    proxies = Proxies_List[proxy_id][0]
    proxy_sleep_time = Proxies_List[proxy_id][1]
    castingid2price = Targets_List[target_id]

    """
    lp_cnt = 0
    while True:
        lp_cnt += 1
        cur_time = datetime.now()
        if cur_time.hour != 2:
            if lp_cnt % 120 == 0:
                print(cur_time)
                lp_cnt = 0
            time.sleep(0.5) 
        else:
            break
    """

    for casting_id in castingid2price:
        print("{}:{}".format(commoninfo.CastingId2MetaInfo[casting_id][1], castingid2price[casting_id]))
    print("疯狂模式:{}".format(crazy_mode))

    loop_cnt = 0
    wx_msg_count = 0
    while True:
        try:
            for casting_id in castingid2price:
                (res_code, saling_prods) = get_top_saling_products(casting_id, proxies)
                if res_code != 0:
                    print("获取在售列表信息失败, res_code={}, casting_id={}".format(res_code, casting_id))
                    continue
                for saling_prod in saling_prods:
                    prod_id = saling_prod[PROD_ID_INDEX]
                    price = saling_prod[PRICE_INDEX]
                    trans_status = saling_prod[TRANS_STATUS_INDEX]
                    if not crazy_mode:
                        if trans_status != TRAN_STATUS_SALING:
                            continue
                    if price <= castingid2price[casting_id]:
                        #(detail_id, user_id) = get_product_detail_id(prod_id, proxies)
                        #if not detail_id:
                        #    print("获取detail_id失败, prod_id={}".format(prod_id))
                        #    continue
                        prod_name = commoninfo.CastingId2MetaInfo[casting_id][1]
                        #print(prod_name, price, prod_id)
                        if buy_product(casting_id, prod_id, token, proxies):
                            content = """
光予: 购买{}
>时间: {}
>价格: {}""".format(prod_name, datetime.now(), price)
                            print(content)
                            utils.send_workwx_msg_agg(utils.GrabNFTs_MSG, "markdown", content)
                            """
                            msg = "购买 {}:{}:{}".format(datetime.now(), prod_name, price)
                            print(msg)
                            utils.send_msg(from_addr, password, to_addr, msg)
                            """
                        else:
                            wx_msg_count += 1
                            if wx_msg_count == 50:
                                content = """
光予: 下单失败{}
>时间: {}
>价格: {}""".format(prod_name, datetime.now(), price)
                                print(content)
                                utils.send_workwx_msg_agg(utils.GrabNFTs_MSG, "markdown", content)
                                wx_msg_count = 0
                            """                       
                            msg = "下单失败 {}:{}:{}".format(datetime.now(), prod_name, price)
                            print(msg)
                            #utils.send_msg(from_addr, password, to_addr, msg)
                            """
                # 防止被封禁
                time.sleep(proxy_sleep_time)
                #time.sleep(random.random())
                    
            loop_cnt += 1
            #print(loop_cnt)
            if loop_cnt % 100 == 0:
                print("{} {} rounds.".format(datetime.now(), loop_cnt))

            # 判断时间是否超过0点
            #cur_time = datetime.now()
            #if cur_time.hour == 0 :
            #    break
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(3)
    