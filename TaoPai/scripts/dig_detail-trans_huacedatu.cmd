rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py huacedatu %1

rem 2. dig info for ANY&&ZHENCANG
python diginfo_from_details_conflux.py huacedatu 1 data/_details_conflux_huacedatu_result_%1.csv 46201 46400 CHANGGEXING-DAJIEJU %1
python diginfo_from_details_conflux.py huacedatu 1 data/_details_conflux_huacedatu_result_%1.csv 68001 69000 RENWU-HAIBAO %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py huacedatu 2 data/_details_conflux_huacedatu_result_%1.csv 501,3000;3001,10000 3;6 FRAGMENT %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py huacedatu 3 data/_details_conflux_huacedatu_result_%1.csv %1

cd scripts