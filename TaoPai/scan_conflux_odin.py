# coding: utf-8

from selenium import webdriver
from datetime import datetime
import sys

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacg8eeuem70cbbtp4ygznshd13kgw27wu6t2sk9u9s&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

FIG_WU_NAME = "吴国县吏"
FIG_WEI_NAME = "魏国县吏"
FIG_YUAN_NAME = "园"
FIG_GE_NAME = "阁"
FIG_XIAOZHU_NAME = "小筑"
FIG_GENERAL_ZHUZHAI_NAME = "住宅"

ODin_IdRange2Name = {
    (817,1065): FIG_WU_NAME,
    (1076,1344): FIG_WEI_NAME,
    (2041,3740): FIG_GENERAL_ZHUZHAI_NAME
}

def return_fig_count(name):
    wu_cnt = 10
    wei_cnt = 10
    yuan_cnt = 25
    ge_cnt = 75
    xiaozhu_cnt = 400

    if name == FIG_WU_NAME:
        return wu_cnt
    elif name == FIG_WEI_NAME:
        return wei_cnt
    elif name == FIG_YUAN_NAME:
        return yuan_cnt
    elif name == FIG_GE_NAME:
        return ge_cnt
    elif name == FIG_XIAOZHU_NAME:
        return xiaozhu_cnt

NEGLECT_COUNT = 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in ODin_IdRange2Name.items():
        if name == FIG_GENERAL_ZHUZHAI_NAME:
            fig_cnt_dict[FIG_YUAN_NAME] = 0
            fig_cnt_dict[FIG_GE_NAME] = 0
            fig_cnt_dict[FIG_XIAOZHU_NAME] = 0
        else:
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
                for (range, name) in ODin_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        n = name
                        # 如果是住宅，根据token_id细分
                        if n == FIG_GENERAL_ZHUZHAI_NAME:
                            if token_id % 20 == 0:
                                n = FIG_YUAN_NAME
                            elif token_id % 5 == 0:
                                n = FIG_GE_NAME
                            else:
                                n = FIG_XIAOZHU_NAME 
                        if n not in fig_cnt_dict:
                            fig_cnt_dict[n] = 0
                        fig_cnt_dict[n] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    # dump file
    result_file = open("_scan_conflux_ODin_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()