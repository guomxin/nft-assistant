rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py tongjing %1

rem 2. dig info for ANY
python diginfo_from_details_conflux.py tongjing 1 data/_details_conflux_tongjing_result_%1.csv 1 32500  ANY %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py tongjing 2 data/_details_conflux_tongjing_result_%1.csv 1,32500 1 FOURMIRROR %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py tongjing 3 data/_details_conflux_tongjing_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py tongjing %2 %3 1,2500;10001,12500;20001,22500;30001,32500 XIANGHUA;WURU;SISHEN;FEISHUANG %1

cd scripts