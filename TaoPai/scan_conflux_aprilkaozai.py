# coding: utf-8
# Contract Name: ConFashion

from selenium import webdriver
from datetime import datetime
import sys

from tpcommon import idrange

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacejnvw0k2zjew74uv570fbrgp2ns541wenhxnjkkv&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

def return_fig_count(name):
    if name == "复活节":
        return 47
    elif name == "清明时节":
        return 44
    elif name == "愚你同乐":
        return 2353
    elif name == "大白烤仔":
        return 2022

NEGLECT_COUNT = 0
MIN_TOKEN_ID = 80001

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in idrange.AprilKZIdRange2Name.items():
        fig_cnt_dict[name] = 0
    reach_min_id = False
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
                if token_id < MIN_TOKEN_ID:
                    reach_min_id = True
                    break
                for (range, name) in idrange.AprilKZIdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
        if reach_min_id:
            break
    # dump file
    result_file = open("data/_scan_conflux_aprilkaozai_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()