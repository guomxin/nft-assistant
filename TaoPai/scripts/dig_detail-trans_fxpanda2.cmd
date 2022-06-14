rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py fxpanda2 %1

rem 2. dig info for ANY
python diginfo_from_details_conflux.py fxpanda2 1 data/_details_conflux_fxpanda2_result_%1.csv 50001 57880 ANY %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py fxpanda2 2 data/_details_conflux_fxpanda2_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py fxpanda2 3 data/_details_conflux_fxpanda2_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py fxpanda2 %2 %3 50001,56704;56705,57880 PUTONG;XIYOU %1

cd scripts