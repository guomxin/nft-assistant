# coding: utf-8
from datetime import datetime
import requests
import time
import sys
import random

from gycommon import commoninfo
from gycommon import utils

GET_ALL_SALE_LIST_URL = "https://api.gandart.com/corecenter/userSaleRecords/es/querySaleToElasticSearch"
PAGE_SIZE = 300
TIME_OUT = 3
GET_CASTING_DETAIL_URL = "https://api2.gandart.com/market/api/v2/resaleManage/resale/collectionDetailsByCastingId"
BUY_URL = "https://api.gandart.com/base/v2/resaleManage/resale/buy/v2"
PAY_URL = "https://api.gandart.com/api/v2/wallet/sand/pay"

TRAN_STATUS_SALING = 2

CASTING_ID_INDEX = 0
PROD_ID_INDEX = 1
PRICE_INDEX = 3
TRANS_STATUS_INDEX = 4

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
    "http": "http://7408150:se3cvgbh@122.114.234.157:16818/",
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

def post_requests_pure_json(url, headers, data, proxies, timeout, decorate=False):
    for _ in range(10):
        try:
            if decorate:
                data = utils.decorate_api_data(data)
            res = requests.post(url, json=data, headers=headers, proxies=proxies, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(3)
            print(e)

def get_all_saling_products(proxies):
    saling_prods = []
    data = {
        "classifyId": 24,
        #"collectionName": "",
        #"createdSort": "null",
        "page": 1,
        "pageSize": PAGE_SIZE,
        "priceSort": 1,
        "type": 24,
    }
    data = utils.decorate_api_data(data)
    GanDart_Headers = {
        "Host": "api.gandart.com",
        "Origin": "https://www.gandart.com",
        "Referer": "https://www.gandart.com/",
        "token": commoninfo.Query_Token,
        "Content-Type": "application/json;charset=UTF-8;",
    }
    res = post_requests_pure_json(GET_ALL_SALE_LIST_URL, GanDart_Headers, data, proxies, TIME_OUT, decorate=True)
    if not res:
        return (1, None)
    if res["code"] != 0:
        return (res["code"], None)
    else:
        #print(res)
        for sinfo in res["data"]["list"]:
            if sinfo["resalePrice"]:
                saling_prods.append(
                    [sinfo["castingId"], sinfo["id"], sinfo["viewSort"], float(sinfo["resalePrice"]), sinfo["transactionStatus"]])
            else:
                ### 已退市藏品无price
                pass
    return (0, saling_prods)

def get_casting_detail_id(casting_id, proxies):
    data = {
        "castingId": casting_id,
    }
    
    while True:
        try:
            data = utils.decorate_api_data(data) 
            res = requests.post(GET_CASTING_DETAIL_URL, data=data, headers= commoninfo.GanDart_Headers, proxies=proxies, timeout=TIME_OUT).json()
            if res["code"] != 0:
                return (None, None, None)
            else:
                prod_id = res["obj"]["id"]
                price = res["obj"]["resalePrice"]
                walletList = res["obj"]["walletList"]
                break
        except Exception as e:
            time.sleep(3)
            print(e)
    return (prod_id, price, walletList)

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
                return (-1, None)
            else:
                return (0, res["obj"]["orderNum"])
        except Exception as e:
            time.sleep(3)
            print(e)

def pay(casting_id, prod_id, order_num, token, proxies):
    data = {
        "orderNum": order_num,
        "castingId": casting_id,
        "transactionRecordId": prod_id,
        #"userId": user_id,
    }

    headers = {
    }
    headers["token"] = token

    while True:
        try: 
            data = utils.decorate_api_data(data)
            res = requests.post(PAY_URL, data=data, headers=headers, proxies=proxies, timeout=TIME_OUT).json()
            if not res["success"]:
                print("支付失败: {} casting_id={},prod_id={},msg={}".format(
                    datetime.now(), casting_id, prod_id, res["msg"]))
                return (-1, None)
            else:
                print(res)
                return (0, res["obj"]["passwordURL"])
        except Exception as e:
            time.sleep(3)
            print(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <proxies_id> <crazy_mode>(缺省为1).".format(sys.argv[0]))
        sys.exit(1)
    proxy_id = int(sys.argv[1])
    crazy_mode = True
    if len(sys.argv) >= 3:
        crazy_mode = (int(sys.argv[2]) > 0)
    token = commoninfo.Home_Token
    proxies = Proxies_List[proxy_id][0]
    proxy_sleep_time = Proxies_List[proxy_id][1]

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
    print("ProxyId:{}, 疯狂模式:{}".format(proxy_id, crazy_mode))

    loop_cnt = 0
    wx_msg_count = 0
    while True:
        try:
            (res_code, saling_prods) = get_all_saling_products(proxies)
            if res_code != 0:
                print("获取在售列表信息失败, res_code={}, casting_id={}".format(res_code))
                time.sleep(1)
                continue
            for saling_prod in saling_prods:
                casting_id = int(saling_prod[CASTING_ID_INDEX])
                if casting_id not in commoninfo.CastingId2MetaInfo:
                    continue
                min_price = commoninfo.DEFAULT_MIN_PRICE
                if len(commoninfo.CastingId2MetaInfo[casting_id]) >= 3:
                    min_price = commoninfo.CastingId2MetaInfo[casting_id][2] 
                prod_id = saling_prod[PROD_ID_INDEX]
                price = saling_prod[PRICE_INDEX]
                trans_status = int(saling_prod[TRANS_STATUS_INDEX])
                if not crazy_mode:
                    if trans_status != TRAN_STATUS_SALING:
                        continue
                #if (price <= min_price) and ((min_price - price) / min_price <= 0.2):
                if price <= min_price:
                    (prod_id, price, walletList) = get_casting_detail_id(casting_id, proxies)
                    if not prod_id or not price:
                    # 1.获取失败，这时prod_id和price都为None
                    # 2.有时产品被抢后，进入产品页面正好已退市状态，这时prod_id和price都为空
                        print("获取prod_id失败, prod_id={}".format(prod_id))
                        continue
                    # 产品被抢后，进入产品页面这时价格为原来第二低价格，需要重新判断
                    price = float(price)
                    if price > min_price:
                        continue
                    # 忽略只能用C钱包购买的商品
                    if len(walletList) == 1 and walletList[0] == 'C':
                        print("只能用C钱包付款, prod_id={}".format(prod_id))
                        continue
                    prod_name = commoninfo.CastingId2MetaInfo[casting_id][1]
                    print(prod_name, price, prod_id)
                    (res_code, order_num) = buy_product(casting_id, prod_id, token, proxies)
                    if res_code == 0:
                        content = """
光予: 购买{}
>时间: {}
>价格: {}""".format(prod_name, datetime.now(), price)
                        print(content)
                        utils.send_workwx_msg_agg(utils.GrabNFTs_MSG, "markdown", content)
                        (res_code, password_url) = pay(casting_id, prod_id, order_num, token, proxies)
                        if res_code == 0:
                            utils.send_workwx_msg_agg(utils.GrabNFTs_MSG, "text", "{}:{}:{}".format(
                                prod_name, price, password_url))
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
    