# coding: utf-8

from email.mime import image
from selenium import webdriver
import requests
import time

RANKER_URL = "https://nft.taopainft.com/friends"
DETAIL_URL = "https://confluxscan.io/stat/nft/checker/detail?contractAddress=cfx:achew68x34cwu04aezbunyaz67gppakvmyn79tau56&tokenId={}"

INPUT_SELECTOR = "#__next > div > div.flex > input"
QUERY_SELECTOR = "#__next > div > div.flex > button"
RANKINFO_SELECTOR = "#__next > div > div.text-gray-50 > div.text-base.my-6.pl-4 > p:nth-child(2)"

def get_rank(rankinfo):
    # 排名: 9396 / 9628
    pos1 = rankinfo.find(':')
    if pos1 == -1:
        return
    pos2 = rankinfo.find('/', pos1+1)
    if pos2 == -1:
        return
    return int(rankinfo[pos1+1:pos2].strip())

def get_image_uri(token_id):
    resp = requests.get(DETAIL_URL.format(token_id))
    resp_json = resp.json()
    resp.close()
    return resp_json['data']['imageUri']

if __name__ == "__main__":
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    # Set cookie
    driver.get(RANKER_URL)
    driver.add_cookie({'name':'refreshToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQxNDIzMjQsImlhdCI6MTY1MTU1MDMyNCwidXNlclVJRCI6eyJ1c2VySWQiOjU1MTh9fQ.ogfeGrbHxcHqG2VRkL1smxghyy-Fz6SEf1oTZg2fHBQ', 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTE1NTA5MjQsImlhdCI6MTY1MTU1MDMyNCwidXNlclVJRCI6eyJ1c2VySWQiOjU1MTh9fQ.laDpmZHZ-D-bxvxfmDTce7WU7hCS9gXB7KDi-FnT9CQ', 'path':'/'})
    driver.add_cookie({'name':'cert', 'value':'1', 'path':'/'})

    # enter the page and find elements
    driver.get(RANKER_URL)
    input_ele = driver.find_element_by_css_selector(INPUT_SELECTOR)
    query_ele = driver.find_element_by_css_selector(QUERY_SELECTOR)
    rankinfo_ele = driver.find_element_by_css_selector(RANKINFO_SELECTOR)

    # get rank and imageuri
    token_info_list = []
    token_cnt = 0
    for token_id in range(100001, 109629):
        input_ele.clear()
        input_ele.send_keys(str(token_id))
        query_ele.click()

        rankinfo = rankinfo_ele.text.strip()
        rank = get_rank(rankinfo)
        image_uri = get_image_uri(token_id)

        token_info_list.append((rank, token_id, image_uri))
        token_cnt += 1
        if token_cnt % 100 == 0:
            print("{} tokens.".format(token_cnt))
        
        time.sleep(0.3)
    driver.close()
    
    # sort
    token_info_list.sort(key=lambda info: info[0])

    # dump files
    with open("data/_extract_kaozaifriends_ranks.csv", "w") as result_file:
        for (rank, token_id, image_uri) in token_info_list:
            result_file.write("{},{},{}\n".format(
                rank, token_id, image_uri
            ))
    with open("data/_extract_kaozaifriends_top100.md", "w", encoding="utf-8-sig") as top100_file:
        top100_file.write("|排名|TokenId|图像|\n")
        top100_file.write("|-|-|-|\n")
        for (rank, token_id, image_uri) in token_info_list[:100]:
            top100_file.write("|{}|{}|![]({})|\n".format(
                rank, token_id, image_uri
            ))

    with open("data/_extract_kaozaifriends_bot100.md", "w", encoding="utf-8-sig") as bot100_file:
        bot100_file.write("|排名|TokenId|图像|\n")
        bot100_file.write("|-|-|-|\n")
        for (rank, token_id, image_uri) in token_info_list[-100:]:
            bot100_file.write("|{}|{}|![]({})|\n".format(
                rank, token_id, image_uri
            ))