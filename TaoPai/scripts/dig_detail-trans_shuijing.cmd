rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py shuijing %1

rem 2. dig info for SSR&SR
python diginfo_from_details_conflux.py shuijing 1 data/_details_conflux_shuijing_result_%1.csv 1 10000  ANY %1
python diginfo_from_details_conflux.py shuijing 1 data/_details_conflux_shuijing_result_%1.csv 8001 9500 SR-RUYI %1
python diginfo_from_details_conflux.py shuijing 1 data/_details_conflux_shuijing_result_%1.csv 9501 10000 SSR-RENWU %1
python diginfo_from_details_conflux.py shuijing 1 data/_details_conflux_shuijing_result_%1.csv 10301 10600 WUDAJUXING %1
python diginfo_from_details_conflux.py shuijing 1 data/_details_conflux_shuijing_result_%1.csv 11001,11078 HEIMAO %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py shuijing 2 data/_details_conflux_shuijing_result_%1.csv 501,3000;3001,10000 3;6 FRAGMENT %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py shuijing 3 data/_details_conflux_shuijing_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py shuijing %2 %3 ^
1,2000;2001,4000;4001,6000;6001,8000;8001,9500;9501,10000;10301,10600;11001,11078 ^
R-MA;R-PING;R-YIN;R-E;SR-RUYI;SSR-RENWU;WUDAJUXING;HEIMAO %1

cd scripts