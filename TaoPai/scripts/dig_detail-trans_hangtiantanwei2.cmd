rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py hangtiantanwei2 %1

rem 2. dig info for Qi
python diginfo_from_details_conflux.py hangtiantanwei2 1 data/_details_conflux_hangtiantanwei2_result_%1.csv 15877 16576 QI %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py hangtiantanwei2 2 data/_details_conflux_hangtiantanwei2_result_%1.csv 10001,11469;11470,12938;12939,14407;14408,15876;15877,16576 2;2;2;2;1 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py hangtiantanwei2 3 data/_details_conflux_hangtiantanwei2_result_%1.csv %1

rem 5. analyze tranctions
rem TODO python transaction_conflux_contract_online.py hangtiantanwei2 %2 %3 1,5;6,370 JIN;ZHURONGZI %1

cd scripts