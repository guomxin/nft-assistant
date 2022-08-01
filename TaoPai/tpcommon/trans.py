# coding: utf-8
import os, sys
# add python path of tpcommon's parent path to sys.path
parent_path = os.path.abspath(os.path.join(__file__, *([".."]*2)))
if parent_path not in sys.path:
    sys.path.append(parent_path)

from conflux import (
    Conflux,
    HTTPProvider
)
import csv
import datetime
import time
import requests

from tpcommon import contract

Taopai_Conflux_Address = "cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz"

TransHashIndex = 3
TransDateIndex = 9

# http接口获取前1000的交易数据
GET_TRANS_URL = "https://api.confluxscan.net/account/transactions?account={}&skip={}&limit=100&sort=DESC"

def get_current_top10000_trans(contract_address, start_time=None):
    trans_info = [] #(trans_hash, trans_date)
    trans_hash_dict = {} # 向后翻页获取，当交易动态增加时，后续页面会有重复
    earlier_than_start_time = False
    for skip in range(0,10000,100):
        while True:
            try:
                resp = requests.get(GET_TRANS_URL.format(contract_address, skip))
                resp_json = resp.json()
                for trans in resp_json["data"]["list"]:
                    trans_hash = trans["hash"]
                    if trans_hash in trans_hash_dict:
                        continue
                    trans_hash_dict[trans_hash] = 1
                    trans_date = datetime.datetime.fromtimestamp(trans["timestamp"])
                    if (start_time != None) and (trans_date < start_time):
                        earlier_than_start_time = True
                    trans_date_str = trans_date.strftime("%Y/%m/%d %H:%M:%S")
                    trans_info.append((trans_hash, trans_date_str))
                break
            except Exception as e:
                print(e)
                time.sleep(1)
        if earlier_than_start_time:
            break

        # access politely
        time.sleep(0.5)
    return trans_info

def blur_address(address):
    return address[:10] + "****" + address[-4:]

def get_transinfo_from_data(trans_data, contra):
    try:
        decode_result = contra.decode_function_input(trans_data.data)
    except:
        return (None, None, None)
    if ("from" not in decode_result[1]) or ("to" not in decode_result[1]) or ("tokenId" not in decode_result[1]):
        return (None, None, -1)
    from_addr = contract.get_base32addr_from_hexaddr(decode_result[1]["from"])
    to_addr = contract.get_base32addr_from_hexaddr(decode_result[1]["to"])
    token_id = decode_result[1]["tokenId"]

    return (from_addr, to_addr, token_id)

def get_tag_from_tokenid(token_id, ranges, tags):
    for tag_index in range(len(tags)):
        min_tid, max_tid = ranges[tag_index]
        if (min_tid != -1) and token_id < min_tid:
            continue
        if (max_tid != -1) and token_id > max_tid:
            continue
        return tags[tag_index]

