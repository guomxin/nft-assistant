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
GET_PRODUCT_DETAIL_URL = "https://nft.taopainft.com/v1/market/product/detail"

BUY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > button"
CONFIRM_SELECTOR =  "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div.flex.mt-2.mb-2.undefined > div.relative.w-3.h-3.flex-shrink-0.mt-px"
PAY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div > button"

# 由于每次从最新发布的50条数据里面分析，有可能过段时间低于阈值的排在50开外；
# 维护一个全局变量记住
target_prods = {} # {keywords: [(product_id, name, price)*]}
# target_prods = {"钻石神像":[("54863892207108096", "钻石神像", 1000)]}

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
                })
        except Exception as e:
            time.sleep(0.5)
            print(e)

    return (1, None)

"""
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

        msg = "{} {}:{}:{}".format(datetime.now(), desp, keywords, price)
        print(msg)
        utils.send_msg(from_addr, password, to_addr, msg)
        #utils.send_wx_msg(msg)
    else:
        msg = "{} {}:{}:{}".format(datetime.now(), desp, keywords, price)        
        print(msg)
        utils.send_wx_msg(msg)
"""

INTERVAL_BETWEEN_PAGES = 0.2 # (s)
GET_PRODUCT_URL = "https://nft.taopainft.com/v1/market/v2/product/list"
CREATE_ORDER_URL = "https://nft.taopainft.com/v1/market/order/create"
TOP_COUNT = 50

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

def buy_nft(access_token, product_id, price, keywords, send_wx_msg=False):
    data = {
        "productId": product_id
    }
    headers = {
        "authorization": "Bearer " + access_token,
    }
    res = requests.post(CREATE_ORDER_URL, data=json.dumps(data), headers=headers).json()
    if res["code"] == 0:
        content = """
淘派: 购买{}
>时间: {}
>价格: {}""".format(keywords, datetime.now(), price)
        print(content)
        utils.send_workwx_msg("markdown", content)
        """
        msg = "购买 {}:{}:{}".format(datetime.now(), keywords, price)
        print(msg)
        utils.send_msg(from_addr, password, to_addr, msg)
        """
    else:
        content = """
淘派: 下单失败{}
>时间: {}
>价格: {}
>原因: {}""".format(keywords, datetime.now(), price, res["message"])
        print(content)
        utils.send_workwx_msg("markdown", content)
        """
        msg = "下单失败 {}:{}:{}:{}".format(datetime.now(), keywords, price, res["message"])
        print(msg)
        if send_wx_msg:
            utils.send_wx_msg(msg)
        """

