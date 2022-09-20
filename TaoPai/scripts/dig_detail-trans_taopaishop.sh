# $1-detail tag, $3-start_date, $4-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py taopaishop $1

# 2. dig info for ShopGongCe
python diginfo_from_details_conflux.py taopaishop 1 data/_details_conflux_taopaishop_result_$1.csv 250001,251200 SHOP $1

# 3. dig count in circulation
python diginfo_from_details_conflux.py taopaishop 3 data/_details_conflux_taopaishop_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py taopaishop $2 $3 250001,251200 ShopGongCe $1

cd scripts