def multi_analyze_transaction_logs(trans_file_name, tradeprice_dict, contract_addr, contract_ABI, start_date_str, end_date_str, ranges, tags, result_file_name,  verbose=True):
    provider = HTTPProvider('https://main.confluxrpc.com')
    c =  Conflux(provider)
    contra = c.contract(contract_addr, contract_ABI)
    start_date = datetime.datetime.strptime(start_date_str + " 0:0", "%Y/%m/%d %H:%M")
    end_date = datetime.datetime.strptime(end_date_str + " 23:59", "%Y/%m/%d %H:%M")
    
    result_detail_file_name = result_file_name + ".details.csv"
    date2tradeinfo = {} #date(%Y/%m/%d): (tag: (trade_cnt, open_mbox_cnt))
    date = start_date
    while (date < end_date):
        date_str = date.strftime("%Y/%m/%d")
        date2tradeinfo[date_str] = {}
        for tag in tags:
            date2tradeinfo[date_str][tag] = [0, 0]
        date = date + datetime.timedelta(days=1)
    
    solders_dict = {}
    buyers_dict = {} 
    traderesult_dict = {} # (tag: [total_cnt, [price_list]])
    if len(tradeprice_dict) > 0:
        for tag in tags:
            traderesult_dict[tag] = [0, []]
    with open(trans_file_name) as f, open(result_detail_file_name, "w") as details:
        rows = csv.reader(f)
        target_row_cnt = 0
        is_first_row = True
        for row in rows:
            if is_first_row:
                is_first_row = False
                continue
            trans_hash = row[TransHashIndex]
            trans_date_str = row[TransDateIndex]
            trans_date = datetime.datetime.strptime(trans_date_str, "%Y/%m/%d %H:%M:%S")
            trans_date_short_str = trans_date.strftime("%Y/%m/%d")
            if (trans_date < start_date) or (trans_date > end_date):
                continue

            trans_data = c.cfx.getTransactionByHash(trans_hash)
            (from_addr, to_addr, token_id) = get_transinfo_from_data(trans_data, contra)
            tag = get_tag_from_tokenid(token_id, ranges,tags)
            if not tag:
                continue
            if to_addr == Taopai_Conflux_Address:
                # to address 如果是淘派的地址，说明是合成或回收行为，不计入统计
                details.write("{},{},{},合成或回收,{},{}\n".format(from_addr, to_addr, trans_date_str, tag, token_id))
                continue
            if from_addr == Taopai_Conflux_Address:
                # from address 如果是淘派的地址，说明是打开盲盒或者空投
                date2tradeinfo[trans_date_short_str][tag][1] += 1
                details.write("{},{},{},开盲盒或空投,{},{}\n".format(from_addr, to_addr, trans_date_str, tag, token_id))
            else:
                # 持有者之间的交易
                date2tradeinfo[trans_date_short_str][tag][0] += 1
                
                # 更新交易价格信息
                if len(tradeprice_dict) > 0:
                    traderesult_dict[tag][0] += 1
                    trade_price = "未知"
                    if (token_id in tradeprice_dict) and (len(tradeprice_dict[token_id]) == 1):
                        trade_price = tradeprice_dict[token_id][0]
                        traderesult_dict[tag][1].append(trade_price)
                    details.write("{},{},{},交易,{},{},{}\n".format(
                        from_addr, to_addr, trans_date_str, tag, token_id, trade_price)) 
                else:
                    details.write("{},{},{},交易,{},{}\n".format(
                        from_addr, to_addr, trans_date_str, tag, token_id))  

                # 更新卖方信息
                if from_addr not in solders_dict:
                    solders_dict[from_addr] = [0, {}]
                    for t in tags:
                        solders_dict[from_addr][1][t] = 0
                solders_dict[from_addr][0] += 1
                solders_dict[from_addr][1][tag] += 1

                # 更新买方信息
                if to_addr not in buyers_dict:
                    buyers_dict[to_addr] = [0, {}]
                    for t in tags:
                        buyers_dict[to_addr][1][t] = 0
                buyers_dict[to_addr][0] += 1
                buyers_dict[to_addr][1][tag] += 1

            target_row_cnt += 1

            # wait for some time for HTTP 429 error
            time.sleep(0.2)
    
    if verbose:
        print("{} target transaction records found.".format(target_row_cnt))

    # 由于tags指定时可以重复，对应不同的id区间（见佛系熊猫二期的常规款），输出时tags需要去重
    nodup_tags = []
    for tag in tags:
        if tag not in nodup_tags:
            nodup_tags.append(tag)
    tags = nodup_tags

    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        # 写入交易的数量
        result_file.write("日期,{}\n".format(",".join(tags)))
        for td_str in date2tradeinfo:
            result_file.write("{},{}\n".format(
                td_str, ",".join([str(date2tradeinfo[td_str][tag][0]) for tag in tags])
            ))
        
        # 写入打开盲盒的数量
        result_file.write("日期,{}\n".format(",".join(tags)))
        for td_str in date2tradeinfo:
            result_file.write("{},{}\n".format(
                td_str, ",".join([str(date2tradeinfo[td_str][tag][1]) for tag in tags])
            ))
    
    # 交易价格汇总数据
    if len(traderesult_dict) > 0:
        trade_agg_file_name = result_file_name + ".tradeagg.csv"
        with open(trade_agg_file_name, "w", encoding="utf-8-sig") as trade_agg_file:
            trade_agg_file.write(",交易总量,价格获得量,成交均值,成交最小价格,成交最大价格\n")
            for tag in tags:
                plist = traderesult_dict[tag][1]
                if len(plist) > 0:
                    trade_agg_file.write("{},{},{},{},{},{}\n".format(
                        tag, traderesult_dict[tag][0], len(plist),
                        sum(plist) / len(plist), min(plist), max(plist)
                    ))
                else:
                    trade_agg_file.write("{},{},{},{},{},{}\n".format(
                        tag, traderesult_dict[tag][0], len(plist),
                        "未知", "未知", "未知"
                    ))

    # 卖方数据
    solders_detail_file_name = result_file_name + ".solders.csv"
    solders_info = []
    for s in solders_dict:
        sinfo = [s, solders_dict[s][0]]
        for t in tags:
            sinfo.append(solders_dict[s][1][t])
        solders_info.append(sinfo)
    solders_info.sort(key=lambda s: s[1], reverse=True)
    with open(solders_detail_file_name, "w", encoding="utf-8-sig") as solders_detail_file:
        solders_detail_file.write("账户,卖出总量,{}\n".format(','.join(tags)))
        for solder_info in solders_info:
            solders_detail_file.write("{},{},{}\n".format(
                blur_address(solder_info[0]),
                ','.join([str(s) for s in solder_info[1:]]),
                solder_info[0]))

    # 买方数据
    buyers_detail_file_name = result_file_name + ".buyers.csv"
    buyers_info = []
    for b in buyers_dict:
        binfo = [b, buyers_dict[b][0]]
        for t in tags:
            binfo.append(buyers_dict[b][1][t])
        buyers_info.append(binfo)
    buyers_info.sort(key=lambda b: b[1], reverse=True)
    with open(buyers_detail_file_name, "w", encoding="utf-8-sig") as buyers_detail_file:
        buyers_detail_file.write("账户,买入总量,{}\n".format(','.join(tags)))
        for buyer_info in buyers_info:
            buyers_detail_file.write("{},{},{}\n".format(
                blur_address(buyer_info[0]),
                ','.join([str(s) for s in buyer_info[1:]]),
                buyer_info[0]))

