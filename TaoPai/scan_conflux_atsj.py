# coding: utf-8

from selenium import webdriver
from datetime import datetime
from tpcommon import idrange
import sys

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacb7hr0ecyatev5gzjnys9mt31xxa22hzuzb3tprps&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

def return_fig_count(name):
    xr_cnt = 300
    ur_per_fig_cnt = 300
    ssr_per_fig_cnt = 300
    sr_per_fig_cnt = 450
    r_per_fig_cnt = 500
    if name.startswith("隐藏款"):
        return 100
    elif name.startswith("XR"):
        return xr_cnt
    elif name.startswith("UR"):
        return ur_per_fig_cnt
    elif name.startswith("SSR"):
        return ssr_per_fig_cnt
    elif name.startswith("SR"):
        return sr_per_fig_cnt
    elif name.startswith("R"):
        return r_per_fig_cnt

# div > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div:nth-child(1) > div > div > div > div.info > div.info-name
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in idrange.ATSJ_IdRange2Name.items():
        fig_cnt_dict[name] = 0
    for skip_count in range(0, contract_item_count, 50):
        driver.get(SCAN_URL.format(skip_count))
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        if len(nfts) == 0:
            print("Could not find items in {}.".format(SCAN_URL.format(skip_count)))
        for nft in nfts:
            nft_text = nft.text
            flag_pos = nft_text.find(FLAG)
            if flag_pos != -1:
                token_id = int(nft_text[flag_pos+len(FLAG):].strip())
                for (range, name) in idrange.ATSJ_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    
    # dump file
    result_file = open("data/_scan_conflux_ATSJ_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()