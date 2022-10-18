# coding: utf-8
from datetime import datetime
import requests
import time
import sys

from gycommon import commoninfo
from gycommon import utils

GET_ON_SALE_LIST_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/onSale"
PAGE_SIZE = 10
TIME_OUT = 3
GET_PRODUCT_DETAIL_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/collectionDetails"
BUY_URL = "https://api.gandart.com/base/v2/resaleManage/resale/buy"

TRAN_STATUS_SALING = 2

PROD_ID_INDEX = 0
PRICE_INDEX = 2

# 131
HOME_PC_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIxNzM2MjE4Njk2MSIsInNvdXJjZSI6InBjIiwidHlwZSI6ImN1c3RvbWVyIiwiZXhwIjoxNjY2MTAzOTc1LCJzaWduSWQiOiI3YTI0ODNjZjYwMGY0MGQ5YmNmOWUwNTAyY2M0N2Y0ZSIsImlhdCI6MTY2NTQ5OTE3NX0.YcexoKivFKbnwIQYxAAPMah3Y-wjm16RCSOTolcuxZs"
#159
DESKTOP_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIxNTkxMDYxOTk2MyIsInNvdXJjZSI6InBjIiwidHlwZSI6ImN1c3RvbWVyIiwiZXhwIjoxNjY2NTc4NTE4LCJzaWduSWQiOiJhZDE0OGYxYzUzNzY0MTVkODgxZmI2ZjcyMjgyZmU3NSIsImlhdCI6MTY2NTk3MzcxOH0.1zrXRh-UMNYwbyoBTQKK7Qvcc111BvkT9DEhEC_I504"

CastingId2Price_1 = {
    54: 2000, # 开拓者
    59: 2000, # 万象龙巢
    #56: 100, # Ctrl  #2022/10/11结束合成
    #66: 400, # V #2022/10/11结束合成
    #67: 400, # C #2022/10/11结束合成

    #31: 100, # 厚土
    #32: 300, # 甘霖
    #33: 1000, # 灰烬
    #30: 2000, # 浮金

    #75: 400, # 龙凤筷
    79: 200, # 龙图腾
}

CastingId2Price_2 = {
    # 32: 200, # 甘霖
    33: 1000, # 灰烬
    30: 2000, # 浮金

    80: 2000, # 龙凤守宝
    #60: 40, # Shift
    #61: 200, # 太空Shift
}

CastingId2Price_3 = {
    #83: 150, # 探索者-Ctrl
    #84: 100, # 探索者-Shift
    #32: 500, # 甘霖
    87:  1900,
}

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
        "pageSize":PAGE_SIZE,
        "sort":2,
        "transactionStatus": TRAN_STATUS_SALING,
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

def get_product_detail_id(prod_id):
    data = {
        "transactionRecordId": prod_id,
    }
    detail_id = None
    user_id = None
    #created_time = None
    while True:
        try: 
            res = requests.post(GET_PRODUCT_DETAIL_URL, data=data, timeout=TIME_OUT).json()
            if res["code"] != 0:
                return (None, None)
            else:
                detail_id = res["obj"]["detailId"]
                user_id = res["obj"]["userId"]
                #created_time = datetime.datetime.strptime(res["obj"]["created"], "%Y-%m-%d %H:%M:%S")
                break
        except Exception as e:
            time.sleep(0.5)
            print(e)
    return (detail_id, user_id)

def buy_product(casting_id, prod_id, detail_id, user_id, token):
    data =  {
        "castingId": casting_id,
        "detailId": detail_id,
        "transactionRecordId": prod_id,
        "userId": user_id,
    }

    headers = {
        "token": token,
    }

    while True:
        try: 
            res = requests.post(BUY_URL, data=data, headers=headers, timeout=TIME_OUT).json()
            if not res["success"]:
                print("下单失败: {} casting_id={},prod_id={},msg={}".format(
                    datetime.now(), casting_id, prod_id, res["msg"]))
                return False
            else:
                return True
        except Exception as e:
            time.sleep(0.5)
            print(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    dict_id = int(sys.argv[1])
    castingid2price = None
    token = None
    if dict_id == 1:
        castingid2price = CastingId2Price_1
        token = HOME_PC_TOKEN
    elif dict_id == 2:
        castingid2price = CastingId2Price_2
        token = HOME_PC_TOKEN
    elif dict_id == 3:
        castingid2price = CastingId2Price_3
        token = DESKTOP_TOKEN
    if not castingid2price:
        print("dict_id={} 没有对应信息!".format(dict_id))
        sys.exit(1)
    print(castingid2price)

    with open("mailconfig") as config_file:
        items = config_file.readline().strip().split(",")
        from_addr = items[0]
        password = items[1]
        to_addr = items[2]
    
    loop_cnt = 0
    while True:
        try:
            for casting_id in castingid2price:
                (res_code, saling_prods) = get_top_saling_products(casting_id)
                if res_code != 0:
                    print("获取在售列表信息失败, res_code={}, casting_id={}".format(res_code, casting_id))
                    continue
                for saling_prod in saling_prods:
                    prod_id = saling_prod[PROD_ID_INDEX]
                    price = saling_prod[PRICE_INDEX]
                    if price <= castingid2price[casting_id]:
                        (detail_id, user_id) = get_product_detail_id(prod_id)
                        if not detail_id:
                            print("获取detail_id失败, prod_id={}".format(prod_id))
                            continue
                        prod_name = commoninfo.CastingId2MetaInfo[casting_id][1]
                        if buy_product(casting_id, prod_id, detail_id, user_id, token):
                            msg = "购买 {}:{}:{}".format(datetime.now(), prod_name, price)
                            print(msg)
                            utils.send_msg(from_addr, password, to_addr, msg)
                        else:
                            msg = "下单失败 {}:{}:{}".format(datetime.now(), prod_name, price)
                            print(msg)
                            #utils.send_msg(from_addr, password, to_addr, msg)
                # 防止被封禁
                time.sleep(1)
                    
            loop_cnt += 1
            #print(loop_cnt)
            if loop_cnt % 100 == 0:
                print("{} {} rounds.".format(datetime.now(), loop_cnt))

            # 判断时间是否超过0点
            cur_time = datetime.now()
            if cur_time.hour == 0 :
                break
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(3)
    