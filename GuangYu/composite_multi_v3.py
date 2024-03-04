# coding: utf-8
import requests
import time
from datetime import datetime
import sys
import json

from gycommon import commoninfo
from gycommon import utils

QUERY_COMPOSITE_URL = "https://api.gandart.com/api/v2/composite/v3/list/v2"
ADD_COL_URL = "https://api.gandart.com/read/api/composite/getDetailByCasting"
COMPOSITE_URL = "https://api.gandart.com/base/v2/composite/v3/confirmCompositeV3"
TIME_OUT = 3
PAGE_SIZE = 1000

def query_composite_info(token):
    headers = {
    }
    headers["token"] = token
    data = {
        "page": 1,
        "pageSize": 10,
        "total": 0,
        "status": 1,
        "labelName": "",
    }
    res = utils.post_requests_json(QUERY_COMPOSITE_URL, headers, data, TIME_OUT)
    if not res:
        return (1, None)
    else:
        #print(res)
        return (0, res["rows"])

def add_collections(casting_ids, token):
    comp_data_cols = []
    for casting_id in casting_ids:
        (res_code, comp_data_col) = add_collection(casting_id, commoninfo.Home_Token)
        if res_code != 0:
            print("获取合成材料失败!")
            sys.exit(1)
        print("CastingId:{}, Count:{}".format(casting_id, len(comp_data_col)))
        comp_data_cols.append(comp_data_col)
    return comp_data_cols

def add_collection(casting_id, token):
    comp_data_col = []
    headers = {
    }
    headers["token"] = token
    data = {
        "castingId": casting_id,
        "page": 1,
        "pageSize": PAGE_SIZE
    }
    res = utils.post_requests_json(ADD_COL_URL, headers, data, TIME_OUT, True)
    if not res:
        return (1, None)
    if not res["success"]:
        return (1, None)
    else:
        #print(res)
        for cinfo in res["obj"]["list"]:
            comp_data_col.append(
                [cinfo["id"], cinfo["viewSort"]]
            )
        return (0, comp_data_col)

def composite(data, token):
    #print(data)
    headers = {
    }
    headers["token"] = token
    #headers["content-type"] = "application/json"

    while True:
        try: 
            res = requests.post(COMPOSITE_URL, json=data, headers=headers, timeout=TIME_OUT).json()
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

START_MIN = 41

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("{} <composite_name> <casting_ids> <counts> <batch> <loops>.".format(sys.argv[0]))
        sys.exit(1)
    target_composite_name = sys.argv[1].strip()
    casting_ids = [int(i) for i in sys.argv[2].split(":")]
    counts = [int(i) for i in sys.argv[3].split(":")]
    batch_count = int(sys.argv[4])
    loops = int(sys.argv[5])
    
    appear = False
    composite_id = None
    while not appear:
        res_code, comp_list = query_composite_info(commoninfo.Home_Token)
        if res_code != 0:
            print("获取合成信息列表失败")
            time.sleep(1)
        else:
            for comp_info in comp_list:
                composite_name = comp_info["compositeTaskName"]
                if composite_name.find(target_composite_name) != -1:
                    composite_id = comp_info["id"]
                    print("{} 开始合成, id={}".format(composite_name, composite_id))
                    appear = True
                    break
            if not appear:
                time.sleep(1)
    
    '''
    lp_cnt = 0
    while True:
        lp_cnt += 1
        cur_time = datetime.now()
        if cur_time.minute != START_MIN:
            if lp_cnt % 120 == 0:
                print(cur_time)
                lp_cnt = 0
            time.sleep(0.05) 
        else:
            break
    time.sleep(1)
    '''

    # 获取已有材料
    comp_data_cols = add_collections(casting_ids, commoninfo.Home_Token)
    if len(comp_data_cols) < len(counts):
        print("合成材料种类不足!")
        sys.exit(1)

    # 组装合成材料
    sids = [0] * len(counts)
    for _ in range(loops):
        data = {
            "taskId": composite_id,
            "compositeList": [],
        }

        for _ in range(batch_count):
            materialDL = {
                    "materialDetailList":[],
            }
            for i in range(0, len(counts)):
                comp_data_col = comp_data_cols[i]
                count = counts[i]
                if (len(comp_data_col) - sids[i]) < count:
                    print("CastingId:{} 缺少材料!".format(casting_ids[i]))
                    sys.exit(0)
                cdata = comp_data_col[sids[i]:sids[i]+count]
                orderId = ",".join([str(c[0]) for c in cdata])
                num = [c[0] for c in cdata]
                material = {
                    "castingId": casting_ids[i],
                    "orderList": num
                }
                materialDL["materialDetailList"].append(material)
                sids[i] += count
            data["compositeList"].append(materialDL)
        composite(data, commoninfo.Home_Token)
        time.sleep(3)