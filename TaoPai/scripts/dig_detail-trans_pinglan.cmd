rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py pinglan %1

rem 2. dig info for KunMingFuHua && FuHua
python diginfo_from_details_conflux.py pinglan 1 data/_details_conflux_pinglan_result_%1.csv 70001,70485 KUNMINGFUHUA  %1
python diginfo_from_details_conflux.py pinglan 1 data/_details_conflux_pinglan_result_%1.csv 70486,71455 FUHUA %1
python diginfo_from_details_conflux.py pinglan 1 data/_details_conflux_pinglan_result_%1.csv 70001,73395 ANY %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py pinglan 2 data/_details_conflux_pinglan_result_%1.csv 70001,70485;70486,71455;71456,73395 1;2;4 FEIJI %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py pinglan 3 data/_details_conflux_pinglan_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py pinglan %2 %3 70001,70485;70486,71455;71456,73395 ^
KUNMINGFUHUA;FUHUA;HANGUANG %1

cd scripts