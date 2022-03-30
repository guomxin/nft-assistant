# coding: utf-8

from selenium import webdriver
from datetime import datetime

CONTRACT_ITEM_COUNT = 1646
SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacgjw8bg7gehy3x7x5evfknfe7pst64hp6tgymfwa4&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

CH_IdRange2Name = {
    (4976,4985): '传说',
    (4926,4955): '史诗',
    (4676,4900): '稀有',
    (1,3735): '高级'
}

def return_fig_count(name):
    if name == "传说":
        return 10
    elif name == "史诗":
        return 30
    elif name == "稀有":
        return 225
    elif name == "高级":
        return 3735

NEGLECT_COUNT = 0

def get_total_endwith8_count():
    cnt = 8
    for pair in CH_IdRange2Name.keys():
        start = pair[0]
        end = pair[1] + 1
        for id in range(start, end):
            if str(id)[-1] == '8':
                cnt += 1
    return cnt

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    total_end_with8_count = get_total_endwith8_count()
    end_with8_count = 0
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
                for (range, name) in CH_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if str(token_id)[-1] == '8':
                            end_with8_count += 1
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    # dump file
    result_file = open("_scan_conflux_chaohu_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.write("{},{}\n".format("--TOTAL_END_WITH8_REMAIN--", total_end_with8_count))
    result_file.write("{},{}\n".format("--END_WITH8_REMAIN--", total_end_with8_count - end_with8_count))
    result_file.close()
    driver.close()