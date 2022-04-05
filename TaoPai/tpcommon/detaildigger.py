# coding: utf-8

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
        dump_file.write("{},{}\n".format(owner, tidcnt))
    dump_file.close()