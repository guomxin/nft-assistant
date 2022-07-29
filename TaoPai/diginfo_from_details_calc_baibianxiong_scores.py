# coding: utf-8

import sys

from tpcommon import idrange

def blur_address(address):
    return address[:10] + "****" + address[-4:]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <details_file_name> <detail_tag>".format(sys.argv[0]))
        sys.exit(1)
    
    details_file_name = sys.argv[1]
    detail_tag = sys.argv[2]
    dump_file_name = "data/_calc_baibianxiong_scores_result_{}.csv".format(
        detail_tag)
        
    idrange2name = idrange.get_idrangedict_by_nftname("baibianxiong")
    owner_scores = []
    for line in open(details_file_name):
        items = line.split(",")
        owner = items[0].strip()
        count = int(items[1])
        
        score = 0
        tokenids = [int(i) for i in items[2].split(":")]
        for tid in tokenids:
            token_name = idrange.get_name_by_tokenid(idrange2name, 15+tid)
            if token_name == "SSR":
                score += 80
            elif token_name == "SR":
                score += 25
            elif token_name == "R":
                score += 3
            elif token_name == "N":
                score += 2
            elif token_name == "SSR-端午限定":
                score += 20
            elif token_name == "熊熊碎片":
                score += 3
            elif token_name == "SR-父亲节限定":
                score += 5
            elif token_name == "熊熊奶嘴":
                score += 50

        owner_scores.append((owner, count, score))
    
    owner_scores.sort(key=lambda p: p[2], reverse=True)
    dump_file = open(dump_file_name, "w", encoding="utf-8-sig")
    dump_file.write("地址,藏品数量,分数\n")
    for (owner, count, score) in owner_scores:
        dump_file.write("{},{},{},{}\n".format(blur_address(owner), count, score, owner))
    dump_file.close()