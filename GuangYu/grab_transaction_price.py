# coding: utf-8

import sys
import datetime
import requests
import time
import os

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

DETAIL_BUYER_ID_INDEX = 0
DETAIL_BUYER_INDEX = 1
DETAIL_SELLER_INDEX = 2
DETAIL_SALE_TIME_INDEX = 3
DETAIL_PRICE_INDEX = 4
DETAIL_PROD_ID_INDEX = 5
DETAIL_DETAIL_ID_INDEX = 6
DETAIL_ITEM_COUNT = 7

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
                print(detail_id, user_id, created_time)
                break
        except Exception as e:
            time.sleep(0.5)
            print(e)
    if not detail_id:
        return None
    
    # Get recent 2 transaction data
    data = {
        "detailId": detail_id,
        "page": 1,
        "pageSize": 2,
    }
    while True:
        try: 
            res = requests.post(GET_TRANS_INFO_URL, data=data, timeout=TIME_OUT).json()
            if res["code"] != 0:
                return None
            else:
                trans = res["obj"]["history"]["list"]
                if len(trans) != 2:
                    print("detailId:{} 未获取到足够的交易信息!".format(detail_id))
                    return None
                sell_price = trans[1]["sellPrice"]
                if not sell_price:
                    sell_price = trans[0]["sellPrice"]
                buy_price = trans[0]["buyPrice"]
                if not buy_price:
                    buy_price = trans[1]["buyPrice"]
                if sell_price != buy_price:
                    print("detailId:{} 买入{}和卖出{}价格不匹配".format(detail_id, buy_price, sell_price))
                    return None
                buyer_name = trans[0]["nickName"]
                seller_name = trans[1]["nickName"]
                
                detail_info[DETAIL_BUYER_ID_INDEX] = user_id
                detail_info[DETAIL_BUYER_INDEX] = buyer_name
                detail_info[DETAIL_SELLER_INDEX] = seller_name
                detail_info[DETAIL_SALE_TIME_INDEX] = datetime.datetime.strptime(trans[0]["created"], "%Y-%m-%d %H:%M:%S")
                detail_info[DETAIL_PRICE_INDEX] = float(buy_price)
                detail_info[DETAIL_PROD_ID_INDEX] = prod_id
                detail_info[DETAIL_DETAIL_ID_INDEX] = detail_id
                break
        except Exception as e:
            time.sleep(0.5)
            print(e)
    
    return detail_info

