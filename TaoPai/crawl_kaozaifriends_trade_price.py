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

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, keywords))
    driver.add_cookie({'name':'refreshToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQxNDIzMjQsImlhdCI6MTY1MTU1MDMyNCwidXNlclVJRCI6eyJ1c2VySWQiOjU1MTh9fQ.ogfeGrbHxcHqG2VRkL1smxghyy-Fz6SEf1oTZg2fHBQ', 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTE1NTA5MjQsImlhdCI6MTY1MTU1MDMyNCwidXNlclVJRCI6eyJ1c2VySWQiOjU1MTh9fQ.laDpmZHZ-D-bxvxfmDTce7WU7hCS9gXB7KDi-FnT9CQ', 'path':'/'})
    driver.add_cookie({'name':'cert', 'value':'1', 'path':'/'})

    product_dict = {}
    while True:
        # 获取页面数
        driver.get(SCAN_URL.format(1, keywords))
        page_cnt_ele = driver.find_element_by_css_selector(TOTALPAGE_SELECTOR)
        page_cnt = int(page_cnt_ele.text.strip())
        print("Total page count:{}.".format(page_cnt))

        # 逐页扫描页面
        for p in range(page_cnt):
            cur_plist = []
            driver.get(SCAN_URL.format(p+1, keywords))
            products = driver.find_elements_by_css_selector(NFTLIST_SELECTOR)
            for product in products:
                price_text = product.find_element_by_tag_name("p").text.strip()
                if len(price_text) == 0:
                    continue
                price = float(price_text[1:])
                p_link = product.find_element_by_tag_name("a")
                href_value = p_link.get_attribute("href").strip()
                product_id = get_id_from_href(href_value)
                cur_plist.append((product_id, price))
            
            # 获取价格
            for (product_id, price) in cur_plist:
                token_id = get_tokenid_from_product_page(driver, product_id)
                if not token_id:
                    continue
                if token_id not in product_dict:
                    product_dict[token_id] = []
                if price not in product_dict[token_id]:
                    product_dict[token_id].append(price)
        
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
        time.sleep(30)

        # 判断时间是否超过交易时间
        cur_time = datetime.now()
        if (cur_time.hour >= 15) and (cur_time.minute >= 1):
            break

    driver.close()