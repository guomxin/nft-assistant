# coding: utf-8

from selenium import webdriver
from datetime import datetime
import time
import requests
import json
import sys

from tpcommon import contract
from tpcommon import utils

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=3&k={}&pid={}&vid={}"
GET_PRODUCT_DETAIL_URL = "https://nft.taopainft.com/v1/market/product/detail"

def get_product_detail(product_id, access_token):
    for _ in range(10):
        try:
            data = {
                "productId": product_id,
            }
            headers = {
                "authorization": "Bearer " + access_token,
            }
            res = requests.post(GET_PRODUCT_DETAIL_URL, data=json.dumps(data), headers=headers).json()
            if res["code"] != 0:
                return (res["code"], None)
            else:
                return (res["code"], {
                    "status": res["data"]["status"],
                    "payStatus": res["data"]["payStatus"],
                    "publishTime": res["data"]["publishTime"],
                    "tokenId": res["data"]["tokenId"],
                })
        except Exception as e:
            time.sleep(0.5)
            print(e)

    return (1, None)

INTERVAL_BETWEEN_PAGES = 0.2 # (s)
GET_PRODUCT_URL = "https://nft.taopainft.com/v1/market/v2/product/list"
TOP_COUNT = 500

def get_access_token(driver, select_id, cookie_dict):
    try:
        driver.get(SCAN_URL.format(1, "", 0, 0))
        access_token = driver.get_cookie("accessToken")["value"]
        refresh_token = driver.get_cookie("refreshToken")["value"]
        if access_token != cookie_dict["accessToken"]:
            cookie_dict["accessToken"] = access_token
            cookie_dict["refreshToken"] = refresh_token
            utils.dump_cookie_dict(select_id, cookie_dict)
        return access_token
    except Exception as e:
        driver.close()
        raise e

def get_newest_product_list(keywords, cnt, access_token):
    for _ in range(10):
        try:
            data = {
                "marketType": 1,
                "offset": 0,
                "limit": TOP_COUNT,
                "types": "all",
                "publisherId": 0,
                "name": keywords,
                "sortType": 1,
                "virtualCategory": 0 
            }
            headers = {
                "authorization": "Bearer " + access_token,
            }
            res = requests.post(GET_PRODUCT_URL, data=json.dumps(data), headers=headers).json()
            if res["code"] != 0:
                return (res["code"], None)
            else:
                return (res["code"], res["data"]["list"])
        except Exception as e:
            time.sleep(0.5)
            print(e)
            #return (1, None, None)
            #driver.close()
            #raise e
    return (1, None)

def grab_newest_nft_from_market(cookie_dict, keywords, contract_address):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, "", 0, 0))
    driver.add_cookie({'name':'refreshToken', 'value':cookie_dict['refreshToken'], 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':cookie_dict['accessToken'], 'path':'/'})

    ##### 调试设置cookie后的用户信息
    #driver.get(SCAN_URL.format(1, "", 0, 0))
    #time.sleep(100) 

    access_token = get_access_token(driver, select_id, cookie_dict)
    
    ## 获取藏品市场信息
    (res_code, res) = get_newest_product_list(keywords, TOP_COUNT, access_token)
    if res_code != 0:
        # access_token可能已过期，重新获得
        print("{} accessToken可能已过期,重新获取...".format(datetime.now()))
        access_token = get_access_token(driver, select_id, cookie_dict)
        (res_code, res) = get_newest_product_list(driver, TOP_COUNT, access_token)
        if res_code != 0:
            print("{} 重取accessToken后依然获取藏品列表失败!".format(datetime.now()))
            sys.exit(1)

    prod_cnt = 0
    for product in res:
        price = float(product["price"][1:])
        product_id = product["productId"]
        prod_cnt += 1
        (res_code, res) = get_product_detail(product_id, access_token)
        if (res_code == 0): 
            #print(res)
            token_id = int(res["tokenId"])
            token_name = contract.get_token_name(contract_address, token_id)
            #if token_name.find("金蛋") != -1 or token_name.find("星际蛋") != -1:
            if token_name.find("星际蛋") != -1:
                print("{}:{}:{}".format(token_id, token_name, price))
            print(token_id, token_name)

    print("{} products.".format(prod_cnt))
    driver.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <target_dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    select_id = int(sys.argv[1])
    cookie_dict = utils.load_cookie_dict(select_id)
    
    keywords = "金蛋"
    contract_address = contract.PartyCat_Contract_Address
    grab_newest_nft_from_market(cookie_dict, keywords, contract_address)