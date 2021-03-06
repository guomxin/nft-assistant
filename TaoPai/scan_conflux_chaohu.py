# coding: utf-8
# ContractName: COCAFE

from selenium import webdriver
from datetime import datetime
import sys

from tpcommon import idrange
from tpcommon import utils

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacgjw8bg7gehy3x7x5evfknfe7pst64hp6tgymfwa4&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

def return_fig_count(name):
    if name == "隐藏":
        return 760
    elif name == "传说":
        return 25
    elif name == "史诗":
        return 30
    elif name == "稀有":
        return 225
    elif name == "珍贵":
        return 400
    elif name == "高级":
        return 3735

NEGLECT_COUNT = 0

def get_total_endwith8_count():
    cnt = 8
    for pair in idrange.CH_IdRange2Name.keys():
        start = pair[0]
        end = pair[1] + 1
        for id in range(start, end):
            if str(id)[-1] == '8':
                cnt += 1
    return cnt

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in idrange.CH_IdRange2Name.items():
        fig_cnt_dict[name] = 0
    total_end_with8_count = get_total_endwith8_count()
    end_with8_count = 0
    for skip_count in range(0, contract_item_count-NEGLECT_COUNT, 50):
        driver.get(SCAN_URL.format(skip_count+NEGLECT_COUNT))

        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        if len(nfts) == 0:
            print("Could not find items in {}.".format(SCAN_URL.format(skip_count)))
        for nft in nfts:
            nft_text = nft.text
            token_id = utils.get_tokenid_from_html_text(nft_text)
            if token_id != None:
                for (range, name) in idrange.CH_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if str(token_id)[-1] == '8':
                            end_with8_count += 1
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    # dump file
    result_file = open("data/_scan_conflux_chaohu_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    # result_file.write("{},{}\n".format("--TOTAL_END_WITH8_REMAIN--", total_end_with8_count))
    # result_file.write("{},{}\n".format("--END_WITH8_REMAIN--", end_with8_count))
    result_file.close()
    driver.close()