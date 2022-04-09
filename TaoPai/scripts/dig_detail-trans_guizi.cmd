rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_guizi.py %1

rem 2. dig info for SR
python diginfo_from_details_conflux.py guizi 1 data/_details_conflux_guizi_result_%1.csv 1 1000 GUIZI-SR %1

rem 3. dig info for N
python diginfo_from_details_conflux.py guizi 1 data/_details_conflux_guizi_result_%1.csv 1001 4000 GUIZI-N %1

rem 4. analyze tranctions for SR
rem python transaction_conflux_dunhuang.py trans/SDQH_transactions_%1.csv %2 %3 37001 38000 GOLD %1

rem 4. analyze tranctions for N
rem transaction_conflux_dunhuang.py trans/SDQH_transactions_%1.csv %2 %3 38001 40000 PURPLE %1

cd scripts