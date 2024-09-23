# coding: utf-8

from selenium import webdriver
import time
from datetime import datetime
import requests
import json
import sys

from tpcommon import utils

SCAN_URL = "https://nft.taopainft.com/trade?type=bb86903952ad5df5f5016c8d3d4d895ae892ee89&p={}&s=3&k={}&pid={}&vid={}"
GET_TOKEN_INFO_URL = "https://nft.taopainft.com/v1/handsel/info/token"
TARGET_TOKEN_ID = 0
AUTH_FAILED_CODE = 3

def get_access_token(driver, select_id, cookie_dict):
    try:
        driver.get(SCAN_URL.format(1, "", 0, 0))
        access_token = driver.get_cookie("accessToken")["value"]
        refresh_token = driver.get_cookie("refreshToken")["value"]
        if access_token != cookie_dict["accessToken"]:
            cookie_dict["accessToken"] = access_token
            cookie_dict["refreshToken"] = refresh_token
            utils.dump_cookie_dict(select_id, cookie_dict)
        return access_token
    except Exception as e:
        driver.close()
        raise e

def get_token_info(token_id, access_token):
    for _ in range(10):
        try:
            data = {
                "tokenId":token_id
            }
            headers = {
                "authorization": "Bearer " + access_token,
            }
            res = requests.post(GET_TOKEN_INFO_URL, data=json.dumps(data), headers=headers).json()
            if res["code"] != 0:
                return (res["code"], None)
            else:
                return (res["code"], {
                    "mobile": res["data"]["mobile"],
                    "name": res["data"]["name"],
                })
        except Exception as e:
            time.sleep(0.5)
            print(e)

    return (1, None)


def grab_all_tokens_info(user_infos, cookie_dict):
    wx_msg_count = 0
    #options = webdriver.ChromeOptions()
    #options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.get(SCAN_URL.format(1, "", 0, 0))
    driver.add_cookie({'name':'refreshToken', 'value':cookie_dict['refreshToken'], 'path':'/'})
    driver.add_cookie({'name':'accessToken', 'value':cookie_dict['accessToken'], 'path':'/'})

    ##### 调试设置cookie后的用户信息
    #driver.get(SCAN_URL.format(1, "", 0, 0))
    #time.sleep(100) 

    access_token = get_access_token(driver, 1, cookie_dict)
    # 循环一定次数后重启浏览器
    for i in range(10000):
        ## 获取藏品市场信息
        (res_code, res) = get_token_info(TARGET_TOKEN_ID, access_token)
        if res_code == AUTH_FAILED_CODE:
            # access_token可能已过期，重新获得
            print("{} accessToken可能已过期,重新获取...".format(datetime.now()))
            access_token = get_access_token(driver, 1, cookie_dict)
            (res_code, res) = get_token_info(TARGET_TOKEN_ID, access_token)
            if res_code == AUTH_FAILED_CODE:
                print("{} 重取accessToken失败!".format(datetime.now()))
                continue
        
        TARGET_TOKEN_ID += 1
        if res_code != 0:
            # 此token信息不存在
            pass
        else:
            mobile = res["mobile"]
            name = res["name"]
            if mobile not in user_infos:
                user_infos[mobile] = {}
            if name not in user_infos[mobile]:
                user_infos[mobile][name] = 0
            user_infos[mobile][name] += 1
        
    
        if (i+1) % 100 == 0:
            print("TokenId:{}, ResCode: {},".format(TARGET_TOKEN_ID-1, res_code))
            if res_code != 0:
                print("Res: {}".format(res))

    driver.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <target_dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    cookie_dict = utils.load_cookie_dict(1)

    user_infos = {}
    while True:
        try:
            grab_all_tokens_info(user_infos, cookie_dict)
        except Exception as e:
            print(e)
            time.sleep(5)