# coding: utf-8
from datetime import datetime
import requests
import time
import sys
import random

from gycommon import commoninfo
from gycommon import utils

GET_ON_SALE_LIST_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/onSale"
PAGE_SIZE = 50
TIME_OUT = 3
GET_PRODUCT_DETAIL_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/collectionDetails"
BUY_URL = "https://api.gandart.com/base/v2/resaleManage/resale/buy"

TRAN_STATUS_SALING = 2

PROD_ID_INDEX = 0
PRICE_INDEX = 2
TRANS_STATUS_INDEX = 3

CastingId2Price_1 = {
    #54: 5000, # 开拓者
    #59: 5000, # 万象龙巢
    #56: 100, # Ctrl  #2022/10/11结束合成
    #66: 400, # V #2022/10/11结束合成
    #67: 400, # C #2022/10/11结束合成

    #31: 300, # 厚土
    #32: 2100, # 甘霖
    #33: 1000, # 灰烬
    #30: 2000, # 浮金

    #75: 400, # 龙凤筷
    #79: 500, # 龙图腾
    #46: 400, # 梦幻小龙

    #101: 1000, # 凤翊泪
    #71: 400, # 平安果
    #99: 2000, # 奇物秘宝-时间磨盘
    #100: 1300, # 奇物碎片-时间磨盘

    #104: 500, #["5-TongXingZheng", "电子通行证"],
    #105: 1020, #["5-BuLaoQuan", "充盈不老泉"],
    #106: 400, #["5-ShiZhiSha", "一抨时之砂"],
    #111: 1000, # 拾荒者
    #72: 2688, # 抚琴
    #95: 800, # 魂魄提灯
    #94: 1000, # 阿尔法之眼
    #65: 4000, #彩猴之神
    #112: 1200,
    #84: 1200, # 探索者-Shift
    #130: 800,
    #128: 6000, # 罗盘指针
    #140: 2000, # 云木方舟
    #61: 2000, # ["2-TaiKongShiftZai", "传说奇遇-太空Shift仔"],
    #60: 600, #["2-ShiftZai", "小小键盘-Shift仔"],
    #134: 1900, # 晶石碎块-未鉴定
    #132: 2200,#["7-FeiLiWuTingMuXia", "奇物秘宝-非礼勿听木匣"],
    #129: 1500, #["5-NengYuanDianChi", "X型能源电池"],
    #150: 2000, # 建木

    #55: 1600,
    #126: 2200, #["7-QingTongShiXiang", "奇物秘宝-青铜石像"],
    #154: 5000,#["7-JuNeng", "启源II聚能号"],

    #156: 599, #["7-EnterZai", "小小键盘-Enter仔"],
    #55: 1600, #["1-ShanLingShuLong", "山岭树龙"],
    #130: 1000, # 虫族骸骨
    #74: 3000, # 可乐
    #155: 8000, #奇物秘宝-蓝海幽蝶
    #55: 1400, #["1-ShanLingShuLong", "山岭树龙"],
    #172: 10,
    169: 250,
}

