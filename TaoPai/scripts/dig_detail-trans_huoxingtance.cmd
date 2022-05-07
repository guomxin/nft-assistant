rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py huoxingtance %1

rem 2. dig info for ZhuRong
python diginfo_from_details_conflux.py huoxingtance 1 data/_details_conflux_huoxingtance_result_%1.csv 20001 20515 ZHURONG %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py huoxingtance 2 data/_details_conflux_huoxingtance_result_%1.csv 20001,24823 1 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py huoxingtance 3 data/_details_conflux_huoxingtance_result_%1.csv %1

rem 5. analyze tranctions
rem python transaction_conflux_contract.py hangtiantanwei2 trans/HTKG_transactions_%1.csv %2 %3 1,5;6,370 JIN;ZHURONGZI %1

cd scripts