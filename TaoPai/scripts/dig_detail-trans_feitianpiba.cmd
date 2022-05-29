rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py feitianpiba %1

rem 2. dig info for SSR&DaTu
rem python diginfo_from_details_conflux.py feitianpiba 1 data/_details_conflux_feitianpiba_result_%1.csv 1 800 SSR %1
python diginfo_from_details_conflux.py feitianpiba 1 data/_details_conflux_feitianpiba_result_%1.csv 15801 16400 DaTu %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py feitianpiba 2 data/_details_conflux_feitianpiba_result_%1.csv 1,800;801,6800;6801,15800 1;2;3 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py feitianpiba 3 data/_details_conflux_feitianpiba_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract.py feitianpiba trans/TLH_transactions_%1.csv %2 %3 1,800;801,6800;6801,15800;15801,16400 SSR;SR;R;DaTu %1

cd scripts