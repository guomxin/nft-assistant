rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py baibianxiong %1
python diginfo_from_details_calc_baibianxiong_scores.py data/_details_conflux_baibianxiong_result_%1.csv %1

rem 2. dig info for SSR&SR
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 1,17300  ANY %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 1,15;13501,13501;14001,14035 SSR %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 10001,10015;12701,12746;10060,10063 SSR-KONGTOU %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 51,185;13502,13503;14036,14350 SR %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 12500,12649;13301,13500;10021,10026;10027,10059 SR-KONGTOU %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 11001,12420 SUIPIAN %1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_%1.csv 13001,13300 NAIZUI %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_%1.csv 3001,10000 18 N18 %1
rem python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_%1.csv 501,3000 6 R6 %1
rem python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_%1.csv 501,3000;3001,10000 3;6 FRAGMENT %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py baibianxiong 3 data/_details_conflux_baibianxiong_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py baibianxiong %2 %3 ^
1,50;51,500;501,3000;3001,10000;10001,10015;11001,12420;12500,12649;13001,13300;12701,12746;12747,12749;^
13301,13500;14001,14035;14036,14350;14351,15100;15101,17300;10021,10059;10060,10063;10064,10065 ^
SSR;SR;R;N;SSR-KONGTOU;SUIPIAN;SR-KONGTOU;NAIZUI;SSR-KONGTOU;XIONGBAO;^
SR-KONGTOU;SSR;SR;R;N;SR-KONGTOU;SSR-KONGTOU;XIONGBAO %1

cd scripts