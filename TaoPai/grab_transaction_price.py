# coding: utf-8

import sys
import datetime
import requests
import time
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from conflux import (
    Conflux,
    HTTPProvider
)

from tpcommon import trans
from tpcommon import contract
from tpcommon import market

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=3&k={}&pid={}&vid={}"
GET_ACCOUNT_TOKEN_URL = "https://api.confluxscan.net/account/tokens?account={}"

def get_account_tokens(account_address):
    tokens_info = [] #(contract_name, contract_address, token_count)
    while True:
        try:
            resp = requests.get(GET_ACCOUNT_TOKEN_URL.format(account_address))
            resp_json = resp.json()
            for token_info in resp_json["data"]["list"]:
                tokens_info.append((
                    token_info["name"],
                    token_info["contract"],
                    token_info["amount"]))
            return tokens_info
        except Exception as e:
            print(e)

def get_access_token(driver):
    try:
        driver.get(SCAN_URL.format(1, "", 0, 0))
        return driver.get_cookie("accessToken")['value']
    except Exception as e:
        driver.close()
        raise e

GET_PRODUCT_URL = "https://nft.taopainft.com/v1/market/v2/product/list"
TOP_COUNT = 100

def get_newest_product_list(driver, offset, cnt, access_token):
    for _ in range(10):
        try:
            data = {
                "marketType": 1,
                "offset": offset,
                "limit": cnt,
                "types": "all",
                "publisherId": 0,
                "name": "",
                "sortType": 3,
                "virtualCategory": 0 
            }
            headers = {
                "authorization": "Bearer " + access_token,
            }
            res = requests.post(GET_PRODUCT_URL, data=json.dumps(data), headers=headers).json()
            if res["code"] != 0:
                return (res["code"], None, None)
            else:
                return (res["code"], res["data"]["list"], res["data"]["total"])
        except Exception as e:
            time.sleep(0.5)
            print(e)
            #return (1, None, None)
            #driver.close()
            #raise e
    return (1, None, None)

PAY_NAME_INDEX = 0
PAY_PRICE_INDEX = 1
PAY_TIME_INDEX = 2

MAX_INTERVAL = 900 # s, 15分钟，上链时间

TRANS_NAME_INDEX = 0
TRANS_TOKENID_INDEX = 1
TRANS_PRICE_INDEX = 2
TRANS_TIME_INDEX = 3
TRANS_FROM_INDEX = 4
TRANS_TO_INDEX = 5
TRANS_PID_INDEX = 6
TRANS_CONTRADDR_INDEX = 7
TRANS_CONTRID_INDEX = 8
TRANS_ITEM_COUNT = 9

def grab_trans_nft_price(cookie_dict):
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=opt)
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, "", 0, 0))
    driver.add_cookie({'name':'refreshToken', 'value':cookie_dict['refreshToken'], 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':cookie_dict['accessToken'], 'path':'/'})
    driver.add_cookie({'name':'cert', 'value':cookie_dict['cert'], 'path':'/'})

    access_token = get_access_token(driver)
    paying_products = {}
    # 循环一定次数后重启浏览器
    for i in range(1600):
        offset = 0
        scan_to_end = False
        paying_prod_cnt = 0
        while not scan_to_end:
            (res_code, res, _) = get_newest_product_list(driver, offset, TOP_COUNT, access_token)
            if res_code != 0:
                # access_token可能已过期，重新获得
                print("{} accessToken可能已过期,重新获取...".format(datetime.datetime.now()))
                access_token = get_access_token(driver)
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
                    if contract_id not in paying_products:
                        paying_products[contract_id] = {}
                    if token_id not in paying_products[contract_id]:
                        paying_products[contract_id][token_id] = {}
                    if product_id not in paying_products[contract_id][token_id]:
                        paying_products[contract_id][token_id][product_id] = [name, price, datetime.datetime.now()]
                    else:
                        paying_products[contract_id][token_id][product_id][PAY_TIME_INDEX] = datetime.datetime.now()
            offset += len(res)
        print("{} {} products, {} is paying".format(datetime.datetime.now(), offset, paying_prod_cnt))

        # 如果循环满50次，大约15分钟，扫描链上交易
        if (i+1) % 50 != 0:
            continue
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        price_result_file_name = "data/_grap_nft_price_result_{}.csv".format(
            date_str
        )
        contract_time_file_name = "data/_grap_nft_contratime_{}.csv".format(
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
                price_info[TRANS_NAME_INDEX] = contract.get_token_name(contract_address, token_id)
                price_info[TRANS_TOKENID_INDEX] = "#"+ str(token_id)
                ## 从扫描的网页端支付信息里面匹配
                if cur_contract_id not in paying_products:
                    price_infos.append(price_info)
                    continue
                if token_id not in paying_products[cur_contract_id]:
                    price_infos.append(price_info)
                    continue
                target_pid = None
                min_interval = None
                for pid in paying_products[cur_contract_id][token_id]:
                    paying_time = paying_products[cur_contract_id][token_id][pid][PAY_TIME_INDEX]
                    if paying_time > trans_time:
                        continue
                    interval = (trans_time - paying_time).seconds
                    if interval >= MAX_INTERVAL:
                        continue
                    if (min_interval == None) or (interval < min_interval):
                        min_interval = interval
                        target_pid = pid
                if target_pid != None:
                    priced_prod_cnt += 1
                    target_price = paying_products[cur_contract_id][token_id][target_pid][PAY_PRICE_INDEX]
                    target_name = paying_products[cur_contract_id][token_id][target_pid][PAY_NAME_INDEX]
                    price_info[TRANS_NAME_INDEX] = target_name
                    price_info[TRANS_PID_INDEX] = target_pid
                    price_info[TRANS_PRICE_INDEX] = target_price
                    # 删除指定信息
                    del paying_products[cur_contract_id][token_id][target_pid]
                    if len(paying_products[cur_contract_id][token_id]) == 0:
                        del paying_products[cur_contract_id][token_id]
                    if len(paying_products[cur_contract_id]) == 0:
                        del paying_products[cur_contract_id]
                
                price_infos.append(price_info)
            if max_trans_time != None:
                contract2starttime[contract_address] = max_trans_time
        print("{} new priced products in this round.".format(priced_prod_cnt))
        print(paying_products)
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
    driver.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <target_dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    select_id = int(sys.argv[1])
    if select_id == 1:
        cookie_dict = market.Cookie_Dict_1
    elif select_id == 2:
        cookie_dict = market.Cookie_Dict_2

    while True:
        try:
            grab_trans_nft_price(cookie_dict)
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(5)

