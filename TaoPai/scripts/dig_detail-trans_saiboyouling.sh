# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py saiboyouling $1

# 2. dig info for ANY&&ZHENCANG
python diginfo_from_details_conflux.py saiboyouling 1 data/_details_conflux_saiboyouling_result_$1.csv 1 3000 ANY $1
python diginfo_from_details_conflux.py saiboyouling 1 data/_details_conflux_saiboyouling_result_$1.csv 2851 3000 ZHENCANG $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py saiboyouling 2 data/_details_conflux_saiboyouling_result_$1.csv 501,3000;3001,10000 3;6 FRAGMENT $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py saiboyouling 3 data/_details_conflux_saiboyouling_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py saiboyouling $2 $3 1,2850\;2851,3000 \
PUTONG\;ZHENCANG $1

cd scripts