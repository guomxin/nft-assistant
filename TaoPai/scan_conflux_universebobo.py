# coding: utf-8
# ContractName: ZGHT 

from selenium import webdriver
from datetime import datetime
import sys

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aachugufke20aym8exsrhr5gkaxr49ae98a0nncyyy0&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

UniverseBoBoIdRange2Name = {
    (1,500): '地球证件照',
    (501,1700): '海王星证件照',
    (1701,2900): '水星证件照',
    (2901,4100): '月球证件照',
    (4101,5000): '黑洞证件照'
}

def return_fig_count(name):
    if name == "地球证件照":
        return 500
    elif name == "海王星证件照":
        return 1200
    elif name == "水星证件照":
        return 1200
    elif name == "月球证件照":
        return 1200
    elif name == "黑洞证件照":
        return 900

NEGLECT_COUNT = 7200

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in UniverseBoBoIdRange2Name.items():
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
                for (range, name) in UniverseBoBoIdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
        
    # dump file
    result_file = open("data/_scan_conflux_universebobo_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()