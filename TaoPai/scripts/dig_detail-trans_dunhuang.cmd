rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. analyze tranctions
python transaction_conflux_contract.py dunhuang trans/SDQH_transactions_%1.csv %2 %3 1001,2000;2001,2333;37001,38000;38001,40000 RAINBOW;FULLGOLD;GOLD;PURPLE %1

rem 2. generate details
python detail_conflux_contract.py dunhuang %1

rem 3. dig info for a-nft
python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 1001 2000 RAINBOW %1
python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 2001 2333 FULLGOLD %1

rem python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 10001 14500 RED %1
rem python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 14501 19000 CHENG %1
rem python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 19001 23500 YELLOW %1
rem python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 23501 28000 GREEN %1
rem python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 28001 32500 BLUE %1
rem python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 32501 37000 DIAN %1

python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 37001 38000 GOLD %1
python diginfo_from_details_conflux.py dunhuang 1 data/_details_conflux_dunhuang_result_%1.csv 38001 40000 PURPLE %1

rem 4. dig full-set info
rem python diginfo_from_details_conflux.py dunhuang 2 data/_details_conflux_dunhuang_result_%1.csv 10001,40000 1 ALL %1

rem 5. dig count in circulation
python diginfo_from_details_conflux.py dunhuang 3 data/_details_conflux_dunhuang_result_%1.csv %1

cd scripts