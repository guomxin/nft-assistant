# coding: utf-8
# Contract Name: TaopaiNFT

from selenium import webdriver
from datetime import datetime
import sys

from tpcommon import idrange
from tpcommon import utils

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aachew68x34cwu04aezbunyaz67gppakvmyn79tau56&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"

def return_fig_count(name):
    if name == "十二生肖款":
        return 12
    elif name == "金色款":
        return 360
    elif name == "普通款":
        return 9628

NEGLECT_COUNT = 0
MIN_TOKEN_ID = 100001

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in idrange.KaoZaiFriends_IdRange2Name.items():
        fig_cnt_dict[name] = 0
    reach_min_id = False
    for skip_count in range(0, contract_item_count-NEGLECT_COUNT, 50):
        driver.get(SCAN_URL.format(skip_count+NEGLECT_COUNT))
        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        if len(nfts) == 0:
            print("Could not find items in {}.".format(SCAN_URL.format(skip_count)))
        for nft in nfts:
            nft_text = nft.text
            token_id = utils.get_tokenid_from_html_text(nft_text)
            if token_id < MIN_TOKEN_ID:
                reach_min_id = True
                break
            if token_id != None:
                for (range, name) in idrange.KaoZaiFriends_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find tokenid in {}.", nft_text)
        if reach_min_id:
            break
    
    # dump file
    result_file = open("data/_scan_conflux_kaozaifriends_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()