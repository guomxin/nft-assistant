rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py dunhuang %1

rem 2. dig info for gold & purple
python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 37001 38000 GOLD %1
python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 38001 40000 PURPLE %1

rem 3. dig full-set info
python diginfo_from_details_conflux.py dunhuang 2 data/_details_conflux_dunhuang_result_%1.csv 10001 40000 ALL %1

rem 4. analyze tranctions for gold & purple
python transaction_conflux_contract.py dunhuang trans/SDQH_transactions_%1.csv %2 %3 37001 38000 GOLD %1
python transaction_conflux_contract.py dunhuang trans/SDQH_transactions_%1.csv %2 %3 38001 40000 PURPLE %1

cd scripts