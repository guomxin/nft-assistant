# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py partycategg $1

# 2. dig info for XingJiDan, JinDan, CaiDan, YuanQiDan
python diginfo_from_details_conflux.py partycategg 1 data/_details_conflux_partycategg_result_$1.csv \
10483,10483\;10890,10896\;11079,11260 XingJiDan $1
python diginfo_from_details_conflux.py partycategg 1 data/_details_conflux_partycategg_result_$1.csv \
10433,10433\;10624,10889\;10897,11078 JinDan $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py partycategg 2 data/_details_conflux_partycategg_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py partycategg 3 data/_details_conflux_partycategg_result_$1.csv $1

# 5. analyze tranctions
# python transaction_conflux_contract_online.py partycategg $2 $3 \
# 901,3838 \
# GONGYOU $1

cd scripts
