# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py kaozaikaituo $1

# 2. dig info for SSR&SR
python diginfo_from_details_conflux.py kaozaikaituo 1 data/_details_conflux_kaozaikaituo_result_$1.csv 15001 17500  ANY $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py kaozaikaituo 2 data/_details_conflux_kaozaikaituo_result_$1.csv 501,3000\;3001,10000 3\;6 FRAGMENT $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py kaozaikaituo 3 data/_details_conflux_kaozaikaituo_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py kaozaikaituo $2 $3 15001,15500\;15501,16000\;16001,16500\;16501,17000\;17001,17500 \
ZHENCHA\;CHONGFENG\;YISHI\;ZHIHUIGUAN\;MENGSHI $1

cd scripts