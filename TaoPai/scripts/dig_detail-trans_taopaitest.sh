# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py taopaitest $1

# 2. dig info for NeiCe & GongCe
python diginfo_from_details_conflux.py taopaitest 1 data/_details_conflux_taopaitest_result_$1.csv 10001 10999 NEICE $1
python diginfo_from_details_conflux.py taopaitest 1 data/_details_conflux_taopaitest_result_$1.csv 20001 20127 GONGCE $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py taopaitest 2 data/_details_conflux_taopaitest_result_$1.csv 10001,20127 1 ALL $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py taopaitest 3 data/_details_conflux_taopaitest_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py taopaitest $2 $3 10001,10999\;20001,20127 NEICE\;GONGCE $1

cd scripts
