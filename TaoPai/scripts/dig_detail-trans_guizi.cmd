rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py guizi %1

rem 2. dig info for SR&N
python diginfo_from_details_conflux.py guizi 1 data/_details_conflux_guizi_result_%1.csv 1 1000 GUIZI-SR %1
python diginfo_from_details_conflux.py guizi 1 data/_details_conflux_guizi_result_%1.csv 1001 4000 GUIZI-N %1

rem 3. dig count in circulation
python diginfo_from_details_conflux.py guizi 3 data/_details_conflux_guizi_result_%1.csv %1

rem 4. analyze tranctions
python transaction_conflux_contract_online.py guizi %2 %3 1,1000;1001,4000 GUIZI-SR;GUIZI-N %1

cd scripts