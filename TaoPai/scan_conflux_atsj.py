# coding: utf-8

from selenium import webdriver
from datetime import datetime

CONTRACT_ITEM_COUNT = 5845
SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacb7hr0ecyatev5gzjnys9mt31xxa22hzuzb3tprps&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

ATSJ_IdRange2Name = {
    (38501,38800): 'XR-全家福',
    (38201,38500): 'UR-金',
    (37901,38200): 'UR-嘉德罗斯',
    (37601,37900): 'UR-雷狮',
    (37301,37600): 'UR-格瑞',
    (37001,37300): 'UR-安迷修',
    (36701,37000): 'SSR-金',
    (36401,36700): 'SSR-凯莉',
    (36101,36400): 'SSR-嘉德罗斯',
    (35801,36100): 'SSR-雷狮',
    (35501,35800): 'SSR-卡米尔',
    (35201,35500): 'SSR-格瑞',
    (34901,35200): 'SSR-安迷修',
    (34601,34900): 'SSR-雷伊',
    (34301,34600): 'SSR-神近耀',
    (34001,34300): 'SSR-帕洛斯',
    (33551,34000): 'SR-安莉洁',
    (33101,33550): 'SR-金',
    (32651,33100): 'SR-凯莉',
    (32201,32650): 'SR-嘉德罗斯',
    (31751,32200): 'SR-雷德',
    (31301,31750): 'SR-紫堂幻',
    (30851,31300): 'SR-秋',
    (30401,30850): 'SR-雷狮',
    (29951,30400): 'SR-佩利',
    (29501,29950): 'SR-卡米尔',
    (29051,29500): 'SR-紫堂真',
    (28601,29050): 'SR-格瑞',
    (28151,28600): 'SR-赞德',
    (27701,28150): 'SR-安迷修',
    (27251,27700): 'SR-埃米',
    (26801,27250): 'SR-雷伊',
    (26351,26800): 'SR-神近耀',
    (25901,26350): 'SR-丹尼尔',
    (25451,25900): 'SR-艾比',
    (25001,25450): 'SR-帕洛斯',
    (24501,25000): 'R-裁判球',
    (24001,24500): 'R-小黑洞',
    (23501,24000): 'R-雷蛰',
    (23001,23500): 'R-鬼狐天冲',
    (22501,23000): 'R-见习天使',
    (22001,22500): 'R-杰德里',
    (21501,22000): 'R-哆莉',
    (21001,21500): 'R-萝洁特',
    (20501,21000): 'R-龙阁',
    (20001,20500): 'R-拉比兹',
    (19501,20000): 'R-莱耶斯',
    (19001,19500): 'R-罗德烈',
    (18501,19000): 'R-雷震',
    (18001,18500): 'R-雷霆',
    (17501,18000): 'R-银爵',
    (17001,17500): 'R-赤星',
    (16501,17000): 'R-梅莉蕾蒂',
    (16001,16500): 'R-霍金斯',
    (15501,16000): 'R-维德',
    (15001,15500): 'R-法尔法拉',
    (14501,15000): 'R-蒙特祖玛',
    (14001,14500): 'R-菲利斯·尼克瑞斯',
    (13501,14000): 'R-安吉拉',
    (13001,13500): 'R-莱娜',
    (12501,13000): 'R-蜜蜜',
    (12001,12500): 'R-紫堂林',
    (11501,12000): 'R-安特',
    (11001,11500): 'R-紫堂陆',
    (10501,11000): 'R-悦然',
    (10001,10500): 'R-京弥'
}

def return_fig_count(name):
    xr_cnt = 300
    ur_per_fig_cnt = 300
    ssr_per_fig_cnt = 300
    sr_per_fig_cnt = 450
    r_per_fig_cnt = 500
    if name.startswith("XR"):
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
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    fig_cnt_dict = {}
    for skip_count in range(0, CONTRACT_ITEM_COUNT, 50):
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
                for (range, name) in ATSJ_IdRange2Name.items():
                    if (token_id >= range[0]) and (token_id <= range[1]):
                        if name not in fig_cnt_dict:
                            fig_cnt_dict[name] = 0
                        fig_cnt_dict[name] += 1    
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    
    # dump file
    result_file = open("_scan_conflux_ATSJ_result_{}.csv".format(
        datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    ), "w")
    for (fig, cnt) in fig_cnt_dict.items():
        result_file.write("{},{}\n".format(fig, return_fig_count(fig) - cnt))
    result_file.close()
    driver.close()