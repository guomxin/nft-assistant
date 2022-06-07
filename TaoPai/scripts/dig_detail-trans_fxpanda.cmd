rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py fxpanda %1

rem 2. dig info for XIYOU&CHUANSHUO&ANY
python diginfo_from_details_conflux.py fxpanda 1 data/_details_conflux_fxpanda_result_%1.csv 30001 35656 ANY %1
python diginfo_from_details_conflux.py fxpanda 1 data/_details_conflux_fxpanda_result_%1.csv 35041 35656 CHUANSHUO %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py fxpanda 2 data/_details_conflux_fxpanda_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py fxpanda 3 data/_details_conflux_fxpanda_result_%1.csv %1

rem 5. analyze tranctions
rem python transaction_conflux_contract.py fxpanda trans/BOOOM_transactions_%1.csv %2 %3 1,50;51,500;501,3000;3001,10000;10001,10015 SSR;SR;R;N;SSR-DUANWU %1

cd scripts