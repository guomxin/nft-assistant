# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py bobosg $1

# 2. dig info for ANY, CONGMING, HANYONG
python diginfo_from_details_conflux.py bobosg 1 data/_details_conflux_bobosg_result_$1.csv \
1,1800\;4001,5800\;8001,9800\;12001,12720\;16001,16360 ANY $1
#python diginfo_from_details_conflux.py bobosg 1 data/_details_conflux_bobosg_result_$1.csv 12001,12720  CAOCAO $1
python diginfo_from_details_conflux.py bobosg 1 data/_details_conflux_bobosg_result_$1.csv 16001,16360  ZHUGELIANG $1
python diginfo_from_details_conflux.py bobosg 1 data/_details_conflux_bobosg_result_$1.csv 17001,17600  TAOYUANJIEYI $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py bobosg 2 data/_details_conflux_bobosg_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py bobosg 3 data/_details_conflux_bobosg_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py bobosg $2 $3 \
1,1800\;4001,5800\;8001,9800\;12001,12720\;16001,16360\;14001,14720\;17001,17600 \
LVBU\;ZHANGFEI\;GUANYU\;CAOCAO\;ZHUGELIANG\;LIUBEI\;TAOYUANJIEYI $1

cd scripts
