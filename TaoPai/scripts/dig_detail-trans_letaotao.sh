# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py letaotao $1

# 2. dig info for ANY
python diginfo_from_details_conflux.py letaotao 1 data/_details_conflux_letaotao_result_$1.csv 50001 52239 ANY $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py letaotao 2 data/_details_conflux_letaotao_result_$1.csv 10001,20127 1 ALL $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py letaotao 3 data/_details_conflux_letaotao_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py letaotao $2 $3 50001,51496\;51636,52239 PART1\;PART2 $1

cd scripts
