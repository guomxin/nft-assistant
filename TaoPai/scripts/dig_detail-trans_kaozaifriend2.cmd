rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py kaozaifriends2 %1

rem 2. dig info for Evo2k
python diginfo_from_details_conflux.py kaozaifriends2 1 data/_details_conflux_kaozaifriends2_result_%1.csv 6001,6120 EVO2K %1

rem 3. dig info for fullset

rem 4. dig count in circulation
python diginfo_from_details_conflux.py kaozaifriends2 3 data/_details_conflux_kaozaifriends2_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py kaozaifriends2 %2 %3 6001,6120 EVO2K %1

cd scripts