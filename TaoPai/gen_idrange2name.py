# coding: utf-8

from selenium import webdriver

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacb7hr0ecyatev5gzjnys9mt31xxa22hzuzb3tprps&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

ATSJ_Name2IdRange = {
    (38501,38800): '<PlaceHolder_XR>',
    (38201,38500): '<PlaceHolder_UR_1>',
    (37901,38200): '<PlaceHolder_UR_2>',
    (37601,37900): '<PlaceHolder_UR_3>',
    (37301,37600): '<PlaceHolder_UR_4>',
    (37001,37300): '<PlaceHolder_UR_5>',
    (36701,37000): '<PlaceHolder_SSR_1>',
    (36401,36700): '<PlaceHolder_SSR_2>',
    (36101,36400): '<PlaceHolder_SSR_3>',
    (35801,36100): '<PlaceHolder_SSR_4>',
    (35501,35800): '<PlaceHolder_SSR_5>',
    (35201,35500): '<PlaceHolder_SSR_6>',
    (34901,35200): '<PlaceHolder_SSR_7>',
    (34601,34900): '<PlaceHolder_SSR_8>',
    (34301,34600): '<PlaceHolder_SSR_9>',
    (34001,34300): '<PlaceHolder_SSR_10>',
    (33551,34000): '<PlaceHolder_SR_1>',
    (33101,33550): '<PlaceHolder_SR_2>',
    (32651,33100): '<PlaceHolder_SR_3>',
    (32201,32650): '<PlaceHolder_SR_4>',
    (31751,32200): '<PlaceHolder_SR_5>',
    (31301,31750): '<PlaceHolder_SR_6>',
    (30851,31300): '<PlaceHolder_SR_7>',
    (30401,30850): '<PlaceHolder_SR_8>',
    (29951,30400): '<PlaceHolder_SR_9>',
    (29501,29950): '<PlaceHolder_SR_10>',
    (29051,29500): '<PlaceHolder_SR_11>',
    (28601,29050): '<PlaceHolder_SR_12>',
    (28151,28600): '<PlaceHolder_SR_13>',
    (27701,28150): '<PlaceHolder_SR_14>',
    (27251,27700): '<PlaceHolder_SR_15>',
    (26801,27250): '<PlaceHolder_SR_16>',
    (26351,26800): '<PlaceHolder_SR_17>',
    (25901,26350): '<PlaceHolder_SR_18>',
    (25451,25900): '<PlaceHolder_SR_19>',
    (25001,25450): '<PlaceHolder_SR_20>',
    (24501,25000): '<PlaceHolder_R_1>',
    (24001,24500): '<PlaceHolder_R_2>',
    (23501,24000): '<PlaceHolder_R_3>',
    (23001,23500): '<PlaceHolder_R_4>',
    (22501,23000): '<PlaceHolder_R_5>',
    (22001,22500): '<PlaceHolder_R_6>',
    (21501,22000): '<PlaceHolder_R_7>',
    (21001,21500): '<PlaceHolder_R_8>',
    (20501,21000): '<PlaceHolder_R_9>',
    (20001,20500): '<PlaceHolder_R_10>',
    (19501,20000): '<PlaceHolder_R_11>',
    (19001,19500): '<PlaceHolder_R_12>',
    (18501,19000): '<PlaceHolder_R_13>',
    (18001,18500): '<PlaceHolder_R_14>',
    (17501,18000): '<PlaceHolder_R_15>',
    (17001,17500): '<PlaceHolder_R_16>',
    (16501,17000): '<PlaceHolder_R_17>',
    (16001,16500): '<PlaceHolder_R_18>',
    (15501,16000): '<PlaceHolder_R_19>',
    (15001,15500): '<PlaceHolder_R_20>',
    (14501,15000): '<PlaceHolder_R_21>',
    (14001,14500): '<PlaceHolder_R_22>',
    (13501,14000): '<PlaceHolder_R_23>',
    (13001,13500): '<PlaceHolder_R_24>',
    (12501,13000): '<PlaceHolder_R_25>',
    (12001,12500): '<PlaceHolder_R_26>',
    (11501,12000): '<PlaceHolder_R_27>',
    (11001,11500): '<PlaceHolder_R_28>',
    (10501,11000): '<PlaceHolder_R_29>',
    (10001,10500): '<PlaceHolder_R_30>'
}

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    for skip_count in range(0, 5567, 50):
        driver.get(SCAN_URL.format(skip_count))
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        for nft in nfts:
            nft_text = nft.text
            flag_pos = nft_text.find(FLAG)
            if flag_pos != -1:
                name = nft_text[:flag_pos].strip()
                token_id = int(nft_text[flag_pos+len(FLAG):].strip())
                for (range, n) in ATSJ_Name2IdRange.items():
                    if name and n.startswith("<PlaceHolder") and (token_id >= range[0]) and (token_id <= range[1]):
                        ATSJ_Name2IdRange[range] = name                        
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    driver.close()

    # dump the dict
    dump_file = open("_gen_idrange2name.txt", "w")
    for (range, name) in ATSJ_Name2IdRange.items():
        dump_file.write("({},{}): '{}',\n".format(range[0], range[1], name))
    dump_file.close()