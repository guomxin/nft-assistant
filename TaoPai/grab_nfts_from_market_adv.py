# coding: utf-8

from selenium import webdriver
from datetime import date, datetime
import sys
import time
import random
import requests
import json

from tpcommon import utils
from tpcommon import market

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=1&k={}&pid={}&vid={}"
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
        time.sleep(1)
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

        msg = "{} {}:{}:{}".format(datetime.now(), desp, keywords, price)
        print(msg)
        utils.send_msg(msg)
        #utils.send_wx_msg(msg)
    else:
        msg = "{} {}:{}:{}".format(datetime.now(), desp, keywords, price)        
        print(msg)
        #utils.send_wx_msg(msg)

INTERVAL_BETWEEN_PAGES = 0.2 # (s)
GET_PRODUCT_URL = "https://nft.taopainft.com/v1/market/v2/product/list"

def get_access_token(driver):
    driver.get(SCAN_URL.format(1, "", 0, 0))
    return driver.get_cookie("accessToken")['value']

def get_product_list(driver, keywords, pid, vid, access_token):
    data = {
        "marketType": 1,
        "offset": 0,
        "limit": 20,
        "types": "all",
        "publisherId": pid,
        "name": keywords,
        "sortType": 1,
        "virtualCategory": vid 
    }
    headers = {
        "authorization": "Bearer " + access_token,
    }
    res = requests.post(GET_PRODUCT_URL, data=json.dumps(data), headers=headers).json()
    if res["code"] != 0:
        return (res["code"], None)
    else:
        return (res["code"], res["data"]["list"])


def grab_nft_from_market(target_dict, cookie_dict):
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
    prod2minprice = {}
    # 循环一定次数后重启浏览器
    for i in range(1000):
        # 只扫描第一页
        for (keywords, (pid,vid,min_price)) in target_dict.items():
            cur_plist = []
            (res_code, res) = get_product_list(driver, keywords, pid, vid, access_token)
            if res_code != 0:
                # access_token可能已过期，重新获得
                print("{} accessToken可能已过期,重新获取...".format(datetime.now()))
                access_token = get_access_token(driver)
                (res_code, res) = get_product_list(driver, keywords, pid, vid, access_token)
            if res_code != 0:
                print("{} 重取accessToken后依然获取藏品列表失败!".format(datetime.now()))
                continue
            for product in res:
                price = float(product["price"][1:])
                is_paying = (product["isPaying"] != 2)
                product_id = product["productId"]
                if keywords in prod2minprice:
                    if price < prod2minprice[keywords]:
                        prod2minprice[keywords] = price
                else:
                    prod2minprice[keywords] = price
                cur_plist.append((product_id, price, keywords, is_paying))
            
            # 支付
            for (product_id, price, keywords, is_paying) in cur_plist:
                if price <= min_price:
                    if not is_paying:
                        buy_nft_from_page(driver, product_id, price, keywords)
                    else:
                        msg = "{} {}:{}:{}".format(datetime.now(), "支付中", keywords, price)        
                        print(msg)
                        #utils.send_wx_msg(msg)
            
            # 避免访问次数过于频繁
            # time.sleep(INTERVAL_BETWEEN_PAGES)
        if (i+1) % 100 == 0:
            print("{} rounds.".format(i+1))
            msg = "{}:{}".format(datetime.now(), prod2minprice)
            print(msg)
            if (i+1) % 1000 == 0:
                utils.send_msg(msg)
            prod2minprice = {}

        # 判断时间是否超过交易时间
        cur_time = datetime.now()
        if cur_time.hour == 0 and cur_time.minute >= 10:
            break

    driver.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <target_dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    select_id = int(sys.argv[1])
    if select_id == 0:
        target_dict = market.Target_Dict_1.copy()
        target_dict.update(market.Target_Dict_2)
        cookie_dict = market.Cookie_Dict_1
    elif select_id == 1:
        target_dict = market.Target_Dict_1
        cookie_dict = market.Cookie_Dict_1
    elif select_id == 2:
        target_dict = market.Target_Dict_2
        cookie_dict = market.Cookie_Dict_1

    while True:
        try:
            grab_nft_from_market(target_dict, cookie_dict)
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(5)

        # 判断时间是否超过交易时间
        cur_time = datetime.now()
        if cur_time.hour == 0 and cur_time.minute >= 10:
            break

        # 等待0-3s的随机时间
        #time.sleep(random.random()*3)