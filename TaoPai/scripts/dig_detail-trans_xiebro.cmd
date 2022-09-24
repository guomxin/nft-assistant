rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py xiebro %1

rem 2. dig info
python diginfo_from_details_conflux.py xiebro 1 data/_details_conflux_xiebro_result_%1.csv 1,6000 ANY %1

rem 3. dig count in circulation
python diginfo_from_details_conflux.py xiebro 3 data/_details_conflux_xiebro_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py xiebro %2 %3 1,1000;1001,2000;2001,3000;3001,4000;4001,5000;5001,6000 ^
QUANJI;HUABAN;CHAOLIU;BENGDI;JIUGUI;YAOGUN %1

cd scripts