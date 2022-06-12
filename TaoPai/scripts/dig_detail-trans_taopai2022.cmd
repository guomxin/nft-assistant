rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py taopai2022 %1

rem 2. dig info for ANY
python diginfo_from_details_conflux.py taopai2022 1 data/_details_conflux_taopai2022_result_%1.csv 30001 32022 ANY %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py taopai2022 2 data/_details_conflux_taopai2022_result_%1.csv 20001,24823 1 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py taopai2022 3 data/_details_conflux_taopai2022_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py taopai2022 %2 %3 30001,32022 ANY %1

cd scripts