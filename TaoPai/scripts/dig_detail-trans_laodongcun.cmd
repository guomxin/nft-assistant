rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py laodongcun %1

rem 2. dig info for ANY, CONGMING, HANYONG
python diginfo_from_details_conflux.py laodongcun 1 data/_details_conflux_laodongcun_result_%1.csv 11801 13000  CONGMING %1
python diginfo_from_details_conflux.py laodongcun 1 data/_details_conflux_laodongcun_result_%1.csv 13001 14200  HANYONG %1
python diginfo_from_details_conflux.py laodongcun 1 data/_details_conflux_laodongcun_result_%1.csv 16001 16600  ZONGZI %1
python diginfo_from_details_conflux.py laodongcun 1 data/_details_conflux_laodongcun_result_%1.csv 16601 17200  LONGZHOU %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py laodongcun 2 data/_details_conflux_laodongcun_result_%1.csv 3001,10000 18 N18 %1
rem python diginfo_from_details_conflux.py laodongcun 2 data/_details_conflux_laodongcun_result_%1.csv 501,3000 6 R6 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py laodongcun 3 data/_details_conflux_laodongcun_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py laodongcun %2 %3 10001,11800;11801,13000;13001,14200;14201,16000;16001,16600;16601,17200;17201,17800 ^
QINLAO;CONGMING;HANYONG;JIANZUI;ZONGZI;LONGZHOU;SR-HUASHOU %1

cd scripts
