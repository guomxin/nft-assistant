# $1-detail tag, $2-start_date, $3-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py fxpanda2 $1

# 2. dig info for ANY&CHUANSHUO
python diginfo_from_details_conflux.py fxpanda2 1 data/_details_conflux_fxpanda2_result_$1.csv 50001 61873 ANY $1
python diginfo_from_details_conflux.py fxpanda2 1 data/_details_conflux_fxpanda2_result_$1.csv 61524 61873 CHUANSHUO $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py fxpanda2 2 data/_details_conflux_fxpanda2_result_$1.csv 3001,10000 18 N18 $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py fxpanda2 3 data/_details_conflux_fxpanda2_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py fxpanda2 $2 $3 \
50001,56704\;56705,57880\;57881,58680\;58681,58880\;60001,61523\;61524,61873 \
PUTONG\;XIYOU\;PUTONG\;XIYOU\;XIYOU\;CHUANSHUO $1

cd scripts
