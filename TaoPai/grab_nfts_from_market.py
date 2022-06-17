# coding: utf-8

from selenium import webdriver
from datetime import datetime
import sys
import time
import random
from datetime import datetime

from tpcommon import utils

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=1&k={}&pid={}&vid={}"
PRODUCT_URL = "https://nft.taopainft.com/trade/detail?pid={}&type=bb86903952ad5df5f5016c8d3d4d895ae892ee89"

TOTALPAGE_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.h-13.flex.items-center.justify-end.mb-3 > div:nth-child(2) > ul > li:nth-child(6)"
NFTLIST_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.content > div > div"
BUY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > button"

#CONFIRM_SELECTOR = "#__next > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div.flex.items-center.mt-2.mb-2.undefined > div"
#PAY_SELECTOR = "#__next > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div:nth-child(2) > button"
CONFIRM_SELECTOR =  "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div.flex.mt-2.mb-2.undefined > div.relative.w-3.h-3.flex-shrink-0.mt-px"
PAY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div:nth-child(3) > button"

def buy_nft_from_page(driver, product_id, price, keywords):
    driver.get(PRODUCT_URL.format(product_id))
    
    # 等待加载，否则取不到内容
    time.sleep(1)
    
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
        #time.sleep(1) # 后面有发送微信消息，耗时，无需等待

        msg = "{} {}:{}:{}".format(datetime.now(), desp, keywords, price)
        print(msg)
        utils.send_msg(msg)
        #utils.send_wx_msg(msg)
    else:
        msg = "{} {}:{}:{}".format(datetime.now(), desp, keywords, price)        
        print(msg)
        #utils.send_msg(msg)
        utils.send_wx_msg(msg)

def get_id_from_href(href_value):
    key = "pid="
    start_pos = href_value.find(key)
    if start_pos != -1:
        end_pos = href_value.find("&", start_pos+3)
        if end_pos != -1:
            return int(href_value[start_pos+len(key):end_pos])

Target_Dict_1 = {
    # 淘派官方
    "乐淘淘": (2,3,240), # 乐淘淘
    "": (2,5,600), # 光符
    "内测": (2,1,3000),
    "公测": (2,2,3000),
    "早鸟勋章": (2,0,50),
    "钻石": (2,4,10000),
    "精英": (2,0,1000),
    "大师": (2,0,5000),

    # 烤仔潮物
    #"清明": (7,9,300),
    #"复活": (7,9,300),

    # 凹凸世界
    #"SR-": (34,0,5.0),
    #"SSR-": (34,0,10.0),
    #"UR": (34,0,30.0),
    #"XR": (34,0,90.0),

    # 百变熊熊
    "N-百变熊熊":(42,110,65),
    "R-百变熊熊":(42,111,130),
    "SR-百变熊熊":(42,112,1000),

    # 潮虎
    #"稀有": (37,27,80.0),
    #"史诗": (37,28,300.0),
    #"传说": (37,26,500.0),

    # 华策
    #"徽章海报":(26,0,300),

    # UXON
    #"重启柜子": (0,0,100.0),
    "龙舟":(35,0,200),
    "粽子":(35,0,85),
}

Cookie_Dict_1 = {
# 173****6961
    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTU3NzUyMTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.5xoBKU1YsDWBPMd3PQG4ba8T0onhMDFWnAHw4Gns7MU',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTMxODM4MTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.OCTI4aGEIVZFTCZEA8OWnwZNR65UAi2EwlmxcoNllj4',
    'cert': '1',
}

