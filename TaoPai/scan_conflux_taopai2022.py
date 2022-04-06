# coding: utf-8

from selenium import webdriver
from datetime import datetime
import sys

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aachew68x34cwu04aezbunyaz67gppakvmyn79tau56&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

TaoPai2022_IdRange2Name = {
    (30001,30100): '颜值爆表',
    (30101,30200): '狂吃不胖',
    (30201,30300): '脱发拜拜',
    (30301,30400): '升职加薪',
    (30401,30500): '财务自由',
    (30501,30600): '一夜暴富',
    (30601,30700): '颜值在线',
    (30701,30800): '大吉大利',
    (30801,30900): '锦鲤附体',
    (30901,31000): '睡到自然醒',
    (31001,31100): '别墅靠着海',
    (31101,31200): '要自由',
    (31201,31300): '去旅行吧',
    (31301,31400): '多喝热水',
    (31401,31500): '记得铲屎',
    (31501,31600): '爱自己',
    (31601,31700): '世界和平',
    (31701,31800): '不空虚',
    (31801,31900): '新生',
    (31901,32000): '涨涨涨',
    (32001,32011): '日进斗金',
    (32012,32023): '桃花旺旺'
}

def return_fig_count(name):
    if name == "日进斗金" or name == "桃花旺旺":
        return 11
    else:
        return 100

NEGLECT_COUNT = 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <contract_item_count>".format(sys.argv[0]))
        sys.exit(1)
    contract_item_count = int(sys.argv[1])

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for (_, name) in TaoPai2022_IdRange2Name.items():
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
                for (range, name) in TaoPai2022_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    # dump file
    result_file = open("data/_scan_conflux_taopai2022_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()