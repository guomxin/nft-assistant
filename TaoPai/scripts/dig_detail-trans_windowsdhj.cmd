rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py windowsdhj %1

rem 2. dig info for ShopGongCe
python diginfo_from_details_conflux.py windowsdhj 1 data/_details_conflux_windowsdhj_result_%1.csv 10001,13600 ANY %1

rem 3. dig count in circulation
python diginfo_from_details_conflux.py windowsdhj 3 data/_details_conflux_windowsdhj_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py windowsdhj %2 %3 10001,13000;13001,13600 NORMAL;HECHENG %1

cd scripts