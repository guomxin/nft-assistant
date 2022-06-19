rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py tiantanbopu %1

rem 2. dig info for a-nft
python diginfo_from_details_conflux.py tiantanbopu 1 data/_details_conflux_tiantanbopu_result_%1.csv 1381 1400 SSS %1
python diginfo_from_details_conflux.py tiantanbopu 1 data/_details_conflux_tiantanbopu_result_%1.csv 1241 1380 SS %1
python diginfo_from_details_conflux.py tiantanbopu 1 data/_details_conflux_tiantanbopu_result_%1.csv 1001 1240 S %1

rem 3. dig full-set info
rem python diginfo_from_details_conflux.py tiantanbopu 2 data/_details_conflux_tiantanbopu_result_%1.csv 1001 1400 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py tiantanbopu 3 data/_details_conflux_tiantanbopu_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py tiantanbopu %2 %3 1001,1240;1241,1380;1381,1400 S;SS;SSS %1

cd scripts