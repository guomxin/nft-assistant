rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py 2pforest %1

rem 2. dig info
python diginfo_from_details_conflux.py 2pforest 1 data/_details_conflux_2pforest_result_%1.csv 4609,6808 ANY %1

rem 3. dig count in circulation
python diginfo_from_details_conflux.py 2pforest 3 data/_details_conflux_2pforest_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py 2pforest %2 %3 4609,5408;5409,5608;5609,6408;6409,6608;6609,6808 ^
YuMeiRen;YuMeiRen-YinCang;ZhuangYu;ZhuangYu-YinCang;CP %1

cd scripts