def multi_analyze_transaction_logs_online(tradeprice_dict, contract_addr, contract_ABI, start_date_str, end_date_str, ranges, tags, result_file_name,  verbose=True):
    provider = HTTPProvider('https://main.confluxrpc.com')
    c =  Conflux(provider)
    contra = c.contract(contract_addr, contract_ABI)
    start_date = datetime.datetime.strptime(start_date_str + " 0:0", "%Y/%m/%d %H:%M")
    end_date = datetime.datetime.strptime(end_date_str + " 23:59", "%Y/%m/%d %H:%M")
    
    result_detail_file_name = result_file_name + ".details.csv"
    date2tradeinfo = {} #date(%Y/%m/%d): (tag: (trade_cnt, open_mbox_cnt))
    date = start_date
    while (date < end_date):
        date_str = date.strftime("%Y/%m/%d")
        date2tradeinfo[date_str] = {}
        for tag in tags:
            date2tradeinfo[date_str][tag] = [0, 0]
        date = date + datetime.timedelta(days=1)
    
    solders_dict = {}
    buyers_dict = {} 
    traderesult_dict = {} # (tag: [total_cnt, [price_list]])
    if len(tradeprice_dict) > 0:
        for tag in tags:
            traderesult_dict[tag] = [0, []]

    trans_list = get_current_top10000_trans(contract_addr, start_date)
    with open(result_detail_file_name, "w", encoding="utf-8-sig") as details:
        target_row_cnt = 0
        for (trans_hash, trans_date_str) in trans_list:
            trans_date = datetime.datetime.strptime(trans_date_str, "%Y/%m/%d %H:%M:%S")
            trans_date_short_str = trans_date.strftime("%Y/%m/%d")
            if (trans_date < start_date) or (trans_date > end_date):
                continue

            trans_data = c.cfx.getTransactionByHash(trans_hash)
            (from_addr, to_addr, token_id) = get_transinfo_from_data(trans_data, contra)
            if (from_addr == None) or (to_addr == None):
                # 说明不是transfer交易，忽略
                continue
            tag = get_tag_from_tokenid(token_id, ranges,tags)
            if not tag:
                continue
            if to_addr == Taopai_Conflux_Address:
                # to address 如果是淘派的地址，说明是合成或回收行为，不计入统计
                details.write("{},{},{},合成或回收,{},{}\n".format(from_addr, to_addr, trans_date_str, tag, token_id))
                continue
            if from_addr == Taopai_Conflux_Address:
                # from address 如果是淘派的地址，说明是打开盲盒或者空投
                date2tradeinfo[trans_date_short_str][tag][1] += 1
                details.write("{},{},{},开盲盒或空投或合成,{},{}\n".format(from_addr, to_addr, trans_date_str, tag, token_id))
            else:
                # 持有者之间的交易
                date2tradeinfo[trans_date_short_str][tag][0] += 1
                
                # 更新交易价格信息
                if len(tradeprice_dict) > 0:
                    traderesult_dict[tag][0] += 1
                    trade_price = "未知"
                    if (token_id in tradeprice_dict) and (len(tradeprice_dict[token_id]) == 1):
                        trade_price = tradeprice_dict[token_id][0]
                        traderesult_dict[tag][1].append(trade_price)
                    details.write("{},{},{},交易,{},{},{}\n".format(
                        from_addr, to_addr, trans_date_str, tag, token_id, trade_price)) 
                else:
                    details.write("{},{},{},交易,{},{}\n".format(
                        from_addr, to_addr, trans_date_str, tag, token_id))  

                # 更新卖方信息
                if from_addr not in solders_dict:
                    solders_dict[from_addr] = [0, {}]
                    for t in tags:
                        solders_dict[from_addr][1][t] = 0
                solders_dict[from_addr][0] += 1
                solders_dict[from_addr][1][tag] += 1

                # 更新买方信息
                if to_addr not in buyers_dict:
                    buyers_dict[to_addr] = [0, {}]
                    for t in tags:
                        buyers_dict[to_addr][1][t] = 0
                buyers_dict[to_addr][0] += 1
                buyers_dict[to_addr][1][tag] += 1

            target_row_cnt += 1

            # wait for some time for HTTP 429 error
            time.sleep(0.2)
    
    if verbose:
        print("{} target transaction records found.".format(target_row_cnt))

    # 由于tags指定时可以重复，对应不同的id区间（见佛系熊猫二期的常规款），输出时tags需要去重
    nodup_tags = []
    for tag in tags:
        if tag not in nodup_tags:
            nodup_tags.append(tag)
    tags = nodup_tags

    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        # 写入交易的数量
        result_file.write("日期,{}\n".format(",".join(tags)))
        for td_str in date2tradeinfo:
            result_file.write("{},{}\n".format(
                td_str, ",".join([str(date2tradeinfo[td_str][tag][0]) for tag in tags])
            ))
        
        # 写入打开盲盒的数量
        result_file.write("日期,{}\n".format(",".join(tags)))
        for td_str in date2tradeinfo:
            result_file.write("{},{}\n".format(
                td_str, ",".join([str(date2tradeinfo[td_str][tag][1]) for tag in tags])
            ))
    
    # 交易价格汇总数据
    if len(traderesult_dict) > 0:
        trade_agg_file_name = result_file_name + ".tradeagg.csv"
        with open(trade_agg_file_name, "w", encoding="utf-8-sig") as trade_agg_file:
            trade_agg_file.write(",交易总量,价格获得量,成交均值,成交最小价格,成交最大价格\n")
            for tag in tags:
                plist = traderesult_dict[tag][1]
                if len(plist) > 0:
                    trade_agg_file.write("{},{},{},{},{},{}\n".format(
                        tag, traderesult_dict[tag][0], len(plist),
                        sum(plist) / len(plist), min(plist), max(plist)
                    ))
                else:
                    trade_agg_file.write("{},{},{},{},{},{}\n".format(
                        tag, traderesult_dict[tag][0], len(plist),
                        "未知", "未知", "未知"
                    ))

    # 卖方数据
    solders_detail_file_name = result_file_name + ".solders.csv"
    solders_info = []
    for s in solders_dict:
        sinfo = [s, solders_dict[s][0]]
        for t in tags:
            sinfo.append(solders_dict[s][1][t])
        solders_info.append(sinfo)
    solders_info.sort(key=lambda s: s[1], reverse=True)
    with open(solders_detail_file_name, "w", encoding="utf-8-sig") as solders_detail_file:
        solders_detail_file.write("账户,卖出总量,{}\n".format(','.join(tags)))
        for solder_info in solders_info:
            solders_detail_file.write("{},{},{}\n".format(
                blur_address(solder_info[0]),
                ','.join([str(s) for s in solder_info[1:]]),
                solder_info[0]))

    # 买方数据
    buyers_detail_file_name = result_file_name + ".buyers.csv"
    buyers_info = []
    for b in buyers_dict:
        binfo = [b, buyers_dict[b][0]]
        for t in tags:
            binfo.append(buyers_dict[b][1][t])
        buyers_info.append(binfo)
    buyers_info.sort(key=lambda b: b[1], reverse=True)
    with open(buyers_detail_file_name, "w", encoding="utf-8-sig") as buyers_detail_file:
        buyers_detail_file.write("账户,买入总量,{}\n".format(','.join(tags)))
        for buyer_info in buyers_info:
            buyers_detail_file.write("{},{},{}\n".format(
                blur_address(buyer_info[0]),
                ','.join([str(s) for s in buyer_info[1:]]),
                buyer_info[0]))