"""
def match_and_dump_trans_info(driver, now_time, in_sale_products, access_token, select_id, cookie_dict):
    date_str = now_time.strftime("%Y%m%d")
    price_result_file_name = "data/_grap_ALL_nft_price_result_{}.csv".format(
        date_str
    )
    contract_time_file_name = "data/_grap_ALL_nft_contratime_{}.csv".format(
        date_str
    )
    contract2starttime = {}
    default_trans_start_time = datetime.datetime.strptime(date_str + " 0:0:0", "%Y%m%d %H:%M:%S")
    if os.path.exists(contract_time_file_name):
        with open(contract_time_file_name, encoding="utf-8-sig") as contract_time_file:
            for line in contract_time_file:
                items = line.strip().split(",")
                # 加1毫秒表示开始，因为文件中记录的是最后一次交易的时间
                contract2starttime[items[0]] = datetime.datetime.strptime(items[1], "%Y/%m/%d %H:%M:%S") + \
                    datetime.timedelta(hours=0, minutes=0, seconds=0, milliseconds=1)
    price_infos = []
    if os.path.exists(price_result_file_name):
        with open(price_result_file_name, encoding="utf-8-sig") as price_result_file:
            # 加载已有的交易信息
            for line in price_result_file:
                pinfo = [None] * TRANS_ITEM_COUNT
                items = line.strip().split(",")
                if len(items) == TRANS_ITEM_COUNT:
                    pinfo[TRANS_NAME_INDEX] = items[0]
                    pinfo[TRANS_TOKENID_INDEX] = items[1]
                    pinfo[TRANS_PRICE_INDEX] = float(items[2])
                    pinfo[TRANS_TIME_INDEX] = items[3]
                    pinfo[TRANS_FROM_INDEX] = items[4]
                    pinfo[TRANS_TO_INDEX] = items[5]
                    pinfo[TRANS_PID_INDEX] = items[6]
                    pinfo[TRANS_CONTRADDR_INDEX] = items[7]
                    pinfo[TRANS_CONTRID_INDEX] = int(items[8])
                elif len(items) == TRANS_ITEM_COUNT - 1:
                    # 兼容未增加tokenid的版本
                    pinfo[TRANS_NAME_INDEX] = items[0]
                    pinfo[TRANS_PRICE_INDEX] = float(items[1])
                    pinfo[TRANS_TIME_INDEX] = items[2]
                    pinfo[TRANS_FROM_INDEX] = items[3]
                    pinfo[TRANS_TO_INDEX] = items[4]
                    pinfo[TRANS_PID_INDEX] = items[5]
                    pinfo[TRANS_CONTRADDR_INDEX] = items[6]
                    pinfo[TRANS_CONTRID_INDEX] = int(items[7])
                price_infos.append(pinfo)
    
    account_tokens = get_account_tokens(trans.Taopai_Conflux_Address)
    provider = HTTPProvider('https://main.confluxrpc.com')
    c =  Conflux(provider)
    priced_prod_cnt = 0
    for (contract_name,contract_address,_) in account_tokens:
        if not contract.is_taopai_contract(contract_address):
            continue
        if contract_address not in contract.ContractAddress2Id:
            # 还未有此contract的统计，暂时忽略
            continue
        cur_contract_id = contract.ContractAddress2Id[contract_address]
        contra = c.contract(contract_address, contract.TaoPai_ABI)
        print("分析合约：{}".format(contract_name))
        
        if contract_address in contract2starttime:
            trans_start_time = contract2starttime[contract_address]
        else:
            trans_start_time = default_trans_start_time
        trans_info = trans.get_current_top10000_trans(contract_address, trans_start_time)
        max_trans_time = None
        for (trans_hash, trans_time_str) in trans_info:
            trans_time = datetime.datetime.strptime(trans_time_str, "%Y/%m/%d %H:%M:%S")
            if (trans_time < trans_start_time):
                continue
            if (max_trans_time == None) or (trans_time > max_trans_time):
                max_trans_time = trans_time
            trans_data = c.cfx.getTransactionByHash(trans_hash)
            (from_addr, to_addr, token_id) = trans.get_transinfo_from_data(trans_data, contra)
            if (from_addr == None) or (to_addr == None):
                # 说明不是transfer交易，忽略
                continue
            if to_addr == trans.Taopai_Conflux_Address:
                # to address 如果是淘派的地址，说明是合成或回收行为，不计入统计
                continue
            if from_addr == trans.Taopai_Conflux_Address:
                # from address 如果是淘派的地址，说明是打开盲盒或者空投，不计入统计
                continue
            
            price_info = [None] * TRANS_ITEM_COUNT
            price_info[TRANS_TIME_INDEX] = trans_time_str
            price_info[TRANS_FROM_INDEX] = from_addr
            price_info[TRANS_TO_INDEX] = to_addr
            price_info[TRANS_CONTRADDR_INDEX] = contract_address
            price_info[TRANS_CONTRID_INDEX] = cur_contract_id
            price_info[TRANS_PRICE_INDEX] = -1
            price_info[TRANS_NAME_INDEX] = clean_token_name(contract.get_token_name(contract_address, token_id))
            price_info[TRANS_TOKENID_INDEX] = "#"+ str(token_id)
            ## 从扫描的网页端支付信息里面匹配
            if cur_contract_id not in in_sale_products:
                price_infos.append(price_info)
                continue
            if token_id not in in_sale_products[cur_contract_id]:
                print("{}:{}:{}".format(cur_contract_id, token_id, "未发现tokenid"))
                price_infos.append(price_info)
                continue
            target_pid = None
            for pid in in_sale_products[cur_contract_id][token_id]:
                sale_time = in_sale_products[cur_contract_id][token_id][pid][SALE_TIME_INDEX]
                if sale_time != None and sale_time > trans_time:
                    continue
                (res_code, res) = get_product_detail(pid, access_token)
                if res_code != 0:
                    # access_token可能已过期，重新获得
                    print("{} accessToken可能已过期,重新获取...".format(datetime.datetime.now()))
                    access_token = get_access_token(driver, select_id, cookie_dict)
                    (res_code, res) = get_product_detail(pid, access_token)
                    if res_code != 0:
                        print("{} accessToken可能已过期,第二次重新获取...".format(datetime.datetime.now()))
                        access_token = get_access_token(driver, select_id, cookie_dict)
                        (res_code, res) = get_product_detail(pid, access_token)
                        if res_code != 0:
                            print("{} 第二次重取accessToken后依然获取藏品列表失败!".format(datetime.datetime.now()))
                            continue
                # 2022/8/12 接口返回的是零时区的时间，链上是GMT+8的时间，需要一致
                sale_time = datetime.datetime.strptime(res["publishTime"], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=8)
                in_sale_products[cur_contract_id][token_id][pid][SALE_TIME_INDEX] = sale_time
                if sale_time > trans_time:
                    continue
                if res["status"] == 3 and res["payStatus"] == 1:
                # status == 2初步推断为下架，看自己下架的藏品payStatus为0，用别的账户看payStatus为1，原因未知
                    target_pid = pid

            if target_pid != None:
                priced_prod_cnt += 1
                target_price = in_sale_products[cur_contract_id][token_id][target_pid][SALE_PRICE_INDEX]
                target_name = in_sale_products[cur_contract_id][token_id][target_pid][SALE_NAME_INDEX]
                price_info[TRANS_NAME_INDEX] = target_name
                price_info[TRANS_PID_INDEX] = target_pid
                price_info[TRANS_PRICE_INDEX] = target_price
                # 删除指定信息
                del in_sale_products[cur_contract_id][token_id][target_pid]
                if len(in_sale_products[cur_contract_id][token_id]) == 0:
                    del in_sale_products[cur_contract_id][token_id]
                if len(in_sale_products[cur_contract_id]) == 0:
                    del in_sale_products[cur_contract_id]
            else:
                print(in_sale_products[cur_contract_id][token_id])
                print("{}:{}:{}".format(cur_contract_id, token_id, "未发现匹配的pid"))
            
            price_infos.append(price_info)
        if max_trans_time != None:
            contract2starttime[contract_address] = max_trans_time
    print("{} new priced products in this round.".format(priced_prod_cnt))
    ## 按价格排序价格信息并输出
    price_infos.sort(key=lambda p: p[TRANS_PRICE_INDEX], reverse=True)
    with open(price_result_file_name, "w+", encoding="utf-8-sig") as price_result_file:
        for pinfo in price_infos:
            price_result_file.write("{}\n".format(
                ",".join([str(i) for i in pinfo ])
            ))
    with open(contract_time_file_name, "w+", encoding="utf-8-sig") as contract_time_file:
        for (caddr,ttime) in contract2starttime.items():
            contract_time_file.write("{},{}\n".format(
                caddr, ttime.strftime("%Y/%m/%d %H:%M:%S")
            ))

def grab_trans_nft_price(casting_id):
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=opt)
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, "", 0, 0))
    driver.add_cookie({'name':'refreshToken', 'value':cookie_dict['refreshToken'], 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':cookie_dict['accessToken'], 'path':'/'})

    access_token = get_access_token(driver, select_id, cookie_dict)
    in_sale_products = {}
    # 一天结束后退出
    day_end_exit = False
    scan_cnt = 0
    while not day_end_exit:
        scan_cnt += 1
        offset = 0
        scan_to_end = False
        paying_prod_cnt = 0
        while not scan_to_end:
            (res_code, res, _) = get_newest_product_list(driver, offset, TOP_COUNT, access_token)
            if res_code != 0:
                # access_token可能已过期，重新获得
                print("{} accessToken可能已过期,重新获取...".format(datetime.datetime.now()))
                access_token = get_access_token(driver, select_id, cookie_dict)
                (res_code, res, _) = get_newest_product_list(driver, offset, TOP_COUNT, access_token)
                if res_code != 0:
                    print("{} 重取accessToken后依然获取藏品列表失败!".format(datetime.datetime.now()))
                    break
            if len(res) == 0:
                scan_to_end = True
            for product in res:
                token_id = product["tokenId"]
                name = product["name"]
                price = float(product["price"][1:])
                is_paying = (product["isPaying"] != 2)
                product_id = product["productId"]
                contract_id = product["contractId"]
                if is_paying:
                    paying_prod_cnt += 1
                if contract_id not in in_sale_products:
                    in_sale_products[contract_id] = {}
                if token_id not in in_sale_products[contract_id]:
                    in_sale_products[contract_id][token_id] = {}
                if product_id not in in_sale_products[contract_id][token_id]:
                    in_sale_products[contract_id][token_id][product_id] = [name, price, None]
                else:
                    pass
            offset += len(res)
        if scan_cnt % 10 == 0:
            print("{} {} products, {} is paying".format(datetime.datetime.now(), offset, paying_prod_cnt))

        # 如果循环满100次，大约30分钟，扫描链上交易
        now_time = datetime.datetime.now()
        if (scan_cnt % 100 != 0) and (now_time.hour != 23 or now_time.minute != 59):
            # 满100次或进入23:59分之后扫描链上
            continue
        if now_time.hour == 23 and now_time.minute == 59:
            # 设置退出循环，重启浏览器标记
            day_end_exit = True
        match_and_dump_trans_info(driver, now_time, in_sale_products, access_token, select_id, cookie_dict)

    driver.close() 
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <casting_id>.".format(sys.argv[0]))
        sys.exit(1)
    casting_id = int(sys.argv[1])

    (res_code, saled_prods) = get_saled_products(casting_id)
    if res_code != 0:
        print("获取在售列表信息失败, res_code={}".format(res_code))
        sys.exit(1)
    for (prod_id, _, _) in saled_prods:
        print(prod_id)
        detail_info = get_product_detail(prod_id)
        print(detail_info)

    """
    while True:
        try:
            grab_nft_price(casting_id)
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(5)
    """

