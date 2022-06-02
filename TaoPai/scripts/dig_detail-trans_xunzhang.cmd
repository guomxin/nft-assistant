rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py xunzhang %1

rem 2. dig info for 
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 60001 66140  ZAONIAO %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py xunzhang 2 data/_details_conflux_xunzhang_result_%1.csv 3001,10000 18 N18 %1
rem python diginfo_from_details_conflux.py xunzhang 2 data/_details_conflux_xunzhang_result_%1.csv 501,3000 6 R6 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py xunzhang 3 data/_details_conflux_xunzhang_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract.py xunzhang trans/TaopaiNFT_transactions_%1.csv %2 %3 60001,66140 ZAONIAO %1

cd scripts