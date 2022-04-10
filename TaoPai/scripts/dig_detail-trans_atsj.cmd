rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
rem python detail_conflux_contract.py atsj %1

rem 2. dig info for QuanJiaFu, LeiShi, Jin, JiaDeLuoSi
rem python diginfo_from_details_conflux.py atsj 1 data/_details_conflux_atsj_result_%1.csv 38501 38800 QuanJiaFu %1
rem python diginfo_from_details_conflux.py atsj 1 data/_details_conflux_atsj_result_%1.csv 301 400 LeiShi %1
rem python diginfo_from_details_conflux.py atsj 1 data/_details_conflux_atsj_result_%1.csv 201 300 Jin %1
rem python diginfo_from_details_conflux.py atsj 1 data/_details_conflux_atsj_result_%1.csv 101 200 JiaDeLuoSi %1

rem 3. analyze tranctions for QuanJiaFu, LeiShi, Jin, JiaDeLuoSi
python transaction_conflux_contract.py atsj trans/ATSJ_transactions_%1.csv %2 %3 38501 38800 QuanJiaFu %1
python transaction_conflux_contract.py atsj trans/ATSJ_transactions_%1.csv %2 %3 301 400 LeiShi %1
python transaction_conflux_contract.py atsj trans/ATSJ_transactions_%1.csv %2 %3 201 300 Jin %1
python transaction_conflux_contract.py atsj trans/ATSJ_transactions_%1.csv %2 %3 101 200 JiaDeLuoSi %1

cd scripts