CastingId2Price_2 = {
    #54: 3000, # 开拓者
    #31: 800, # 厚土
    #32: 1000, # 甘霖
    #29: 360, # 栖龙云木
    #33: 1000, # 灰烬
    #30: 2000, # 浮金

    #80: 2000, # 龙凤守宝
    #60: 40, # Shift
    #61: 1000, # 太空Shift
    #46: 400, # 梦幻小龙
    #79:  900, # 龙图腾
    #87:  2000, # 凤图腾
    #71: 360, # 平安果
    #101: 1700, # 凤翊泪
    94: 7500, # 阿尔法之眼
    #100: 950, # 奇物碎片-时间磨盘
    #71: 400, # 平安果
    # 99: 2000, # 奇物秘宝-时间磨盘
    #84: 800, # 探索者-Shift
    #61: 2000, # ["2-TaiKongShiftZai", "传说奇遇-太空Shift仔"],

    #104: 500, #["5-TongXingZheng", "电子通行证"],
    #105: 1050, #["5-BuLaoQuan", "充盈不老泉"],
    #106: 400, #["5-ShiZhiSha", "一抨时之砂"],
    #111: 5000, # 拾荒者
    #72: 1000, # 抚琴
    #95: 800, # 魂魄提灯
    #65: 4000, #彩猴之神
    #112: 1200,
    #111: 6000, # 拾荒者
    #84: 550,
    #130: 800,
    #129: 1000,
    #128: 4000, #罗盘指针
    ## 140: 2000, # 云木方舟
    #148: 3000, # 合金
    #101: 1000, # 凤翊泪
    #151: 3500, #琉璃
    #126: 2000, #["7-QingTongShiXiang", "奇物秘宝-青铜石像"],
    #154: 5000,#["7-JuNeng", "启源II聚能号"],
    #156: 700, #["7-EnterZai", "小小键盘-Enter仔"],
    #130: 1500, #["5-ChongZuHaiGu", "虫族骸骨"],
    #153: 1000,
    #72: 2500, # 福琴
    #73: 3000, # 缘结
    #83: 1200, #["5-TanSuoZhe-Ctrl", "探索者-Ctrl"],
    #155: 8000, #奇物秘宝-蓝海幽蝶
    #74: 3000, # 可乐
    #169: 270,
    #172: 20,
}

CastingId2Price_3 = {
    #83: 150, # 探索者-Ctrl
    #84: 100, # 探索者-Shift
    #32: 500, # 甘霖
    87:  1500, # 凤图腾
}

CastingId2Price_4 = {
    #83: 150, # 探索者-Ctrl
    #84: 100, # 探索者-Shift
    #32: 500, # 甘霖
    87:  1500, # 凤图腾
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
                [pinfo["id"], pinfo["viewSort"], float(pinfo["resalePrice"]), pinfo["transactionStatus"]])
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
                print("下单失败: {} casting_id={},prod_id={},detail_id={},user_id={},msg={}".format(
                    datetime.now(), casting_id, prod_id, detail_id, user_id, res["msg"]))
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
        token = commoninfo.Home_Token
    elif dict_id == 2:
        castingid2price = CastingId2Price_2
        token = commoninfo.Home_Token
    elif dict_id == 3:
        castingid2price = CastingId2Price_3
        token = commoninfo.Home_Token
    elif dict_id == 4:
        castingid2price = CastingId2Price_4
        token = commoninfo.Home_Token
    if not castingid2price:
        print("dict_id={} 没有对应信息!".format(dict_id))
        sys.exit(1)
    for casting_id in castingid2price:
        print("{}:{}".format(commoninfo.CastingId2MetaInfo[casting_id][1], castingid2price[casting_id]))

    with open("mailconfig") as config_file:
        items = config_file.readline().strip().split(",")
        from_addr = items[0]
        password = items[1]
        to_addr = items[2]
    
    loop_cnt = 0
    wx_msg_count = 0
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
                    trans_status = saling_prod[TRANS_STATUS_INDEX]
                    #if trans_status != TRAN_STATUS_SALING:
                    #    continue
                    if price <= castingid2price[casting_id]:
                        (detail_id, user_id) = get_product_detail_id(prod_id)
                        if not detail_id:
                            print("获取detail_id失败, prod_id={}".format(prod_id))
                            continue
                        prod_name = commoninfo.CastingId2MetaInfo[casting_id][1]
                        if buy_product(casting_id, prod_id, detail_id, user_id, token):
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
                time.sleep(1)
                #time.sleep(random.random())
                    
            loop_cnt += 1
            #print(loop_cnt)
            if loop_cnt % 100 == 0:
                print("{} {} rounds.".format(datetime.now(), loop_cnt))

            # 判断时间是否超过0点
            cur_time = datetime.now()
            #if cur_time.hour == 0 :
            #    break
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(3)
    