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

# 部分材料消耗完后，短时间内会返回（比如黄金之路岛徽章），设置等待时间
RETURN_TIME = 30 #(s)

def add_collections(casting_ids, token):
    comp_data_cols = []
    for casting_id in casting_ids:
        (res_code, comp_data_col) = add_collection(casting_id, commoninfo.Home_Token)
        if res_code != 0:
            print("获取CastingId:{}失败, 等待{}s...".format(casting_id, RETURN_TIME))
            time.sleep(RETURN_TIME)
            (res_code, comp_data_col) = add_collection(casting_id, commoninfo.Home_Token)
            if res_code != 0:
                print("获取合成材料CastingId:{}失败!".format(casting_id))
                sys.exit(1)
        comp_data_cols.append(comp_data_col)
    return comp_data_cols

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

START_HOUR = 16

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("{} <composite_id> <casting_ids> <counts>.".format(sys.argv[0]))
        sys.exit(1)
    composite_id = int(sys.argv[1])
    casting_ids = [int(i) for i in sys.argv[2].split(":")]
    counts = [int(i) for i in sys.argv[3].split(":")]
    
    """
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
    """
    # 组装合成材料
    while True:
        # 获取已有材料
        comp_data_cols = add_collections(casting_ids, commoninfo.Home_Token)
        if len(comp_data_cols) < len(counts):
            print("合成材料种类不足!")
            sys.exit(1)

        data = {
            "id": composite_id,
            "compositeQoList": [],
        }
        for i in range(0, len(counts)):
            comp_data_col = comp_data_cols[i]
            count = counts[i]
            if len(comp_data_col) < count:
                print("CastingId:{} 缺少材料!".format(casting_ids[i]))
                sys.exit(0)
            cdata = comp_data_col[:count]
            orderId = ",".join([str(c[0]) for c in cdata])
            num = [c[0] for c in cdata]
            material = {
                "orderId": orderId,
                "needQuantity": count,
                "id": casting_ids[i],
                "num": num
            }
            data["compositeQoList"].append(material)
        composite({"data": json.dumps(data)}, commoninfo.Home_Token)
        time.sleep(2)