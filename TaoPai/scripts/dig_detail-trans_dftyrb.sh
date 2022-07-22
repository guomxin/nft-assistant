# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py dftyrb $1

# 2. dig info for ANY
python diginfo_from_details_conflux.py dftyrb 1 data/_details_conflux_dftyrb_result_$1.csv \
1,8000 ANY $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py dftyrb 2 data/_details_conflux_dftyrb_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py dftyrb 3 data/_details_conflux_dftyrb_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py dftyrb $2 $3 \
1,8000 \
ANY $1

cd scripts
