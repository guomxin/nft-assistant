# coding: utf-8
import requests
import time
from datetime import datetime
import sys
import json

from gycommon import commoninfo
from gycommon import utils

ADD_COL_URL = "https://api.gandart.com/base/composite/addCollection?castingId={}"
COMPOSITE_URL = "https://api.gandart.com/base/v2/composite/confirmCompositeV3"
TIME_OUT = 3

def add_collection(casting_id, token):
    comp_data_col = []
    headers = {
    }
    headers["token"] = token
    res = utils.post_requests_json(ADD_COL_URL.format(casting_id), headers, {}, TIME_OUT)
    if not res:
        return (1, None)
    if not res["success"]:
        return (1, None)
    else:
        #print(res)
        for cinfo in res["obj"]:
            comp_data_col.append(
                [cinfo["id"], cinfo["viewSort"]]
            )
        return (0, comp_data_col)

def composite(data, token):
    #print(data)
    headers = {
    }
    headers["token"] = token

    while True:
        try: 
            res = requests.post(COMPOSITE_URL, data=data, headers=headers, timeout=TIME_OUT).json()
            if not res["success"]:
                print("合成失败: msg={}, data={}".format(
                    res["msg"], data))
                return False
            else:
                print(res)
                return True
        except Exception as e:
            time.sleep(3)
            print(e)

START_HOUR = 17

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("{} <composite_id> <casting_id> <count>.".format(sys.argv[0]))
        sys.exit(1)
    composite_id = int(sys.argv[1])
    casting_id = int(sys.argv[2])
    count = int(sys.argv[3])
    
    lp_cnt = 0
    while True:
        lp_cnt += 1
        cur_time = datetime.now()
        if cur_time.hour != START_HOUR:
            if lp_cnt % 120 == 0:
                print(cur_time)
                lp_cnt = 0
            time.sleep(0.5) 
        else:
            break

    # 获取已有材料
    (res_code, comp_data_col) = add_collection(casting_id, commoninfo.Home_Token)
    if res_code != 0:
        print("获取合成材料失败!")
        sys.exit(1)
    if len(comp_data_col) < count:
        print("合成材料不足")
        sys.exit(1)

    # 组装合成材料
    for i in range(0, len(comp_data_col), count):
        data = {
            "id": composite_id,
            "compositeQoList": [],
        }
        
        cdata = comp_data_col[i:i+count]
        if len(cdata) < count:
            continue
        orderId = ",".join([str(c[0]) for c in cdata])
        num = [c[0] for c in cdata]
        material = {
            "orderId": orderId,
            "needQuantity": count,
            "id": casting_id,
            "num": num
        }
        data["compositeQoList"].append(material)
        composite({"data": json.dumps(data)}, commoninfo.Home_Token)
        time.sleep(2)