# coding: utf-8
from datetime import datetime
import requests
import time
import sys

from gycommon import commoninfo
from gycommon import utils


TIME_OUT = 3
BUY_URL = "https://api.gandart.com/base/v2/resaleManage/resale/buy"

# 173
HOME_PC_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIxNzM2MjE4Njk2MSIsInNvdXJjZSI6InBjIiwidHlwZSI6ImN1c3RvbWVyIiwiZXhwIjoxNjY3Mzk2OTg5LCJzaWduSWQiOiI5ZTJjYjRmZTRmOWY0NDNmOGJhNDgxNjgwMWNmZTIxNiIsImlhdCI6MTY2Njc5MjE4OX0.zA2T82D8vot1JNw-OcU5MaLeHLsx02hLcCLfsAzpGus"
# 159
LAPTOP_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIxNTkxMDYxOTk2MyIsInNvdXJjZSI6InBjIiwidHlwZSI6ImN1c3RvbWVyIiwiZXhwIjoxNjY2NTc4NTE4LCJzaWduSWQiOiJhZDE0OGYxYzUzNzY0MTVkODgxZmI2ZjcyMjgyZmU3NSIsImlhdCI6MTY2NTk3MzcxOH0.1zrXRh-UMNYwbyoBTQKK7Qvcc111BvkT9DEhEC_I504"

def buy_product(data, token):
    headers = {
        "token": token,
    }

    while True:
        try: 
            res = requests.post(BUY_URL, data=data, headers=headers, timeout=TIME_OUT).json()
            if not res["success"]:
                print("下单失败: {} data={},msg={}".format(
                    datetime.now(), data, res["msg"]))
                return False
            else:
                return True
        except Exception as e:
            time.sleep(0.5)
            print(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <dict_id>.".format(sys.argv[0]))
        sys.exit(1)
    dict_id = int(sys.argv[1])
    token = None
    if dict_id == 1:
        token = HOME_PC_TOKEN
    elif dict_id == 2:
        token = HOME_PC_TOKEN
    elif dict_id == 3:
        token = LAPTOP_TOKEN
    elif dict_id == 4:
        token = LAPTOP_TOKEN
    
    products = [
        {
            "castingId": 101,
            "detailId": 285768,
            "transactionRecordId": 361811,
            "userId": 406,
        },
        {
            "castingId": 101,
            "detailId": 281092,
            "transactionRecordId": 360494,
            "userId": 49396,
        },
    ]

    loop_cnt = 0
    wx_msg_count = 0
    while True:
        try:
            for data in products:
                if buy_product(data, token):
                    content = """
光予: 购买{}
>时间: {}
>价格: {}""".format("", datetime.now(), "指定")
                    print(content)
                    utils.send_workwx_msg("markdown", content)
                else:
                    wx_msg_count += 1
                    if wx_msg_count == 50:
                        content = """
光予: 下单失败{}
>时间: {}
>价格: {}""".format("", datetime.now(), "指定")
                        print(content)
                        utils.send_workwx_msg("markdown", content)
                        wx_msg_count = 0
                            
                # 防止被封禁
                time.sleep(0.5)
                    
            loop_cnt += 1
            #print(loop_cnt)
            if loop_cnt % 100 == 0:
                print("{} {} rounds.".format(datetime.now(), loop_cnt))

            # 判断时间是否超过0点
            cur_time = datetime.now()
            #if cur_time.hour == 0 :
            #    break
        except Exception as e:
            print(e)
            # 出错后等待一段时间
            time.sleep(3)
    