def get_newest_blindbox_list(driver, cnt, access_token):
    for _ in range(10):
        try:
            data = {
                "marketType": 2,
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
            time.sleep(0.5)
            print(e)
            #return (1, None, None)
            #driver.close()
            #raise e
    return (1, None)

def get_newest_product_list(driver, cnt, access_token):
    for _ in range(10):
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
            time.sleep(0.5)
            print(e)
            #return (1, None, None)
            #driver.close()
            #raise e
    return (1, None)

def is_name_match(name, keyword):
    items = keyword.split("not")
    if len(items) < 2:
        return name.find(keyword) != -1
    else:
        require_word = items[0].strip()
        not_require_words = items[1:]
        require = (name.find(require_word) != -1)
        not_require = True
        for not_require_word in not_require_words:
            not_require_word = not_require_word.strip()
            not_require = (not_require and name.find(not_require_word) == -1)
        return require and not_require

def grab_newest_nft_from_market(target_dict, contract_dict, blindbox_dict, cookie_dict, send_wx_msg=False):
    wx_msg_count = 0
    #options = webdriver.ChromeOptions()
    #options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, "", 0, 0))
    driver.add_cookie({'name':'refreshToken', 'value':cookie_dict['refreshToken'], 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':cookie_dict['accessToken'], 'path':'/'})

    ##### 调试设置cookie后的用户信息
    #driver.get(SCAN_URL.format(1, "", 0, 0))
    #time.sleep(100) 

    access_token = get_access_token(driver, select_id, cookie_dict)
    # 循环一定次数后重启浏览器
    for i in range(10000):
        ## 获取藏品市场信息
        (res_code, res) = get_newest_product_list(driver, TOP_COUNT, access_token)
        if res_code != 0:
            # access_token可能已过期，重新获得
            print("{} accessToken可能已过期,重新获取...".format(datetime.now()))
            access_token = get_access_token(driver, select_id, cookie_dict)
            (res_code, res) = get_newest_product_list(driver, TOP_COUNT, access_token)
            if res_code != 0:
                print("{} 重取accessToken后依然获取藏品列表失败!".format(datetime.now()))
                continue

        match_prod = False
        for product in res:
            name = product["name"]
            price = float(product["price"][1:])
            is_paying = (product["isPaying"] != 2)
            product_id = product["productId"]
            contract_id = product["contractId"]

            for keyword in target_dict:
                min_price = target_dict[keyword]
                if is_name_match(name, keyword) and price <= min_price:
                    match_prod = True
                    if not is_paying:
                        buy_nft(access_token, product_id, price, name, send_wx_msg)
                        #buy_nft_from_page(driver, product_id, price, name)
                    else:
                        wx_msg_count += 1
                        if wx_msg_count == 200:
                            content = """
淘派: 支付中{}
>时间: {}
>价格: {}""".format(name, datetime.now(), price)
                            print(content)
                            utils.send_workwx_msg("markdown", content)
                            """
                            msg = "藏品 {} {}:{}:{}".format(datetime.now(), "支付中", name, price)        
                            print(msg)
                            if send_wx_msg:
                                utils.send_wx_msg(msg)
                            """
                            wx_msg_count = 0
                    if keyword not in target_prods:
                        target_prods[keyword] = []
                    if (product_id, name, price) not in target_prods[keyword]:
                        target_prods[keyword].append((product_id, name, price))
        
        if not match_prod:
            for keyword in target_prods:
                if len(target_prods[keyword]) == 0:
                    continue
                # 按发布时间排序前50以外的
                target_prods[keyword].sort(key=lambda p: p[2])
                for (pid, name, price) in target_prods[keyword]:
                    (res_code, res) = get_product_detail(pid, access_token)
                    if (res_code == 0): 
                        if (res["status"] == 1): # status==1表示未下架或被购买
                            # payStatus==0表示在售，payStatus==1表示已支付
                            # payStatus==7表示他人正在支付, payStatus==2自己正在支付
                            if res["payStatus"] == 0: 
                                buy_nft(access_token, pid, price, name, send_wx_msg)
                            else:
                                wx_msg_count += 1
                                if wx_msg_count == 200:
                                    content = """
淘派: 支付中{}
>时间: {}
>价格: {}""".format(name, datetime.now(), price)
                                    print(content)
                                    utils.send_workwx_msg("markdown", content)
                                    """
                                    msg = "藏品 {} {}:{}:{}".format(datetime.now(), "支付中", name, price)        
                                    print(msg)
                                    if send_wx_msg:
                                        utils.send_wx_msg(msg)
                                    """
                                    wx_msg_count = 0
                        else:
                            target_prods[keyword].remove((pid, name, price))

            for cid in contract_dict:
                min_price = contract_dict[cid]
                if contract_id == cid and price <= min_price:
                    if not is_paying:
                        buy_nft(access_token, product_id, price, name, send_wx_msg)
                        #buy_nft_from_page(driver, product_id, price, name)
                    else:
                        wx_msg_count += 1
                        if wx_msg_count == 200:
                            content = """
淘派: 支付中{}
>时间: {}
>价格: {}""".format(name, datetime.now(), price)
                            print(content)
                            utils.send_workwx_msg("markdown", content)
                            """
                            msg = "藏品 {} {}:{}:{}".format(datetime.now(), "支付中", name, price)        
                            print(msg)
                            if send_wx_msg:
                                utils.send_wx_msg(msg)
                            """
                            wx_msg_count = 0

        ## 获取盲盒市场信息
        '''
        (res_code, res) = get_newest_blindbox_list(driver, TOP_COUNT, access_token)
        if res_code != 0:
            # access_token可能已过期，重新获得
            print("{} accessToken可能已过期,重新获取...".format(datetime.now()))
            access_token = get_access_token(driver, select_id, cookie_dict)
            (res_code, res) = get_newest_blindbox_list(driver, TOP_COUNT, access_token)
            if res_code != 0:
                print("{} 重取accessToken后依然获取盲盒列表失败!".format(datetime.now()))
                continue
        for product in res:
            name = product["name"]
            price = float(product["price"][1:])
            is_paying = (product["isPaying"] != 2)
            product_id = product["productId"]

            for keyword in blindbox_dict:
                min_price = blindbox_dict[keyword]
                if is_name_match(name, keyword) and price <= min_price:
                    if not is_paying:
                        buy_nft(access_token, product_id, price, name, send_wx_msg)
                        #buy_nft_from_page(driver, product_id, price, name)
                    else:
                        wx_msg_count += 1
                        if wx_msg_count == 300:
                            msg = "盲盒 {} {}:{}:{}".format(datetime.now(), "支付中", name, price)        
                            print(msg)
                            if send_wx_msg:
                                utils.send_wx_msg(msg)
                            wx_msg_count = 0
        '''
        
        # 避免访问次数过于频繁
        # time.sleep(INTERVAL_BETWEEN_PAGES)    
    
        if (i+1) % 1000 == 0:
            print("{} {} rounds.(len(target_prods)={})".format(datetime.now(), i+1, len(target_prods)))

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
    cookie_dict = utils.load_cookie_dict(select_id)
    target_dict = market.Keywords_Dict
    contract_dict = market.Contract_Dict
    blindbox_dict = market.BlindBox_Keywords_Dict

    with open("mailconfig") as config_file:
        items = config_file.readline().strip().split(",")
        from_addr = items[0]
        password = items[1]
        to_addr = items[2]

    while True:
        try:
            grab_newest_nft_from_market(target_dict, contract_dict, blindbox_dict, cookie_dict, select_id==1)
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