# coding: utf-8

import sys
import datetime
import requests
import time

from conflux import (
    Conflux,
    HTTPProvider
)

from tpcommon import trans
from tpcommon import contract

GET_ACCOUNT_TOKEN_URL = "https://api.confluxscan.net/account/tokens?account={}"

def get_account_tokens(account_address):
    tokens_info = [] #(contract_name, contract_address, token_count)
    while True:
        try:
            resp = requests.get(GET_ACCOUNT_TOKEN_URL.format(account_address))
            resp_json = resp.json()
            for token_info in resp_json["data"]["list"]:
                tokens_info.append((
                    token_info["name"],
                    token_info["contract"],
                    token_info["amount"]))
            return tokens_info
        except Exception as e:
            print(e)

def sort_and_output_userinfo(userinfo_dict, result_file_name):
    users_info = []
    for u in userinfo_dict:
        uinfo = [u, userinfo_dict[u]]
        users_info.append(uinfo)
    users_info.sort(key=lambda a: a[1], reverse=True)
    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        for (addr, cnt) in users_info:
            result_file.write("{},{},{}\n".format(
                trans.blur_address(addr), cnt, addr
            ))

def sort_and_output_prodinfo(prod_info_dict, result_file_name):
    prods_info = []
    for p in prod_info_dict:
        pinfo = [p, prod_info_dict[p]]
        prods_info.append(pinfo)
    prods_info.sort(key=lambda a: a[1], reverse=True)
    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        for (prod, cnt) in prods_info:
            result_file.write("{},{}\n".format(
                prod, cnt
            ))

def remove_tail_numbers(token_name):
    if len(token_name) == 0:
        return ""
    index = len(token_name) - 1
    while (index >= 0) and token_name[index:].isdigit():
        index -= 1
    if index < 0:
        # 全为数字
        return token_name
    else:
        return token_name[:index+1]

def postprocess_token_name(token_name):
    if len(token_name) == 0:
        return token_name
    token_name = token_name.strip()
    # 去掉尾部的"-""
    if token_name[-1] == "-":
        token_name = token_name[:-1]
    if (token_name == "高级款") or (token_name == "隐藏款") or (token_name == "珍贵款") or (token_name == "稀有款") or \
        (token_name == "史诗款") or (token_name == "传说款"):
        # 说明是潮虎系列
        token_name = "潮虎:" + token_name
    return token_name

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <date>(YYmmdd).".format(sys.argv[0]))
        sys.exit(1)
    
    date_str = sys.argv[1]
    start_time = datetime.datetime.strptime(date_str + " 0:0:0", "%Y%m%d %H:%M:%S")
    end_time = datetime.datetime.strptime(date_str + " 23:59:59", "%Y%m%d %H:%M:%S")

    account_tokens = get_account_tokens(trans.Taopai_Conflux_Address)
    provider = HTTPProvider('https://main.confluxrpc.com')
    c =  Conflux(provider)

    blindbox_userinfo_dict = {}
    buyer_userinfo_dict = {}
    solder_userinfo_dict = {}
    active_userinfo_dict = {} # {address: (total_cnt, buy_cnt, sold_cnt, blindbox_cnt)}
    product_info_dict = {} # {name: cnt}

    for (contract_name,contract_address,_) in account_tokens:
        contra = c.contract(contract_address, contract.TaoPai_ABI)
        if not contract.is_taopai_contract(contract_address):
            continue
        print("分析合约：{}".format(contract_name))
        trans_info = trans.get_current_top10000_trans(contract_address, start_time)
        for (trans_hash, trans_time_str) in trans_info:
            trans_time = datetime.datetime.strptime(trans_time_str, "%Y/%m/%d %H:%M:%S")
            if (trans_time < start_time) or (trans_time > end_time):
                continue
            trans_data = c.cfx.getTransactionByHash(trans_hash)
            (from_addr, to_addr, token_id) = trans.get_transinfo_from_data(trans_data, contra)
            if (from_addr == None) or (to_addr == None):
                # 说明不是transfer交易，忽略
                continue

            if to_addr == trans.Taopai_Conflux_Address:
                # to address 如果是淘派的地址，说明是合成或回收行为，不计入统计
                continue
            if from_addr == trans.Taopai_Conflux_Address:
                # from address 如果是淘派的地址，说明是打开盲盒或者空投
                if to_addr not in blindbox_userinfo_dict:
                    blindbox_userinfo_dict[to_addr] = 0
                blindbox_userinfo_dict[to_addr] += 1

                if to_addr not in active_userinfo_dict:
                    active_userinfo_dict[to_addr] = [0,0,0]
                active_userinfo_dict[to_addr][2] += 1
            else:
                # 持有着之间的交易
                if from_addr not in solder_userinfo_dict:
                    solder_userinfo_dict[from_addr] = 0
                solder_userinfo_dict[from_addr] += 1
                if from_addr not in active_userinfo_dict:
                    active_userinfo_dict[from_addr] = [0,0,0]
                active_userinfo_dict[from_addr][1] += 1

                if to_addr not in buyer_userinfo_dict:
                    buyer_userinfo_dict[to_addr] = 0
                buyer_userinfo_dict[to_addr] += 1
                if to_addr not in active_userinfo_dict:
                    active_userinfo_dict[to_addr] = [0,0,0]
                active_userinfo_dict[to_addr][0] += 1

                token_name = contract.get_token_name(contract_address, token_id)
                if token_name == None:
                    # 获取失败
                    token_name = "未知"
                token_name = remove_tail_numbers(token_name)
                token_name = postprocess_token_name(token_name)
                if token_name not in product_info_dict:
                    product_info_dict[token_name] = 0
                product_info_dict[token_name] += 1

            # wait for some time for HTTP 429 error
            time.sleep(0.2)
    
    # 输出active账户信息
    anyactive_result_file_name = "data/_stat_activeuser_{}_result_{}.csv".format(
        "ANY", date_str
    )
    activeusers_info = []
    for a in active_userinfo_dict:
        ainfo = [a, sum(active_userinfo_dict[a])]
        ainfo.extend(active_userinfo_dict[a])
        activeusers_info.append(ainfo)
    activeusers_info.sort(key=lambda a: a[1], reverse=True)
    with open(anyactive_result_file_name, "w", encoding="utf-8-sig") as anyactive_result_file:
        for (addr, total_cnt, buy_cnt, sold_cnt, blindbox_cnt) in activeusers_info:
            anyactive_result_file.write("{},{},{},{},{},{}\n".format(
                trans.blur_address(addr), total_cnt, buy_cnt, sold_cnt, blindbox_cnt, addr
            ))

    # 输出买入账户信息
    buy_result_file_name = "data/_stat_activeuser_{}_result_{}.csv".format(
        "BUY", date_str
    )
    sort_and_output_userinfo(buyer_userinfo_dict, buy_result_file_name)

    # 输出卖出账户信息
    sold_result_file_name = "data/_stat_activeuser_{}_result_{}.csv".format(
        "SOLD", date_str
    )
    sort_and_output_userinfo(solder_userinfo_dict, sold_result_file_name)

    # 输出开盲盒或空投账户信息
    blindbox_result_file_name = "data/_stat_activeuser_{}_result_{}.csv".format(
        "BLINDBOX", date_str
    )
    sort_and_output_userinfo(blindbox_userinfo_dict, blindbox_result_file_name)

    # 输出交易的token信息
    product_result_file_name = "data/_stat_activeuser_{}_result_{}.csv".format(
        "PRODUCT", date_str
    )
    sort_and_output_prodinfo(product_info_dict, product_result_file_name)


