rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py sdqhchuangshi %1

rem 2. dig info for CHUANGSHI
python diginfo_from_details_conflux.py sdqhchuangshi 1 data/_details_conflux_sdqhchuangshi_result_%1.csv ^
2701,2765 SDQHCHUANGSHI %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py sdqhchuangshi 2 data/_details_conflux_sdqhchuangshi_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py sdqhchuangshi 3 data/_details_conflux_sdqhchuangshi_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py sdqhchuangshi %2 %3 ^
2701,2765 ^
SDQHCHUANGSHI %1

cd scripts
