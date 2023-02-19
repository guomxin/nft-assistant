rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py xiyouxingqiu2 %1

rem 2. dig info for PUTONG&XIYOU
python diginfo_from_details_conflux.py xiyouxingqiu2 1 data/_details_conflux_xiyouxingqiu2_result_%1.csv ^
20001,24900 PUTONG %1
python diginfo_from_details_conflux.py xiyouxingqiu2 1 data/_details_conflux_xiyouxingqiu2_result_%1.csv ^
24901,25000 XIYOU %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py xiyouxingqiu2 2 data/_details_conflux_xiyouxingqiu2_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py xiyouxingqiu2 3 data/_details_conflux_xiyouxingqiu2_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py xiyouxingqiu2 %2 %3 ^
20001,24900;24901,25000 ^
PUTONG;XIYOU %1

cd scripts
