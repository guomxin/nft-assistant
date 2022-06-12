# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py guizi $1

# 2. dig info for SR&N
python diginfo_from_details_conflux.py guizi 1 data/_details_conflux_guizi_result_$1.csv 1 1000 GUIZI-SR $1
python diginfo_from_details_conflux.py guizi 1 data/_details_conflux_guizi_result_$1.csv 1001 4000 GUIZI-N $1

# 3. dig count in circulation
python diginfo_from_details_conflux.py guizi 3 data/_details_conflux_guizi_result_$1.csv $1

# 4. analyze tranctions
python transaction_conflux_contract_online.py guizi $2 $3 1,1000\;1001,4000 GUIZI-SR\;GUIZI-N $1

cd scripts
