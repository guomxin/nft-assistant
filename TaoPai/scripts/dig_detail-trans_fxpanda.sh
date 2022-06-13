# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py fxpanda $1

# 2. dig info for XIYOU&CHUANSHUO&ANY
python diginfo_from_details_conflux.py fxpanda 1 data/_details_conflux_fxpanda_result_$1.csv 30001 35656 ANY $1
python diginfo_from_details_conflux.py fxpanda 1 data/_details_conflux_fxpanda_result_$1.csv 35041 35656 CHUANSHUO $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py fxpanda 2 data/_details_conflux_fxpanda_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py fxpanda 3 data/_details_conflux_fxpanda_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py fxpanda $2 $3 30001,33624\;33625,35040\;35041,35656 PUTONG\;XIYOU\;CHUANSHUO $1

cd scripts
