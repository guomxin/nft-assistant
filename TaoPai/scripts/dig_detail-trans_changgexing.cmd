rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py changgexing %1

rem 2. dig info for SSR
rem python diginfo_from_details_conflux.py changgexing 1 data/_details_conflux_changgexing_result_%1.csv 30001 32400 SSR %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 40001,41800 1 R %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 41801,43000 1 SR %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 43001,43600 1 SSR %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 45001,46200 1 DAJIEJU %1

python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 10001,12240;16701,16860 1;1 R-CHANGAN %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 12241,14460;16861,17040 1;1 R-YOUZHOU %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 14461,16700;17041,17200 1;1 R-SHUOZHOU %1

python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 20001,21502;24468,24565 1;1 SR-YINGSHI %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 21503,22988;24566,24679 1;1 SR-WEISHUI %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 22989,24467;24680,24800 1;1 SR-WANGTING %1

python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 30001,30744;32234,32289 1;1 SSR-LIUYUNGUAN %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 30745,31488;32290,32345 1;1 SSR-MOBEI %1
python diginfo_from_details_conflux.py changgexing 2 data/_details_conflux_changgexing_result_%1.csv 31489,32233;32346,32400 1;1 SSR-DINGXIANG %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py changgexing 3 data/_details_conflux_changgexing_result_%1.csv %1

rem 5. analyze tranctions
rem python transaction_conflux_contract.py kaozaifriends trans/TaopaiNFT_transactions_%1.csv %2 %3 100001,109628;200001,200360;300001,300012 PUTONG;JINSE;SHENGXIAO %1

cd scripts