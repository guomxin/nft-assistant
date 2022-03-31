# coding: utf-8

from selenium import webdriver
from datetime import datetime

CONTRACT_ITEM_COUNT = 17169
SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacdvdbkwm4r8jakn721bz8gmyc3m2tf1xj8z0w7rh7&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

TS_IdRange2Name = {
    (20001,20500): '灵禅天使',
    (20501,21000): '风雨天使',
    (21001,21500): '异瞳天使',
    (21501,22000): '黑梦天使',
    (22001,22500): '蓝骨天使',
    (22501,23000): '隐形天使'
}

def return_fig_count(name):
    return 500

NEGLECT_COUNT = 16800

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in TS_IdRange2Name.items():
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
                for (range, name) in TS_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    # dump file
    result_file = open("_scan_conflux_liuyuangel_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()