# coding: utf-8

import sys
from datetime import datetime

from tpcommon import detaildigger

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <function_id>(1:dig_a_nft_info)".format(sys.argv[0]))
        sys.exit(1)
    func_id = int(sys.argv[1])
    if func_id == 1:
        # dig_a_nftinfo_from_details
        details_file_name = sys.argv[2]
        min_tid = int(sys.argv[3])
        max_tid = int(sys.argv[4])
        dump_file_name = "data/_dig_a_nftinfo_conflux_atsj_result_{}.csv".format(
            datetime.strftime(datetime.now(), '%Y%m%d%H%M'))
        detaildigger.dig_a_nftinfo_from_details(details_file_name, min_tid, max_tid, dump_file_name)