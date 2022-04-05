# coding: utf-8
# ContractName: LT

from selenium import webdriver
from datetime import datetime
import sys

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacaha2pz5j1g6b0fbv9xazv5umm587xucjcdu83b02&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

LT_IdRange2Name = {
    (8382,8680): '19 野餐',
    (8083,8381): '18 未来',
    (7784,8082): '17 梦想',
    (7485,7783): '16 春天',
    (7186,7484): '15 我爱吃水果',
    (6887,7185): '14 亲爱的一家人',
    (6588,6886): '13 星空中的我们',
    (6289,6587): '12 呐喊',
    (5990,6288): '11 海蛞蝓',
    (5691,5989): '10 人与自然2',
    (5392,5690): '9 花开',
    (5093,5391): '8 日出',
    (4794,5092): '7 梦想起航机',
    (4495,4793): '6 宇航员登月球',
    (4196,4494): '5 和蓝天做游戏',
    (3897,4195): '4 丸子公主',
    (3598,3896): '3 布老虎',
    (3299,3597): '2 小陆宇宙探险之回归地球',
    (3000,3298): '1 虎年大吉'
}

def return_fig_count(name):
    return 299

NEGLECT_COUNT = 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in LT_IdRange2Name.items():
        fig_cnt_dict[name] = 0
    for skip_count in range(0, contract_item_count-NEGLECT_COUNT, 50):
        driver.get(SCAN_URL.format(skip_count+NEGLECT_COUNT))

        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        if len(nfts) == 0:
            print("Could not find items in {}.".format(SCAN_URL.format(skip_count)))
        for nft in nfts:
            nft_text = nft.text
            flag_pos = nft_text.find(FLAG)
            if flag_pos != -1:
                token_id = int(nft_text[flag_pos+len(FLAG):].strip())
                for (range, name) in LT_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    # dump file
    result_file = open("_scan_conflux_lt0402_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()