# coding: utf-8

from selenium import webdriver
from datetime import datetime
import time
import random
import requests
import json
import sys

from tpcommon import utils
from tpcommon import market

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=3&k={}&pid={}&vid={}"
PRODUCT_URL = "https://nft.taopainft.com/trade/detail?pid={}&type=bb86903952ad5df5f5016c8d3d4d895ae892ee89"

BUY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > button"
CONFIRM_SELECTOR =  "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div.flex.mt-2.mb-2.undefined > div.relative.w-3.h-3.flex-shrink-0.mt-px"
PAY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div > button"

def buy_nft_from_page(driver, product_id, price, keywords):
    driver.get(PRODUCT_URL.format(product_id))
    
    # 等待加载，否则取不到内容
    time.sleep(0.5)
    
    buy_btn = driver.find_element_by_css_selector(BUY_SELECTOR)
    desp = buy_btn.text.strip()
    if (desp == "购买"):
        buy_btn.click()
        time.sleep(0.5)
        # 点击仔细阅读并同意框
        confrim_btn = driver.find_element_by_css_selector(CONFIRM_SELECTOR)
        confrim_btn.click()
        #time.sleep(0.5) # 无服务器交互，无需等待
        # 点击立即支付按钮
        pay_btn = driver.find_element_by_css_selector(PAY_SELECTOR)
        pay_btn.click()
        # 回到交易平台页面
        time.sleep(1) 
        driver.get(SCAN_URL.format(1, "", 0, 0))

        msg = "NEW {} {}:{}:{}".format(datetime.now(), desp, keywords, price)
        print(msg)
        utils.send_msg(msg)
        #utils.send_wx_msg(msg)
    else:
        msg = "NEW {} {}:{}:{}".format(datetime.now(), desp, keywords, price)        
        print(msg)
        utils.send_wx_msg(msg)

INTERVAL_BETWEEN_PAGES = 0.2 # (s)
GET_PRODUCT_URL = "https://nft.taopainft.com/v1/market/v2/product/list"
CREATE_ORDER_URL = "https://nft.taopainft.com/v1/market/order/create"
TOP_COUNT = 100

def get_access_token(driver):
    try:
        driver.get(SCAN_URL.format(1, "", 0, 0))
        return driver.get_cookie("accessToken")['value']
    except Exception as e:
        #driver.close()
        raise e

def buy_nft(access_token, product_id, price, keywords, send_wx_msg=False):
    data = {
        "productId": product_id
    }
    headers = {
        "authorization": "Bearer " + access_token,
    }
    res = requests.post(CREATE_ORDER_URL, data=json.dumps(data), headers=headers).json()
    if res["code"] == 0:
        msg = "NEW 购买 {}:{}:{}".format(datetime.now(), keywords, price)
        print(msg)
        utils.send_msg(msg)
    else:
        msg = "NEW 下单失败 {}:{}:{}:{}".format(datetime.now(), keywords, price, res["message"])
        print(msg)
        if send_wx_msg:
            utils.send_wx_msg(msg)

def get_newest_product_list(driver, cnt, access_token):
    try:
        data = {
            "marketType": 1,
            "offset": 0,
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
            return (res["code"], None)
        else:
            return (res["code"], res["data"]["list"])
    except Exception as e:
        driver.close()
        raise e

def is_name_match(name, keyword):
    items = keyword.split("not")
    if len(items) < 2:
        return name.find(keyword) != -1
    else:
        require_word = items[0].strip()
        not_require_word = items[1].strip()
        return name.find(require_word) != -1 and name.find(not_require_word) == -1

def grab_newest_nft_from_market(target_dict, contract_dict, cookie_dict, send_wx_msg=False):
    wx_msg_count = 0
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, "", 0, 0))
    driver.add_cookie({'name':'refreshToken', 'value':cookie_dict['refreshToken'], 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':cookie_dict['accessToken'], 'path':'/'})
    driver.add_cookie({'name':'cert', 'value':cookie_dict['cert'], 'path':'/'})

    ##### 调试设置cookie后的用户信息
    #driver.get(SCAN_URL.format(1, "", 0, 0))
    #time.sleep(100) 

    access_token = get_access_token(driver)
    # 循环一定次数后重启浏览器
    for i in range(10000):
        (res_code, res) = get_newest_product_list(driver, TOP_COUNT, access_token)
        if res_code != 0:
            # access_token可能已过期，重新获得
            print("{} accessToken可能已过期,重新获取...".format(datetime.now()))
            access_token = get_access_token(driver)
            (res_code, res) = get_newest_product_list(driver, TOP_COUNT, access_token)
            if res_code != 0:
                print("{} 重取accessToken后依然获取藏品列表失败!".format(datetime.now()))
                continue
        for product in res:
            name = product["name"]
            price = float(product["price"][1:])
            is_paying = (product["isPaying"] != 2)
            product_id = product["productId"]
            contract_id = product["contractId"]

            for keyword in target_dict:
                min_price = target_dict[keyword]
                if is_name_match(name, keyword) and price <= min_price:
                    if not is_paying:
                        buy_nft(access_token, product_id, price, name, send_wx_msg)
                        #buy_nft_from_page(driver, product_id, price, name)
                    else:
                        wx_msg_count += 1
                        if wx_msg_count == 300:
                            msg = "NEW {} {}:{}:{}".format(datetime.now(), "支付中", name, price)        
                            print(msg)
                            if send_wx_msg:
                                utils.send_wx_msg(msg)
                            wx_msg_count = 0
            
            for cid in contract_dict:
                min_price = contract_dict[cid]
                if contract_id == cid and price <= min_price:
                    if not is_paying:
                        buy_nft(access_token, product_id, price, name, send_wx_msg)
                        #buy_nft_from_page(driver, product_id, price, name)
                    else:
                        wx_msg_count += 1
                        if wx_msg_count == 300:
                            msg = "NEW {} {}:{}:{}".format(datetime.now(), "支付中", name, price)        
                            print(msg)
                            if send_wx_msg:
                                utils.send_wx_msg(msg)
                            wx_msg_count = 0
        
        # 避免访问次数过于频繁
        # time.sleep(INTERVAL_BETWEEN_PAGES)    
    
        if (i+1) % 1000 == 0:
            print("{} {} rounds.".format(datetime.now(), i+1))

        # 判断时间是否超过交易时间
        #cur_time = datetime.now()
        #if cur_time.hour == 0 and cur_time.minute >= 10:
        #    break

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
    target_dict = market.Keywords_Dict
    contract_dict = market.Contract_Dict

    while True:
        try:
            grab_newest_nft_from_market(target_dict, contract_dict, cookie_dict, select_id==1)
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(5)

        # 判断时间是否超过交易时间
        #cur_time = datetime.now()
        #if cur_time.hour == 6 and cur_time.minute >= 10:
        #    break

        # 等待0-3s的随机时间
        #time.sleep(random.random()*3)