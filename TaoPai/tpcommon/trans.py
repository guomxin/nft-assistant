# coding: utf-8
from conflux import (
    Conflux,
    HTTPProvider
)
import csv
import datetime

from tpcommon import contract

Taopai_Conflux_Address = "cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz"

TransHashIndex = 3
TransDateIndex = 9

def get_transinfo_from_data(trans_data, contra):
    decode_result = contra.decode_function_input(trans_data.data)
    if ("from" not in decode_result[1]) or ("to" not in decode_result[1]) or ("tokenId" not in decode_result[1]):
        return (None, None, -1)
    from_addr = contract.get_base32addr_from_hexaddr(decode_result[1]["from"])
    to_addr = contract.get_base32addr_from_hexaddr(decode_result[1]["to"])
    token_id = decode_result[1]["tokenId"]

    return (from_addr, to_addr, token_id)

def analyze_transaction_logs(trans_file_name, contract_addr, contract_ABI, start_date_str, end_date_str, result_file_name, min_tid=-1, max_tid=-1, verbose=True):
    provider = HTTPProvider('https://main.confluxrpc.com')
    c =  Conflux(provider)
    contra = c.contract(contract_addr, contract_ABI)
    date2tradeinfo = {} #date(%Y/%m/%d): (trade_cnt, open_mbox_cnt)
    start_date = datetime.datetime.strptime(start_date_str + " 0:0", "%Y/%m/%d %H:%M")
    end_date = datetime.datetime.strptime(end_date_str + " 23:59", "%Y/%m/%d %H:%M")
    
    with open(trans_file_name) as f:
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
            if trans_date_short_str not in date2tradeinfo:
                date2tradeinfo[trans_date_short_str] = [0, 0]
            trans_data = c.cfx.getTransactionByHash(trans_hash)
            (from_addr, to_addr, token_id) = get_transinfo_from_data(trans_data, contra)
            if (min_tid != -1) and token_id < min_tid:
                continue
            if (max_tid != -1) and token_id > max_tid:
                continue
            #print(trans_hash, trans_date_short_str)
            if to_addr == Taopai_Conflux_Address:
                # to address 如果是淘派的地址，说明是合成行为，不计入统计
                continue
            if from_addr == Taopai_Conflux_Address:
                # from address 如果是淘派的地址，说明是打开盲盒或者空投
                date2tradeinfo[trans_date_short_str][1] += 1
            else:
                # 持有者之间的交易
                date2tradeinfo[trans_date_short_str][0] += 1
            target_row_cnt += 1
    
    if verbose:
        print("{} target transaction records found.".format(target_row_cnt))

    with open(result_file_name, "w") as result_file:
        for (td_str, (trade_cnt, open_mbox_cnt)) in date2tradeinfo.items():
            result_file.write("{},{},{}\n".format(
                td_str, trade_cnt, open_mbox_cnt
            ))

def get_tag_from_tokenid(token_id, ranges, tags):
    for tag_index in range(len(tags)):
        min_tid, max_tid = ranges[tag_index]
        if (min_tid != -1) and token_id < min_tid:
            continue
        if (max_tid != -1) and token_id > max_tid:
            continue
        return tags[tag_index]

def multi_analyze_transaction_logs(trans_file_name, contract_addr, contract_ABI, start_date_str, end_date_str, ranges, tags, result_file_name,  verbose=True):
    provider = HTTPProvider('https://main.confluxrpc.com')
    c =  Conflux(provider)
    contra = c.contract(contract_addr, contract_ABI)
    start_date = datetime.datetime.strptime(start_date_str + " 0:0", "%Y/%m/%d %H:%M")
    end_date = datetime.datetime.strptime(end_date_str + " 23:59", "%Y/%m/%d %H:%M")
    
    date2tradeinfo = {} #date(%Y/%m/%d): (tag: (trade_cnt, open_mbox_cnt))
    date = start_date
    while (date < end_date):
        date_str = date.strftime("%Y/%m/%d")
        date2tradeinfo[date_str] = {}
        for tag in tags:
            date2tradeinfo[date_str][tag] = [0, 0]
        date = date + datetime.timedelta(days=1)
    
    with open(trans_file_name) as f:
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
                # to address 如果是淘派的地址，说明是合成行为，不计入统计
                continue
            if from_addr == Taopai_Conflux_Address:
                # from address 如果是淘派的地址，说明是打开盲盒或者空投
                date2tradeinfo[trans_date_short_str][tag][1] += 1
            else:
                # 持有者之间的交易
                date2tradeinfo[trans_date_short_str][tag][0] += 1
            target_row_cnt += 1
    
    if verbose:
        print("{} target transaction records found.".format(target_row_cnt))

    with open(result_file_name, "w") as result_file:
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