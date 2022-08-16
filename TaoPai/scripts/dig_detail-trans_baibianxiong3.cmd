rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py baibianxiong3 %1

rem 2. dig info for SSR&SR
python diginfo_from_details_conflux.py baibianxiong3 1 data/_details_conflux_baibianxiong3_result_%1.csv 14001,17300  ANY %1
python diginfo_from_details_conflux.py baibianxiong3 1 data/_details_conflux_baibianxiong3_result_%1.csv 14001,14035 SSR %1
python diginfo_from_details_conflux.py baibianxiong3 1 data/_details_conflux_baibianxiong3_result_%1.csv 14036,14350 SR %1

rem 3. dig count in circulation
python diginfo_from_details_conflux.py baibianxiong3 3 data/_details_conflux_baibianxiong3_result_%1.csv %1

cd scripts