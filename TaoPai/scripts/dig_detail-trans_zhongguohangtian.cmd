rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py zhongguohangtian %1

rem 2. dig info for Jin&ZhuRongZi&ChangJuan
python diginfo_from_details_conflux.py zhongguohangtian 1 data/_details_conflux_zhongguohangtian_result_%1.csv 1 5 JIN %1
python diginfo_from_details_conflux.py zhongguohangtian 1 data/_details_conflux_zhongguohangtian_result_%1.csv 6 370 ZHURONGZI %1
python diginfo_from_details_conflux.py zhongguohangtian 1 data/_details_conflux_zhongguohangtian_result_%1.csv 9001 9365 CHANGJUAN %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py zhongguohangtian 2 data/_details_conflux_zhongguohangtian_result_%1.csv 6,370;371,794;795,2750;2751,4772;4773,6794;6795,8816 1;1;1;1;1;1 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py zhongguohangtian 3 data/_details_conflux_zhongguohangtian_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py zhongguohangtian %2 %3 1,5;6,370 JIN;ZHURONGZI %1

cd scripts