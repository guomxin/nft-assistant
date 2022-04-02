# coding: utf-8
# ContractName: LT

from selenium import webdriver

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aacaha2pz5j1g6b0fbv9xazv5umm587xucjcdu83b02&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

LT_Name2IdRange = {
    (8382,8680): '<PlaceHolder_1>',
    (8083,8381): '<PlaceHolder_2>',
    (7784,8082): '<PlaceHolder_3>',
    (7485,7783): '<PlaceHolder_4>',
    (7186,7484): '<PlaceHolder_5>',
    (6887,7185): '<PlaceHolder_6>',
    (6588,6886): '<PlaceHolder_7>',
    (6289,6587): '<PlaceHolder_8>',
    (5990,6288): '<PlaceHolder_9>',
    (5691,5989): '<PlaceHolder_10>',
    (5392,5690): '<PlaceHolder_11>',
    (5093,5391): '<PlaceHolder_12>',
    (4794,5092): '<PlaceHolder_13>',
    (4495,4793): '<PlaceHolder_14>',
    (4196,4494): '<PlaceHolder_15>',
    (3897,4195): '<PlaceHolder_16>',
    (3598,3896): '<PlaceHolder_17>',
    (3299,3597): '<PlaceHolder_18>',
    (3000,3298): '<PlaceHolder_19>',
}

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    for skip_count in range(0, 5733, 50):
        driver.get(SCAN_URL.format(skip_count))
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        for nft in nfts:
            nft_text = nft.text
            flag_pos = nft_text.find(FLAG)
            if flag_pos != -1:
                name = nft_text[:flag_pos].strip()
                token_id = int(nft_text[flag_pos+len(FLAG):].strip())
                for (range, n) in LT_Name2IdRange.items():
                    if name and n.startswith("<PlaceHolder") and (token_id >= range[0]) and (token_id <= range[1]):
                        LT_Name2IdRange[range] = name                        
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    driver.close()

    # dump the dict
    dump_file = open("_gen_idrange2name_lt.txt", "w")
    for (range, name) in LT_Name2IdRange.items():
        dump_file.write("({},{}): '{}',\n".format(range[0], range[1], name))
    dump_file.close()