Target_Dict_2 = {
    # 敦煌菩萨
    #"美女菩萨": (15,22,10.0),
    #"美女菩萨-紫": (15,96,50.0),
    "美女菩萨-金": (15,96,100.0),
    "彩虹": (15,21,300.0),
    "满金": (15,20,1000.0),

    # 敦煌乐舞
    #"乐舞伎楽图": (39,78,300),
    #"反弹琵琶": (39,74,50),

    # 佛系惠二
    #"大圆满": (32,32,600),

    # UXON
    #"重启柜子": (0,0,100.0),
    "憨勇小子":(35,0,85),
    "勤劳大叔":(35,0,50),
    "尖嘴汉":(35,0,65),
    "聪明小子":(35,0,85),
    "龙舟":(35,0,200),
    "粽子":(35,0,85),

    # 烤仔的朋友
    "烤仔的朋友": (2,6,200),
    "金色款": (2,7,500),
    "十二生肖款": (2,8,10000),

    # 中国航天
    #"中国航天日金色版": (0,0,500),
    #"中国航天日绿色版": (40,70,100),
    #"祝融周岁纪念紫色版": (40,70,150),

    # 淘派官方
    "": (2,5,600), # 光符
    "公测": (2,2,3000),
}

Cookie_Dict_2 = {
# 159****9963
    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTY1MDAwMTgsImlhdCI6MTY1MzkwODAxOCwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDM5fX0.RgDjKMu7Fjw4ze32PyHJ7eHVJfmMZvrLcONgPDlre_8',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTM5MDg2MTgsImlhdCI6MTY1MzkwODAxOCwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDM5fX0.ZT_NiHWRhA23SIzWFFSS0ylwPAciP9y9bdpA-9SpsHs',
    'cert': '1',
}

INTERVAL_BETWEEN_PAGES = 0.2 # (s)
PAUSE_TIME = 120 # (s)

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

    # 避免重复登录，循环500次
    for _ in range(500):
        # 只扫描第一页
        first_page_prod_cnt = 0
        for (keywords, (pid,vid,min_price)) in target_dict.items():
            cur_plist = []
            driver.get(SCAN_URL.format(1, keywords, pid, vid))
            products = driver.find_elements_by_css_selector(NFTLIST_SELECTOR)
            for product in products:
                if len(product.text.strip()) == 0:
                    continue
                price_text = product.find_element_by_tag_name("p").text.strip()
                if len(price_text) == 0:
                    continue
                is_paying = False
                if product.text.strip().find("支付中") != -1:
                    if_paying = True
                first_page_prod_cnt += 1
                price = float(price_text[1:])
                p_link = product.find_element_by_tag_name("a")
                href_value = p_link.get_attribute("href").strip()
                product_id = get_id_from_href(href_value)
                cur_plist.append((product_id, price, keywords, is_paying))
            
            # 支付
            for (product_id, price, keywords, is_paying) in cur_plist:
                if price <= min_price:
                    if not is_paying:
                        buy_nft_from_page(driver, product_id, price, keywords)
                    else:
                        msg = "{} {}:{}:{}".format(datetime.now(), "支付中", keywords, price)        
                        print(msg)
                        utils.send_wx_msg(msg)

            # 避免访问次数过于频繁而重登录
            #time.sleep(INTERVAL_BETWEEN_PAGES)
        
        # 判断时间是否超过交易时间
        cur_time = datetime.now()
        if cur_time.hour == 0:
            break

        if first_page_prod_cnt == 0:
            # 可能由于访问过于频繁而封禁
            print("{} 可能由于访问过于频繁而封禁，暂停{}秒钟...".format(datetime.now(), PAUSE_TIME))
            time.sleep(PAUSE_TIME)
            break

    driver.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <target_dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    select_id = int(sys.argv[1])
    if select_id == 0:
        target_dict = Target_Dict_1.copy()
        target_dict.update(Target_Dict_2)
        cookie_dict = Cookie_Dict_1
    elif select_id == 1:
        target_dict = Target_Dict_1
        cookie_dict = Cookie_Dict_1
    elif select_id == 2:
        target_dict = Target_Dict_2
        cookie_dict = Cookie_Dict_1

    while True:
        try:
            grab_nft_from_market(target_dict, cookie_dict)
        except Exception as e:
            print(e)

        # 判断时间是否超过交易时间
        cur_time = datetime.now()
        if cur_time.hour == 0:
            break

        # 等待0-3s的随机时间
        time.sleep(random.random()*3)