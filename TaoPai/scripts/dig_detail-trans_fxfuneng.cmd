rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py fxfuneng %1

rem 2. dig info CHUANGSHI & DAYUANMAN
python diginfo_from_details_conflux.py fxfuneng 1 data/_details_conflux_fxfuneng_result_%1.csv ^
11001,11103 FXCHUANGSHI %1
python diginfo_from_details_conflux.py fxfuneng 1 data/_details_conflux_fxfuneng_result_%1.csv ^
23751,24750 DAYUANMAN %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py fxfuneng 2 data/_details_conflux_fxfuneng_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py fxfuneng 3 data/_details_conflux_fxfuneng_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py fxfuneng %2 %3 ^
23751,24750;11001,11103 ^
DAYUANMAN;CHUANGSHI %1

cd scripts
