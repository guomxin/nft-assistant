rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py xunzhang %1

rem 2. dig info for 
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 60001 70000 ZAONIAO %1
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 201 218 DASHI %1
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 219 303 JINGYING %1
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 2501 2705 CESHIDASHI %1
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 70001 82000 QINGLIANG %1
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 1,200;300013,300015 WANGZHE %1
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 4001,4200 ZHIYUANZHE %1
python diginfo_from_details_conflux.py xunzhang 1 data/_details_conflux_xunzhang_result_%1.csv 1101,1700 LVMA %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py xunzhang 2 data/_details_conflux_xunzhang_result_%1.csv 3001,10000 18 N18 %1
rem python diginfo_from_details_conflux.py xunzhang 2 data/_details_conflux_xunzhang_result_%1.csv 501,3000 6 R6 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py xunzhang 3 data/_details_conflux_xunzhang_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py xunzhang %2 %3 ^
60001,70000;201,218;219,303;401,605;2501,2705;1,200;4001,4200;1101,1700;300013,300015 ^
ZAONIAO;DASHI;JINGYING;CESHIDASHI;QINGLIANG;WANGZHE;ZHIYUANZHE;LVMA;WANGZHE %1

cd scripts