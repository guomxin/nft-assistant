# coding: utf-8
import os, sys
# add python path of tpcommon's parent path to sys.path
parent_path = os.path.abspath(os.path.join(__file__, *([".."]*2)))
if parent_path not in sys.path:
    sys.path.append(parent_path)

from tpcommon import idrange

def blur_address(address):
    return address[:10] + "****" + address[-4:]

def token_id_in_ranges(token_id, ranges):
    for (min_tid, max_tid) in ranges:
        if (token_id >= min_tid) and (token_id <= max_tid):
            return True
    return False

def dig_a_nftinfo_from_details_adv(details_file_name, ranges, dump_file_name):
    owner2tidcnt = {}
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        tokenids = [int(i) for i in items[2].split(":")]
        target_tid_cnt = 0
        for tid in tokenids:
            if token_id_in_ranges(tid, ranges):
                target_tid_cnt += 1
        if target_tid_cnt > 0:
            owner2tidcnt[owner] = target_tid_cnt
    
    # sort the info
    owner_tidcnt_list = []
    for (owner, tidcnt) in owner2tidcnt.items():
        owner_tidcnt_list.append((owner, tidcnt))
    owner_tidcnt_list.sort(key=lambda p: p[1], reverse=True)

    dump_file = open(dump_file_name, "w")
    for (owner, tidcnt) in owner_tidcnt_list:
        dump_file.write("{},{},{}\n".format(blur_address(owner), tidcnt, owner))
    dump_file.close()

def dig_a_nftinfo_from_details(details_file_name, min_tid, max_tid, dump_file_name):
    owner2tidcnt = {}
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        tokenids = [int(i) for i in items[2].split(":")]
        target_tid_cnt = 0
        for tid in tokenids:
            if (tid >= min_tid) and (tid <= max_tid):
                target_tid_cnt += 1
        if target_tid_cnt > 0:
            owner2tidcnt[owner] = target_tid_cnt
    
    # sort the info
    owner_tidcnt_list = []
    for (owner, tidcnt) in owner2tidcnt.items():
        owner_tidcnt_list.append((owner, tidcnt))
    owner_tidcnt_list.sort(key=lambda p: p[1], reverse=True)

    dump_file = open(dump_file_name, "w")
    for (owner, tidcnt) in owner_tidcnt_list:
        dump_file.write("{},{},{}\n".format(blur_address(owner), tidcnt, owner))
    dump_file.close()

def get_range_index(low, high, ranges):
    for i in range(len(ranges)):
        min_tid = ranges[i][0]
        max_tid = ranges[i][1]
        if (low >= min_tid) and (high <= max_tid):
            return i
    return None

def dig_fullsetinfo_from_details_multi_adv(nft_name, details_file_name, ranges, min_counts, dump_file_name):
    owner2fullsetinfo = {}
    idrange2name = idrange.get_idrangedict_by_nftname(nft_name)
    
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        
        # initialize owner values
        owner2fullsetinfo[owner] = {}
        for ((t1, t2), name) in idrange2name.items():
            range_index = get_range_index(t1, t2, ranges)
            if range_index == None:
                continue
            owner2fullsetinfo[owner][name] = 0

        tokenids = [int(i) for i in items[2].split(":")]
        for tid in tokenids:
            range_index = get_range_index(tid, tid, ranges)
            if range_index == None:
                continue
            name = idrange.get_name_by_tokenid(idrange2name, tid)
            if name in owner2fullsetinfo[owner]:
                owner2fullsetinfo[owner][name] += 1
    
    name2mincounts = {}
    for ((t1, t2), name) in idrange2name.items():
        range_index = get_range_index(t1, t2, ranges)
        if range_index == None:
            continue

        # 如果min_counts长度少于ranges，最后一个min_count重复
        if range_index >= len(min_counts):
            range_index = len(min_counts) - 1
        
        if name in name2mincounts:
            assert name2mincounts[name] == min_counts[range_index], "{} min counts inconsistent!".format(name)
        name2mincounts[name] = min_counts[range_index]


    # calculate owner's full-set count
    owner2fullsetcnt = {}
    for (owner, fsinfos) in owner2fullsetinfo.items():
        min_factor = -1
        for (name, cnt) in fsinfos.items():
            factor = cnt // name2mincounts[name]
            if min_factor == -1:
                min_factor = factor
            elif factor < min_factor:
                min_factor = factor
        owner2fullsetcnt[owner] = min_factor
    
    # sort the info
    owner_fullsetcnt_list = []
    for (owner, fullset_cnt) in owner2fullsetcnt.items():
        owner_fullsetcnt_list.append((owner, fullset_cnt))
    owner_fullsetcnt_list.sort(key=lambda p: p[1], reverse=True)

    dump_file = open(dump_file_name, "w")
    for (owner, fullset_cnt) in owner_fullsetcnt_list:
        if fullset_cnt > 0:
            dump_file.write("{},{},{}\n".format(blur_address(owner), fullset_cnt, owner))
    dump_file.close()

