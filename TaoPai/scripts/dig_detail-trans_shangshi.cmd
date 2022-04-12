rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py shangshi %1

rem 2. dig info for single items
rem python diginfo_from_details_conflux.py shangshi 1 data/_details_conflux_dunhuang_result_%1.csv 2167 2388 ShouShi-GuiFei %1

rem 3. dig full-set info
python diginfo_from_details_conflux.py shangshi 2 data/_details_conflux_shangshi_result_%1.csv 889 2388 ALL %1
python diginfo_from_details_conflux.py shangshi 2 data/_details_conflux_shangshi_result_%1.csv 889 1944 YIFU %1
python diginfo_from_details_conflux.py shangshi 2 data/_details_conflux_shangshi_result_%1.csv 1945 2388 SHOUSHI %1

rem 4. analyze tranctions for single items
rem python transaction_conflux_contract.py shangshi trans/HYYS_transactions_%1.csv %2 %3 2167 2388 ShouShi-GuiFei %1
python transaction_conflux_contract.py shangshi trans/HYYS_transactions_%1.csv %2 %3 889 2388 ShangShi-ALL %1

cd scripts