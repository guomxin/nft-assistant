# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py pcatmem $1

# 2. dig info for SHOUFA
python diginfo_from_details_conflux.py pcatmem 1 data/_details_conflux_pcatmem_result_$1.csv \
12001,13001 SHOUFA $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py pcatmem 2 data/_details_conflux_pcatmem_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py pcatmem 3 data/_details_conflux_pcatmem_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py pcatmem $2 $3 \
12001,13001 \
SHOUFA $1

cd scripts
