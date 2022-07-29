# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py fxxunzhang $1

# 2. dig info CHUANGSHI
python diginfo_from_details_conflux.py fxxunzhang 1 data/_details_conflux_fxxunzhang_result_$1.csv \
11001,11103 FXCHUANGSHI $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py fxxunzhang 2 data/_details_conflux_fxxunzhang_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py fxxunzhang 3 data/_details_conflux_fxxunzhang_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py fxxunzhang $2 $3 \
40104,40206\;40207,40309\;40310,40517\;40518,40620\;40621,40688\;11001,11103 \
HUNIAN\;XIONGMAO\;QINGTONG\;BAIYIN\;HUANGJIN\;CHUANGSHI $1

cd scripts
