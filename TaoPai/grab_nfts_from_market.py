# coding: utf-8

from selenium import webdriver
from datetime import datetime
import sys
import time
import random
from datetime import datetime

from tpcommon import utils
from tpcommon import market

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
    
    # ????????????????????????????????????
    time.sleep(1)
    
    buy_btn = driver.find_element_by_css_selector(BUY_SELECTOR)
    desp = buy_btn.text.strip()
    if (desp == "??????"):
        buy_btn.click()
        time.sleep(1)
        # ??????????????????????????????
        confrim_btn = driver.find_element_by_css_selector(CONFIRM_SELECTOR)
        confrim_btn.click()
        #time.sleep(0.5) # ?????????????????????????????????
        # ????????????????????????
        pay_btn = driver.find_element_by_css_selector(PAY_SELECTOR)
        pay_btn.click()
        #time.sleep(1) # ???????????????????????????????????????????????????

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

INTERVAL_BETWEEN_PAGES = 0.2 # (s)
PAUSE_TIME = 120 # (s)

def grab_nft_from_market(target_dict, cookie_dict):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, "", 0, 0))
    driver.add_cookie({'name':'refreshToken', 'value':cookie_dict['refreshToken'], 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':cookie_dict['accessToken'], 'path':'/'})
    driver.add_cookie({'name':'cert', 'value':cookie_dict['cert'], 'path':'/'})

    ##### ????????????cookie??????????????????
    #driver.get(SCAN_URL.format(1, "", 0, 0))
    #time.sleep(100) 

    # ???????????????????????????500???
    for _ in range(500):
        # ??????????????????
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
                if product.text.strip().find("?????????") != -1:
                    is_paying = True
                first_page_prod_cnt += 1
                price = float(price_text[1:])
                p_link = product.find_element_by_tag_name("a")
                href_value = p_link.get_attribute("href").strip()
                product_id = get_id_from_href(href_value)
                cur_plist.append((product_id, price, keywords, is_paying))
            
            # ??????
            for (product_id, price, keywords, is_paying) in cur_plist:
                if price <= min_price:
                    if not is_paying:
                        buy_nft_from_page(driver, product_id, price, keywords)
                    else:
                        msg = "{} {}:{}:{}".format(datetime.now(), "?????????", keywords, price)        
                        print(msg)
                        #utils.send_wx_msg(msg)

            # ??????????????????????????????????????????
            #time.sleep(INTERVAL_BETWEEN_PAGES)
        
        # ????????????????????????????????????
        cur_time = datetime.now()
        if cur_time.hour == 0:
            pass #break

        if first_page_prod_cnt == 0:
            # ???????????????????????????????????????
            print("{} ????????????????????????????????????????????????{}??????...".format(datetime.now(), PAUSE_TIME))
            time.sleep(PAUSE_TIME)
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

        # ????????????????????????????????????
        cur_time = datetime.now()
        if cur_time.hour == 0:
            pass #break

        # ??????0-3s???????????????
        time.sleep(random.random()*3)