rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py qiannian %1

rem 2. dig info for QianNianShouHu
python diginfo_from_details_conflux.py qiannian 1 data/_details_conflux_qiannian_result_%1.csv 11001 11500 QIANNIAN %1

rem 3. analyze tranctions for QianNianShouHu
python transaction_conflux_contract.py qiannian trans/JYY_transactions_%1.csv %2 %3 11001 11500 QIANNIAN %1

cd scripts