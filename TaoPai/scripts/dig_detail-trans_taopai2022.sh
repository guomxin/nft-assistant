# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py taopai2022 $1

# 2. dig info for ANY
python diginfo_from_details_conflux.py taopai2022 1 data/_details_conflux_taopai2022_result_$1.csv 30001 32022 ANY $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py taopai2022 2 data/_details_conflux_taopai2022_result_$1.csv 20001,24823 1 ALL $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py taopai2022 3 data/_details_conflux_taopai2022_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py taopai2022 $2 $3 30001,32022 ANY $1

cd scripts
