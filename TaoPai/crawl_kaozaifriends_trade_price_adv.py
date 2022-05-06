# coding: utf-8

from selenium import webdriver
from datetime import datetime
import sys
import time

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=1&k={}&pid=0&vid=0"
PRODUCT_URL = "https://nft.taopainft.com/trade/detail?pid={}&type=bb86903952ad5df5f5016c8d3d4d895ae892ee89"

TOTALPAGE_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.h-13.flex.items-center.justify-end.mb-3 > div:nth-child(2) > ul > li:nth-child(6)"
NFTLIST_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.content > div > div"
TOKENID_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.mt-6.mb-10 > div.text-2xl.flex.justify-start > p"
CHANGE_VIEW_SELECTOR = "#__next > div.text-white.px-4\.5.scrolling-touch.h-full.min-h-full > div > main > div.flex.h-8.mb-2.items-center.text-sm.-mt-2.relative.z-30 > div.relative.w-8.h-full.flex.items-center.justify-center.bg-c171717.rounded"

def get_tokenid_from_product_page(driver, product_id):
    driver.get(PRODUCT_URL.format(product_id))
    
    # 等待加载，否则取不到内容
    time.sleep(1)
    
    ele = driver.find_element_by_css_selector(TOKENID_SELECTOR)
    desp = ele.text.strip()
    if len(desp) > 0:
        items = desp.split("-")
        if items[0] == "普通款":
            return 100000+int(items[2])
        elif items[0] == "金色款":
            return 200000+int(items[2])
        elif items[0] == "十二生肖款":
            # 十二生肖款，目前还没显示id只显示属相，后续需要映射
            pass

def get_id_from_href(href_value):
    key = "pid="
    start_pos = href_value.find(key)
    if start_pos != -1:
        end_pos = href_value.find("&", start_pos+3)
        if end_pos != -1:
            return int(href_value[start_pos+len(key):end_pos])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <keywords>".format(sys.argv[0]))
        sys.exit(1)
    keywords = sys.argv[1]

    while True:
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)

        # Set cookie
        driver.get(SCAN_URL.format(1, keywords))
        driver.add_cookie({'name':'refreshToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQxNDIzMjQsImlhdCI6MTY1MTU1MDMyNCwidXNlclVJRCI6eyJ1c2VySWQiOjU1MTh9fQ.ogfeGrbHxcHqG2VRkL1smxghyy-Fz6SEf1oTZg2fHBQ', 'path':'/'})
        driver.add_cookie({'name':'accessToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTE1NTA5MjQsImlhdCI6MTY1MTU1MDMyNCwidXNlclVJRCI6eyJ1c2VySWQiOjU1MTh9fQ.laDpmZHZ-D-bxvxfmDTce7WU7hCS9gXB7KDi-FnT9CQ', 'path':'/'})
        driver.add_cookie({'name':'cert', 'value':'1', 'path':'/'})

        # Change view
        driver.get(SCAN_URL.format(1, keywords))
        change_view_ele = driver.find_element_by_css_selector(CHANGE_VIEW_SELECTOR)
        change_view_ele.click()
        time.sleep(1)

        product_dict = {}
        try:
            # 获取页面数
            driver.get(SCAN_URL.format(1, keywords))
            page_cnt_ele = driver.find_element_by_css_selector(TOTALPAGE_SELECTOR)
            page_cnt = int(page_cnt_ele.text.strip())
            print("Total page count:{}.".format(page_cnt))

            # 逐页扫描页面
            for p in range(page_cnt):
                driver.get(SCAN_URL.format(p+1, keywords))
                products = driver.find_elements_by_css_selector(NFTLIST_SELECTOR)
                for product in products:
                    key_ele = product.find_element_by_css_selector("a > div.m-2 > div")
                    items = key_ele.text.strip().split("#")
                    price = float(items[0].strip()[1:])
                    token_id = items[1].strip()
                    if token_id not in product_dict:
                        product_dict[token_id] = []
                    if price not in product_dict[token_id]:
                        product_dict[token_id].append(price)
                time.sleep(1)
                
            print("{} products.".format(len(product_dict)))

            # dump file
            result_file = open("data/_crawl_kaozaifriends_trade_{}.csv".format(
                datetime.strftime(datetime.now(), '%Y%m%d')
            ), "w")
            for (token_id, plist) in product_dict.items():
                result_file.write("{},{}\n".format(
                    token_id,
                    ";".join([str(p) for p in plist])
                ))
            result_file.close()
        except Exception as e:
            print(e)
        driver.close()

        time.sleep(60)
        # 判断时间是否超过交易时间
        cur_time = datetime.now()
        if (cur_time.hour >= 16) and (cur_time.minute >= 1):
            break
