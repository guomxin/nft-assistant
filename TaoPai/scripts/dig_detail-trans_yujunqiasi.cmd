rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py yujunqiasi %1

rem 2. dig info for SSR
rem python diginfo_from_details_conflux.py yujunqiasi 1 data/_details_conflux_yujunqiasi_result_%1.csv 30001 32400 SSR %1

rem 3. dig info for fullset
python diginfo_from_details_conflux.py yujunqiasi 2 data/_details_conflux_yujunqiasi_result_%1.csv 50001,51700;61401,61700 2;2 JIYUNHE %1
python diginfo_from_details_conflux.py yujunqiasi 2 data/_details_conflux_yujunqiasi_result_%1.csv 51701,53400;61701,62000 2;2 CHANGYI %1
python diginfo_from_details_conflux.py yujunqiasi 2 data/_details_conflux_yujunqiasi_result_%1.csv 53401,55400 2 LINHAOQIN %1
python diginfo_from_details_conflux.py yujunqiasi 2 data/_details_conflux_yujunqiasi_result_%1.csv 55401,57400 2 XIANJI %1
python diginfo_from_details_conflux.py yujunqiasi 2 data/_details_conflux_yujunqiasi_result_%1.csv 57401,59400 2 KONGMING %1
python diginfo_from_details_conflux.py yujunqiasi 2 data/_details_conflux_yujunqiasi_result_%1.csv 59401,61400 2 NINGQING %1

python diginfo_from_details_conflux.py yujunqiasi 2 data/_details_conflux_yujunqiasi_result_%1.csv 50001,62000 2 ALL %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py yujunqiasi 3 data/_details_conflux_yujunqiasi_result_%1.csv %1

rem 5. analyze tranctions
rem python transaction_conflux_contract.py kaozaifriends trans/TaopaiNFT_transactions_%1.csv %2 %3 100001,109628;200001,200360;300001,300012 PUTONG;JINSE;SHENGXIAO %1

cd scripts