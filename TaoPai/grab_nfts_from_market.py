# coding: utf-8

from selenium import webdriver
from datetime import datetime
import sys
import time
import random

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=1&k={}&pid=0&vid=0"
PRODUCT_URL = "https://nft.taopainft.com/trade/detail?pid={}&type=bb86903952ad5df5f5016c8d3d4d895ae892ee89"

TOTALPAGE_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.h-13.flex.items-center.justify-end.mb-3 > div:nth-child(2) > ul > li:nth-child(6)"
NFTLIST_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.content > div > div"
BUY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > button"

#CONFIRM_SELECTOR = "#__next > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div.flex.items-center.mt-2.mb-2.undefined > div"
#PAY_SELECTOR = "#__next > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div:nth-child(2) > button"
CONFIRM_SELECTOR =  "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div.flex.mt-2.mb-2.undefined > div.relative.w-3.h-3.flex-shrink-0.mt-px"
PAY_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div:nth-child(3) > div.transition-bottom.duration-500.ease-linear.fixed.w-full.overflow-scroll.top-0.bottom-0.-inset-x-0.z-50.text-white.text-left.box-border.flex.flex-col.justify-center.items-center.px-6.bg-modelAlphaBg.backdrop-filter.backdrop-blur > div > div.text-sm.px-4 > footer > div:nth-child(2) > button"

def buy_nft_from_page(driver, product_id, price):
    driver.get(PRODUCT_URL.format(product_id))
    
    # 等待加载，否则取不到内容
    time.sleep(1)
    
    buy_btn = driver.find_element_by_css_selector(BUY_SELECTOR)
    desp = buy_btn.text.strip()
    if (desp == "购买"):
        print("{}:{}:{}".format(product_id, price, desp))
        buy_btn.click()
        time.sleep(0.5)
        # 点击仔细阅读并同意框
        confrim_btn = driver.find_element_by_css_selector(CONFIRM_SELECTOR)
        confrim_btn.click()
        time.sleep(0.5)
        # 点击立即支付按钮
        pay_btn = driver.find_element_by_css_selector(PAY_SELECTOR)
        pay_btn.click()
        time.sleep(1)
    else:
        print("{}:{}:{}".format(product_id, price, desp))

def get_id_from_href(href_value):
    key = "pid="
    start_pos = href_value.find(key)
    if start_pos != -1:
        end_pos = href_value.find("&", start_pos+3)
        if end_pos != -1:
            return int(href_value[start_pos+len(key):end_pos])

Target_Dict_1 = {
    "SR-": 5.0,
    "SSR-": 15.0,
    "UR": 30.0,
    "XR": 100.0,

    "稀有": 150.0,
    "史诗": 300.0,
    "传说": 500.0
}

Target_Dict_2 = {
    "美女菩萨": 10.0,
    "美女菩萨-紫": 30.0,
    "美女菩萨-金": 200.0,
    "彩虹": 500.0,
    "满金": 1000.0,

    "重启柜子": 100.0,
}

def grab_nft_from_market(keywords, min_price):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, keywords))
    driver.add_cookie({'name':'refreshToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTU3NzUyMTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.5xoBKU1YsDWBPMd3PQG4ba8T0onhMDFWnAHw4Gns7MU', 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTMxODM4MTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.OCTI4aGEIVZFTCZEA8OWnwZNR65UAi2EwlmxcoNllj4', 'path':'/'})
    driver.add_cookie({'name':'cert', 'value':'1', 'path':'/'})

    # 获取页面数
    """
    driver.get(SCAN_URL.format(1, keywords))
    page_cnt_ele = driver.find_element_by_css_selector(TOTALPAGE_SELECTOR)
    page_cnt_text = page_cnt_ele.text.strip()
    if len(page_cnt_text) != 0:
        page_cnt = int(page_cnt_ele.text.strip())
    else:
        page_cnt = None
    print("Total page count:{}.".format(page_cnt))
    """

    # 只扫描第一页
    for p in range(1):
        cur_plist = []
        driver.get(SCAN_URL.format(p+1, keywords))
        products = driver.find_elements_by_css_selector(NFTLIST_SELECTOR)
        for product in products:
            if len(product.text.strip()) == 0:
                continue
            price_text = product.find_element_by_tag_name("p").text.strip()
            if len(price_text) == 0:
                continue
            price = float(price_text[1:])
            p_link = product.find_element_by_tag_name("a")
            href_value = p_link.get_attribute("href").strip()
            product_id = get_id_from_href(href_value)
            cur_plist.append((product_id, price))
        
        # 支付
        for (product_id, price) in cur_plist:
            if price <= min_price:
                buy_nft_from_page(driver, product_id, price)
    
    driver.close()

def grab_nft_from_market(target_dict):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, ""))
    driver.add_cookie({'name':'refreshToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTU3NzUyMTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.5xoBKU1YsDWBPMd3PQG4ba8T0onhMDFWnAHw4Gns7MU', 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTMxODM4MTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.OCTI4aGEIVZFTCZEA8OWnwZNR65UAi2EwlmxcoNllj4', 'path':'/'})
    driver.add_cookie({'name':'cert', 'value':'1', 'path':'/'})

    # 只扫描第一页
    for (keywords, min_price) in target_dict.items():
        cur_plist = []
        driver.get(SCAN_URL.format(1, keywords))
        products = driver.find_elements_by_css_selector(NFTLIST_SELECTOR)
        for product in products:
            if len(product.text.strip()) == 0:
                continue
            price_text = product.find_element_by_tag_name("p").text.strip()
            if len(price_text) == 0:
                continue
            price = float(price_text[1:])
            p_link = product.find_element_by_tag_name("a")
            href_value = p_link.get_attribute("href").strip()
            product_id = get_id_from_href(href_value)
            cur_plist.append((product_id, price))
        
        # 支付
        for (product_id, price) in cur_plist:
            if price <= min_price:
                buy_nft_from_page(driver, product_id, price)
    
    driver.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <target_dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    select_id = int(sys.argv[1])
    if select_id == 1:
        target_dict = Target_Dict_1
    elif select_id == 2:
        target_dict = Target_Dict_2

    while True:
        grab_nft_from_market(target_dict)

        # 判断时间是否超过交易时间
        cur_time = datetime.now()
        if (cur_time.hour >= 15) and (cur_time.minute >= 1):
            break

        # 等待0-5s的随机时间
        time.sleep(random.random()*5)