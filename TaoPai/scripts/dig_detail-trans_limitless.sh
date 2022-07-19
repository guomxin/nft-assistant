# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py limitless $1

# 2. dig info for ANY, SSR
python diginfo_from_details_conflux.py limitless 1 data/_details_conflux_limitless_result_$1.csv \
1,7000 ANY $1
python diginfo_from_details_conflux.py limitless 1 data/_details_conflux_limitless_result_$1.csv 1,500 SSR $1
python diginfo_from_details_conflux.py limitless 1 data/_details_conflux_limitless_result_$1.csv 10001,10050 SP $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py limitless 2 data/_details_conflux_limitless_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py limitless 3 data/_details_conflux_limitless_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py limitless $2 $3 \
1,500\;501,2500\;2501,7000\;10001,10050 \
SSR\;SR\;R\;SP $1

cd scripts
