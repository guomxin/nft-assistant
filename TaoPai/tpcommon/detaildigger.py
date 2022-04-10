# coding: utf-8
from tpcommon import idrange

def blur_address(address):
    return address[:10] + "****" + address[-4:]

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

def dig_fullsetinfo_from_details(nft_name, details_file_name, min_tid, max_tid, dump_file_name):
    owner2fullsetinfo = {}
    idrange2name = idrange.get_idrangedict_by_nftname(nft_name)
    
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        
        # initialize owner values
        owner2fullsetinfo[owner] = {}
        for ((t1, t2), name) in idrange2name.items():
            if (t1 >= min_tid) and (t2 <= max_tid):
                owner2fullsetinfo[owner][name] = 0

        tokenids = [int(i) for i in items[2].split(":")]
        for tid in tokenids:
            if (tid >= min_tid) and (tid <= max_tid):
                name = idrange.get_name_by_tokenid(idrange2name, tid)
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