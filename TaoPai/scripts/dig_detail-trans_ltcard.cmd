rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py ltcard %1

rem 2. dig info
python diginfo_from_details_conflux.py ltcard 1 data/_details_conflux_ltcard_result_%1.csv 11001,11066  SHISHI %1

rem 3. dig info for fullset

rem 4. dig count in circulation
python diginfo_from_details_conflux.py ltcard 3 data/_details_conflux_ltcard_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py ltcard %2 %3 11001,11066 SHISHI %1

cd scripts