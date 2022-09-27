# coding: utf-8

from lib2to3.pgen2 import token
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
            token_name = idrange.get_name_by_tokenid(idrange2name, tid)
            if token_name == "SSR" or token_name == "SSR-变身计划":
                score += 80
            elif token_name == "SR" or token_name == "SR-变身计划":
                score += 25   
            elif token_name == "R":
                score += 3
            elif token_name == "N":
                score += 2
            elif token_name == "SSR-端午限定" or token_name == "SSR-熊熊铁军" or \
                token_name == "SSR-熊熊强者" or token_name == "SSR-中秋限定" or token_name == "SSR-荣耀王者":
                score += 20
            elif token_name == "熊熊碎片":
                score += 3
            elif token_name == "SR-父亲节限定" or token_name == "SR-七夕节限定" or \
                token_name == "SR-熊熊铁粉" or token_name == "SR-非洲土著" or token_name == "SR-荣耀战队" or \
                token_name == "SR-荣耀战队":
                score += 5
            elif token_name == "熊熊奶嘴":
                score += 50
            #elif token_name == "百变熊宝-金" or token_name == "百变熊宝-银" or token_name == "百变熊宝-铜" or \
            #    token_name == "百变熊宝-天选之子" or token_name == "百变熊宝-熊熊王者":
            elif token_name.startswith("百变熊宝"):
                score += 70
            elif token_name == "熊熊神像-青铜神像":
                score += 1
            elif token_name == "熊熊神像-白银神像":
                score += 2
            elif token_name == "熊熊神像-黄金神像":
                score += 5
            elif token_name == "熊熊神像-钻石神像":
                score += 20
            elif token_name == "熊熊蜜罐":
                pass
            elif token_name == "熊宝凭证":
                pass                        
            else:
                print("[calc_baibianxiong_scores]" + token_name)

        owner_scores.append((owner, count, score))
    
    owner_scores.sort(key=lambda p: p[2], reverse=True)
    dump_file = open(dump_file_name, "w", encoding="utf-8-sig")
    dump_file.write("地址,藏品数量,分数\n")
    for (owner, count, score) in owner_scores:
        dump_file.write("{},{},{},{}\n".format(blur_address(owner), count, score, owner))
    dump_file.close()