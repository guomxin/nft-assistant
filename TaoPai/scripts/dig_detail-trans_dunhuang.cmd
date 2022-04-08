rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
rem python detail_conflux_dunhuang.py %1

rem 2. dig info for gold
python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 37001 38000 GOLD %1

rem 3. dig info for purple
python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 38001 40000 PURPLE %1

rem 4. analyze tranctions for gold
python transaction_conflux_dunhuang.py trans/SDQH_transactions_%1.csv %2 %3 37001 38000 GOLD %1

rem 4. analyze tranctions for purple
python transaction_conflux_dunhuang.py trans/SDQH_transactions_%1.csv %2 %3 38001 40000 PURPLE %1

cd scripts