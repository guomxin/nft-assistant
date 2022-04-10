# coding: utf-8

import sys

from tpcommon import detaildigger

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <nft_name> <function_id>(1:dig_a_nft_info)".format(sys.argv[0]))
        sys.exit(1)
    nft_name = sys.argv[1]
    func_id = int(sys.argv[2])
    if func_id == 1:
        # dig_a_nftinfo_from_details
        details_file_name = sys.argv[3]
        min_tid = int(sys.argv[4])
        max_tid = int(sys.argv[5])
        dig_tag = sys.argv[6]
        detail_tag = sys.argv[7]
        dump_file_name = "data/_dig_a_nftinfo_conflux_{}_{}_result_{}.csv".format(
            nft_name, dig_tag, detail_tag)
        detaildigger.dig_a_nftinfo_from_details(details_file_name, min_tid, max_tid, dump_file_name)
    elif func_id == 2:
        # dig fullset info from details
        details_file_name = sys.argv[3]
        min_tid = int(sys.argv[4])
        max_tid = int(sys.argv[5])
        dig_tag = sys.argv[6]
        detail_tag = sys.argv[7]
        dump_file_name = "data/_dig_fullsetinfo_conflux_{}_{}_result_{}.csv".format(
            nft_name, dig_tag, detail_tag)
        detaildigger.dig_fullsetinfo_from_details(nft_name, details_file_name, min_tid, max_tid, dump_file_name)
        