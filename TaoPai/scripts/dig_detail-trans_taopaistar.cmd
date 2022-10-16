rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py taopaistar %1

rem 2. dig info for Star
python diginfo_from_details_conflux.py taopaistar 1 data/_details_conflux_taopaistar_result_%1.csv 1,5072 STAR %1

rem 3. dig count in circulation
python diginfo_from_details_conflux.py taopaistar 3 data/_details_conflux_taopaistar_result_%1.csv %1

rem 5. analyze tranctions for Star
python transaction_conflux_contract_online.py taopaistar %2 %3 1,5072 Star %1

cd scripts