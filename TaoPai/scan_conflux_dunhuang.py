# coding: utf-8

from selenium import webdriver
from datetime import datetime

CONTRACT_ITEM_COUNT = 6078
SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacff8dvjv6pys2ws19dhx753h1h00sum6yhu3m188h&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

DH_IdRange2Name = {
    (10001,14500): '红',
    (14501,19000): '橙',
    (19001,23500): '黄',
    (23501,28000): '绿',
    (28001,32500): '蓝',
    (32501,37000): '靛',
    (37001,38000): '金',
    (38001,40000): '紫'
}

def return_fig_count(name):
    gold_cnt = 1000
    purple_cnt = 2000
    other_cnt = 4500

    if name == "金":
        return gold_cnt
    elif name == "紫":
        return purple_cnt
    else:
        return other_cnt

NEGLECT_COUNT = 4750

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in DH_IdRange2Name.items():
        fig_cnt_dict[name] = 0
    for skip_count in range(0, CONTRACT_ITEM_COUNT-NEGLECT_COUNT, 50):
        driver.get(SCAN_URL.format(skip_count+NEGLECT_COUNT))

        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        if len(nfts) == 0:
            print("Could not find items in {}.".format(SCAN_URL.format(skip_count)))
        for nft in nfts:
            nft_text = nft.text
            flag_pos = nft_text.find(FLAG)
            if flag_pos != -1:
                token_id = int(nft_text[flag_pos+len(FLAG):].strip())
                for (range, name) in DH_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    # dump file
    result_file = open("_scan_conflux_dunhuang_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()