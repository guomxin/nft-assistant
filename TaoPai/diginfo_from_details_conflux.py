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
        
        #min_tids = [int(n) for n in sys.argv[4].split(",")]
        #max_tids = [int(n) for n in sys.argv[5].split(",")]

        ranges_str = sys.argv[4]
        min_counts_str = sys.argv[5]
        dig_tag = sys.argv[6]
        detail_tag = sys.argv[7]
        dump_file_name = "data/_dig_fullsetinfo_conflux_{}_{}_result_{}.csv".format(
            nft_name, dig_tag, detail_tag)

        min_counts = [int(s.strip()) for s in min_counts_str.split(";")]
        ranges = [[int(item) for item in range_str.split(",")] for range_str in ranges_str.split(";")]
        detaildigger.dig_fullsetinfo_from_details_multi_adv(nft_name, details_file_name, ranges, min_counts, dump_file_name)
        #detaildigger.dig_fullsetinfo_from_details_multi(nft_name, details_file_name, ranges, min_counts, dump_file_name)
        #detaildigger.dig_fullsetinfo_from_details(nft_name, details_file_name, min_tids, max_tids, dump_file_name)
    elif func_id == 3:
        # stat nft count in circulation
        details_file_name = sys.argv[3]
        detail_tag = sys.argv[4]
        dump_file_name = "data/_scan_conflux_{}_result_{}.csv".format(
            nft_name, detail_tag)
        detaildigger.dig_circulation_from_details(nft_name, details_file_name, dump_file_name)
        