# coding: utf-8

from selenium import webdriver

SCAN_URL = "https://confluxscan.io/address/cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz?NFTAddress=cfx%3Aachew68x34cwu04aezbunyaz67gppakvmyn79tau56&limit=50&skip={}&tab=nft-asset"
CSS_SELECTOR = "div.sc-8rjegh-0.eTefxZ > div > section.sc-fzoNJl.loPePV > div > div > div > div > div > div > div > div > div > div.sc-1hbozql-2.bnWPJO > div.ant-row > div.ant-col"
FLAG = "TokenID:"

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    name2ids = {}

    for skip_count in range(0, 1566, 50):
        driver.get(SCAN_URL.format(skip_count))

        nfts = driver.find_elements_by_css_selector(CSS_SELECTOR)
        for nft in nfts:
            nft_text = nft.text
            flag_pos = nft_text.find(FLAG)
            if flag_pos != -1:
                name = nft_text[:flag_pos].strip()
                token_id = int(nft_text[flag_pos+len(FLAG):].strip())
                if not name:
                    continue
                if name not in name2ids:
                    name2ids[name] = []
                name2ids[name].append(token_id)
            else:
                print("Couldn't find {} in {}.", FLAG, nft_text)
    driver.close()

    # dump the dict
    dump_file = open("data/_general_scan_conflux.txt", "w")
    for (name, ids) in name2ids.items():
        dump_file.write("{}: {},\n".format(name, ids))
    dump_file.close()