def dig_fullsetinfo_from_details_multi(nft_name, details_file_name, ranges, min_counts, dump_file_name):
    owner2fullsetinfo = {}
    idrange2name = idrange.get_idrangedict_by_nftname(nft_name)
    
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        
        # initialize owner values
        owner2fullsetinfo[owner] = []
        for i in range(len(ranges)):
            owner2fullsetinfo[owner].append({})
        for ((t1, t2), name) in idrange2name.items():
            range_index = get_range_index(t1, t2, ranges)
            if range_index == None:
                continue
            owner2fullsetinfo[owner][range_index][name] = 0

        tokenids = [int(i) for i in items[2].split(":")]
        for tid in tokenids:
            range_index = get_range_index(tid, tid, ranges)
            if range_index == None:
                continue
            name = idrange.get_name_by_tokenid(idrange2name, tid)
            if name in owner2fullsetinfo[owner][range_index]:
                owner2fullsetinfo[owner][range_index][name] += 1
    
    # calculate owner's full-set count
    owner2fullsetcnt = {}
    for (owner, fsinfos) in owner2fullsetinfo.items():
        min_factor = -1
        for range_index in range(len(fsinfos)):
            min_cnt = -1
            for (name, cnt) in fsinfos[range_index].items():
                if min_cnt == -1:
                    min_cnt = cnt
                elif cnt < min_cnt:
                    min_cnt = cnt
            factor = min_cnt // min_counts[range_index]
            if min_factor == -1:
                min_factor = factor
            elif factor < min_factor:
                min_factor = factor
        owner2fullsetcnt[owner] = min_factor
    
    # sort the info
    owner_fullsetcnt_list = []
    for (owner, fullset_cnt) in owner2fullsetcnt.items():
        owner_fullsetcnt_list.append((owner, fullset_cnt))
    owner_fullsetcnt_list.sort(key=lambda p: p[1], reverse=True)

    dump_file = open(dump_file_name, "w")
    for (owner, fullset_cnt) in owner_fullsetcnt_list:
        if fullset_cnt > 0:
            dump_file.write("{},{},{}\n".format(blur_address(owner), fullset_cnt, owner))
    dump_file.close()

def is_range_in_rangelist(low, high, min_tids, max_tids):
    for i in range(len(min_tids)):
        min_tid = min_tids[i]
        max_tid = max_tids[i]
        if (low >= min_tid) and (high <= max_tid):
            return True
    return False

def dig_fullsetinfo_from_details(nft_name, details_file_name, min_tids, max_tids, dump_file_name):
    owner2fullsetinfo = {}
    idrange2name = idrange.get_idrangedict_by_nftname(nft_name)
    
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        
        # initialize owner values
        owner2fullsetinfo[owner] = {}
        for ((t1, t2), name) in idrange2name.items():
            if is_range_in_rangelist(t1, t2, min_tids, max_tids):
                owner2fullsetinfo[owner][name] = 0

        tokenids = [int(i) for i in items[2].split(":")]
        for tid in tokenids:
            name = idrange.get_name_by_tokenid(idrange2name, tid)
            if name in owner2fullsetinfo[owner]:
                owner2fullsetinfo[owner][name] += 1
    
    # calculate owner's full-set count
    owner2fullsetcnt = {}
    for (owner, fsinfo) in owner2fullsetinfo.items():
        min_cnt = -1
        for (name, cnt) in fsinfo.items():
            if min_cnt == -1:
                min_cnt = cnt
            elif cnt < min_cnt:
                min_cnt = cnt
        owner2fullsetcnt[owner] = min_cnt
    
    # sort the info
    owner_fullsetcnt_list = []
    for (owner, fullset_cnt) in owner2fullsetcnt.items():
        owner_fullsetcnt_list.append((owner, fullset_cnt))
    owner_fullsetcnt_list.sort(key=lambda p: p[1], reverse=True)

    dump_file = open(dump_file_name, "w")
    for (owner, fullset_cnt) in owner_fullsetcnt_list:
        if fullset_cnt > 0:
            dump_file.write("{},{},{}\n".format(blur_address(owner), fullset_cnt, owner))
    dump_file.close()

Taopai_Conflux_Address = "cfx:aapwjebcay7d6jv02whjrrvkm9egmw5fye09cea6zz"
Taopai_Prev_Conflux_Address = "cfx:aam2cnrarzburf6sspm6jg6eznbwht8uj6hf4jg8f2"
Taopai_Recycle_Conflux_Address = "cfx:aapj481b9pmg8ppnwcpnskpzym1hddfbtupnhth2ac" # 淘派回收账号(比如多发行的乐淘淘-小满)

Taopai_FXHE_Conflux_Address = "cfx:aakrxdm1crf40xt7d9yutbxycghvsbm88680kkymdu"
Taopai_FXHE_Conflux_Address_2 = "cfx:aanh0x2uyf7j6gdftz3m4cvze8b93chzx6vk17bzy3"
Taopai_FXHE_Conflux_Address_3 = "cfx:aajsd02wfexpj4r3t6httyn6ycujyfgzy6cuxbn4tz"

def dig_circulation_from_details(nft_name, details_file_name, dump_file_name):
    idrange2name = idrange.get_idrangedict_by_nftname(nft_name)
    circulation_dict = {} # name->count
    for (_, name) in idrange2name.items():
        circulation_dict[name] = 0
    
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        if (owner == Taopai_Conflux_Address) or (owner == Taopai_Prev_Conflux_Address) or (owner == Taopai_Recycle_Conflux_Address):
            # negelect Taopai account
            continue
        #if (nft_name == "partycat") or  (nft_name == "fxxunzhang") or (nft_name == "fxfuneng") \
        #    or (nft_name == "fxpanda") or (nft_name == "fxpanda2") or (nft_name == "fxpandaall"):
        #    if owner == Taopai_FXHE_Conflux_Address or owner == Taopai_FXHE_Conflux_Address_2 \
        #        or owner == Taopai_FXHE_Conflux_Address_3:
        #        # neglect FXHE acccount
        #        continue
        tokenids = [int(i) for i in items[2].split(":")]
        for tid in tokenids:
            name = idrange.get_name_by_tokenid(idrange2name, tid)
            if name not in circulation_dict:
                circulation_dict[name] = 0
            circulation_dict[name] += 1
    
    dump_file = open(dump_file_name, "w", encoding="utf-8-sig")
    for (fig, cnt) in circulation_dict.items():
        dump_file.write("{},{}\n".format(fig, cnt))
    dump_file.close()