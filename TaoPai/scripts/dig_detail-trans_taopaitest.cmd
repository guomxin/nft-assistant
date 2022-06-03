rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py taopaitest %1

rem 2. dig info for NeiCe & GongCe
python diginfo_from_details_conflux.py taopaitest 1 data/_details_conflux_taopaitest_result_%1.csv 10001 10999 NEICE %1
python diginfo_from_details_conflux.py taopaitest 1 data/_details_conflux_taopaitest_result_%1.csv 20001 20127 GONGCE %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py taopaitest 2 data/_details_conflux_taopaitest_result_%1.csv 10001,20127 1 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py taopaitest 3 data/_details_conflux_taopaitest_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract.py taopaitest trans/TaopaiNFT_transactions_%1.csv %2 %3 10001,10999;20001,20127 NEICE;GONGCE %1

cd scripts