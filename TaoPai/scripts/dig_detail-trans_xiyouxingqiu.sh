# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py xiyouxingqiu $1

# 2. dig info for PUTONG&XIANLIANG
python diginfo_from_details_conflux.py xiyouxingqiu 1 data/_details_conflux_xiyouxingqiu_result_$1.csv \
1,4100\;4201,5020 PUTONG $1
python diginfo_from_details_conflux.py xiyouxingqiu 1 data/_details_conflux_xiyouxingqiu_result_$1.csv \
4101,4200 XIANLIANG $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py xiyouxingqiu 2 data/_details_conflux_xiyouxingqiu_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py xiyouxingqiu 3 data/_details_conflux_xiyouxingqiu_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py xiyouxingqiu $2 $3 \
1,4100\;4201,5020\;4101,4200 \
PUTONG\;PUTONG\;XIANLIANG $1

cd scripts
