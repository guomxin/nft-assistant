# coding: utf-8
from heapq import merge
import sys

def blur_address(address):
    return address[:10] + "****" + address[-4:]

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("{} <nft_name> <result_tag> <fullset_tags>".format(sys.argv[0]))
        sys.exit(1)

    nft_name = sys.argv[1]
    result_tag = sys.argv[2]
    fullset_tags = sys.argv[3].split(";")

    # merge full set infos
    merged_result = {}
    for fullset_tag in fullset_tags:
        fullset_file_name = "data/_dig_fullsetinfo_conflux_{}_{}_result_{}.csv".format(
            nft_name, fullset_tag, result_tag)
        for line in open(fullset_file_name):
            items = line.strip().split(",")
            account = items[2]
            cnt = int(items[1])
            if account not in merged_result:
                merged_result[account] = cnt
            if cnt > merged_result[account]:
                merged_result[account] = cnt
    
    # sort and output
    merged_fullset_file_name = "data/_dig_fullsetinfo_conflux_{}_merged_result_{}.csv".format(
            nft_name,  result_tag)
    merged_fullset_file = open(merged_fullset_file_name, "w")
    for (account,cnt) in sorted(list(merged_result.items()), key=lambda i:i[1], reverse=True):
        merged_fullset_file.write("{},{},{}\n".format(
            blur_address(account), cnt, account
        ))
    merged_fullset_file.close()