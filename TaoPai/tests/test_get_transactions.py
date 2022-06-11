# coding: utf-8

import os, sys
# add python path of tpcommon's parent path to sys.path
parent_path = os.path.abspath(os.path.join(__file__, *([".."]*2)))
if parent_path not in sys.path:
    sys.path.append(parent_path)


from tpcommon import trans
from tpcommon import contract

if __name__ == "__main__":
    trans = trans.get_current_top10000_trans(contract.TaopaiNFT_Contract_Address)
    print(trans[:10])