def multi_analyze_transaction_logs_hourly_online(contract_addr, contract_ABI, date_str, hour_str, ranges, tags, result_file_name,  verbose=True):
    '''
    分析当天零点开始到输入的小时结束的交易
    [date_str 0:0:0, datestr hour_str:59:59]
    '''
    provider = HTTPProvider('https://main.confluxrpc.com')
    c =  Conflux(provider)
    contra = c.contract(contract_addr, contract_ABI)
    start_time = datetime.datetime.strptime(date_str + " 0:0:0", "%Y/%m/%d %H:%M:%S")
    end_time = datetime.datetime.strptime(date_str + " {}:59:59".format(hour_str), "%Y/%m/%d %H:%M:%S")
    
    result_detail_file_name = result_file_name + ".details.csv"
    tradeinfo = {} #tag: (trade_cnt, open_mbox_cnt)
    for tag in tags:
        tradeinfo[tag] = [0, 0]
    
    solders_dict = {}
    buyers_dict = {} 

    trans_list = get_current_top10000_trans(contract_addr, start_time)
    with open(result_detail_file_name, "w", encoding="utf-8-sig") as details:
        target_row_cnt = 0
        for (trans_hash, trans_time_str) in trans_list:
            trans_time = datetime.datetime.strptime(trans_time_str, "%Y/%m/%d %H:%M:%S")
            if (trans_time < start_time) or (trans_time > end_time):
                continue

            trans_data = c.cfx.getTransactionByHash(trans_hash)
            (from_addr, to_addr, token_id) = get_transinfo_from_data(trans_data, contra)
            if (from_addr == None) or (to_addr == None):
                # 说明不是transfer交易，忽略
                continue
            tag = get_tag_from_tokenid(token_id, ranges,tags)
            if not tag:
                continue
            if to_addr == Taopai_Conflux_Address:
                # to address 如果是淘派的地址，说明是合成或回收行为，不计入统计
                details.write("{},{},{},合成或回收,{},{}\n".format(from_addr, to_addr, trans_time_str, tag, token_id))
                continue
            if from_addr == Taopai_Conflux_Address:
                # from address 如果是淘派的地址，说明是打开盲盒或者空投
                tradeinfo[tag][1] += 1
                details.write("{},{},{},开盲盒或空投或合成,{},{}\n".format(from_addr, to_addr, trans_time_str, tag, token_id))
            else:
                # 持有者之间的交易
                tradeinfo[tag][0] += 1
                details.write("{},{},{},交易,{},{}\n".format(
                    from_addr, to_addr, trans_time_str, tag, token_id))  

                # 更新卖方信息
                if from_addr not in solders_dict:
                    solders_dict[from_addr] = [0, {}]
                    for t in tags:
                        solders_dict[from_addr][1][t] = 0
                solders_dict[from_addr][0] += 1
                solders_dict[from_addr][1][tag] += 1

                # 更新买方信息
                if to_addr not in buyers_dict:
                    buyers_dict[to_addr] = [0, {}]
                    for t in tags:
                        buyers_dict[to_addr][1][t] = 0
                buyers_dict[to_addr][0] += 1
                buyers_dict[to_addr][1][tag] += 1

            target_row_cnt += 1

            # wait for some time for HTTP 429 error
            time.sleep(0.2)
    
    if verbose:
        print("{} target transaction records found.".format(target_row_cnt))

    # 由于tags指定时可以重复，对应不同的id区间（见佛系熊猫二期的常规款），输出时tags需要去重
    nodup_tags = []
    for tag in tags:
        if tag not in nodup_tags:
            nodup_tags.append(tag)
    tags = nodup_tags

    with open(result_file_name, "w", encoding="utf-8-sig") as result_file:
        # 写入交易的数量
        result_file.write("{}\n".format(",".join(tags)))
        result_file.write("{}\n".format(
            ",".join([str(tradeinfo[tag][0]) for tag in tags])
        ))
        
        # 写入打开盲盒的数量
        result_file.write("{}\n".format(",".join(tags)))
        result_file.write("{}\n".format(
            ",".join([str(tradeinfo[tag][1]) for tag in tags])
        ))

    # 卖方数据
    solders_detail_file_name = result_file_name + ".solders.csv"
    solders_info = []
    for s in solders_dict:
        sinfo = [s, solders_dict[s][0]]
        for t in tags:
            sinfo.append(solders_dict[s][1][t])
        solders_info.append(sinfo)
    solders_info.sort(key=lambda s: s[1], reverse=True)
    with open(solders_detail_file_name, "w", encoding="utf-8-sig") as solders_detail_file:
        solders_detail_file.write("账户,卖出总量,{}\n".format(','.join(tags)))
        for solder_info in solders_info:
            solders_detail_file.write("{},{},{}\n".format(
                blur_address(solder_info[0]),
                ','.join([str(s) for s in solder_info[1:]]),
                solder_info[0]))

    # 买方数据
    buyers_detail_file_name = result_file_name + ".buyers.csv"
    buyers_info = []
    for b in buyers_dict:
        binfo = [b, buyers_dict[b][0]]
        for t in tags:
            binfo.append(buyers_dict[b][1][t])
        buyers_info.append(binfo)
    buyers_info.sort(key=lambda b: b[1], reverse=True)
    with open(buyers_detail_file_name, "w", encoding="utf-8-sig") as buyers_detail_file:
        buyers_detail_file.write("账户,买入总量,{}\n".format(','.join(tags)))
        for buyer_info in buyers_info:
            buyers_detail_file.write("{},{},{}\n".format(
                blur_address(buyer_info[0]),
                ','.join([str(s) for s in buyer_info[1:]]),
                buyer_info[0]))