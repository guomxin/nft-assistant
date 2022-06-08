rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py kaoshenglaile %1

rem 2. dig info for ANY
python diginfo_from_details_conflux.py kaoshenglaile 1 data/_details_conflux_kaoshenglaile_result_%1.csv 1 40000  ANY %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py kaoshenglaile 2 data/_details_conflux_kaoshenglaile_result_%1.csv 1,40000 1 FOURFIG %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py kaoshenglaile 3 data/_details_conflux_kaoshenglaile_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract.py kaoshenglaile trans/MBNH_transactions_%1.csv %2 %3 1,10000;10001,20000;20001,30000;30001,40000;10001,10015 MANZAI;XIBAO;JINBANG;ZHUANGYUAN %1

cd scripts