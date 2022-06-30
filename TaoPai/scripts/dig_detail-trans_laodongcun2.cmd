rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py laodongcun2 %1

rem 2. dig info for ANY, CONGMING, HANYONG
python diginfo_from_details_conflux.py laodongcun2 1 data/_details_conflux_laodongcun2_result_%1.csv 20001,26666  ANY %1
python diginfo_from_details_conflux.py laodongcun2 1 data/_details_conflux_laodongcun2_result_%1.csv 20001,21111  GUAILI %1
python diginfo_from_details_conflux.py laodongcun2 1 data/_details_conflux_laodongcun2_result_%1.csv 21112,22222  FUJIA %1
python diginfo_from_details_conflux.py laodongcun2 1 data/_details_conflux_laodongcun2_result_%1.csv 22223,24444  CUNKOU %1
python diginfo_from_details_conflux.py laodongcun2 1 data/_details_conflux_laodongcun2_result_%1.csv 24445,26666  SHIHUANG %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py laodongcun2 2 data/_details_conflux_laodongcun2_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py laodongcun2 3 data/_details_conflux_laodongcun2_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py laodongcun2 %2 %3 ^
20001,21111;21112,22222;22223,24444;24445,26666 ^
GUAILI;FUJIA;CUNKOU;SHIHUANG %1

cd scripts