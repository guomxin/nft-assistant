rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py lt %1

rem 2. dig info
rem python diginfo_from_details_conflux.py lt 1 data/_details_conflux_lt_result_%1.csv 1 10000  ANY %1
rem python diginfo_from_details_conflux.py lt 1 data/_details_conflux_lt_result_%1.csv 1 50 SSR %1
rem python diginfo_from_details_conflux.py lt 1 data/_details_conflux_lt_result_%1.csv 51 500 SR %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py lt 2 data/_details_conflux_lt_result_%1.csv 3000,8680 2 LIANGTAO %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py lt 3 data/_details_conflux_lt_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py lt %2 %3 3000,8680 XINGER %1

cd scripts