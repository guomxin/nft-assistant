rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
rem python detail_conflux_contract.py fxxunzhang %1

rem 2. dig info CHUANGSHI
python diginfo_from_details_conflux.py fxxunzhang 1 data/_details_conflux_fxxunzhang_result_%1.csv ^
11001,11103 FXCHUANGSHI %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py fxxunzhang 2 data/_details_conflux_fxxunzhang_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py fxxunzhang 3 data/_details_conflux_fxxunzhang_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py fxxunzhang %2 %3 ^
40104,40206;40207,40309;40310,40517;40518,40620;40621,40688;11001,11103 ^
HUNIAN;XIONGMAO;QINGTONG;BAIYIN;HUANGJIN;CHUANGSHI %1

cd scripts
