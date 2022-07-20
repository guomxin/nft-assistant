# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py partycat $1

# 2. dig info for SHOUFA
python diginfo_from_details_conflux.py partycat 1 data/_details_conflux_partycat_result_$1.csv \
901,3838 GONGYOU $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py partycat 2 data/_details_conflux_partycat_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py partycat 3 data/_details_conflux_partycat_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py partycat $2 $3 \
901,3838 \
GONGYOU $1

cd scripts
