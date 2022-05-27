rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
rem python detail_conflux_contract.py baibianxiong %1

rem 2. dig info for SSR&SR
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 1 10000  ANY %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 1 50 SSR %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 51 500 SR %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_%1.csv 3001,10000 18 N18 %1
python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_%1.csv 501,3000 6 R6 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py baibianxiong 3 data/_details_conflux_baibianxiong_result_%1.csv %1

rem 5. analyze tranctions
rem python transaction_conflux_contract.py baibianxiong trans/TaopaiNFT_transactions_%1.csv %2 %3 100001,109628;200001,200360;300001,300012;2001,2052 PUTONG;JINSE;SHENGXIAO;520DIANCANG %1

cd scripts