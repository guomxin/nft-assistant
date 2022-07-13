rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py huakaiyunqi %1

rem 2. dig info for ANY, YUNQILONGXIANG
python diginfo_from_details_conflux.py huakaiyunqi 1 data/_details_conflux_huakaiyunqi_result_%1.csv ^
12001,12199 CHUN %1
python diginfo_from_details_conflux.py huakaiyunqi 1 data/_details_conflux_huakaiyunqi_result_%1.csv ^
13401,13659 YUNQI %1
python diginfo_from_details_conflux.py huakaiyunqi 1 data/_details_conflux_huakaiyunqi_result_%1.csv ^
12001,13659 ANY %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py huakaiyunqi 2 data/_details_conflux_huakaiyunqi_result_%1.csv 12001,13399 1 HUAKAI %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py huakaiyunqi 3 data/_details_conflux_huakaiyunqi_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py huakaiyunqi %2 %3 ^
12001,12199;12201,12499;12501,12899;12901,13399;13401,13659 ^
CHUN;XIA;QIU;DONG;YUNQI %1

cd scripts
