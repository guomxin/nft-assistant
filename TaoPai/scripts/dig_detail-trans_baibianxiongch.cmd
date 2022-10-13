rem %1-detail tag, %3-start_date, %4-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py baibianxiongch %1

rem 2. dig info for fullset
python diginfo_from_details_conflux.py baibianxiongch 2 data/_details_conflux_baibianxiongch_result_%1.csv ^
12747,12749;10064,10065;19462,19502;^
10001,10015;12701,12746;^
10060,10063;19101,19191;19434,19438;19503,19589;^
18962,18981;19000,19100;19324,19373;^
12500,12649;13301,13500;10021,10026;10027,10059;19439,19460 ^
1;1;1;^
1;1;^
7;7;7;7;^
4;4;4;^
9;9;9;9;9 ^
CHUANGSHI %1

rem 3. dig count in circulation
python diginfo_from_details_conflux.py baibianxiongch 3 data/_details_conflux_baibianxiongch_result_%1.csv %1

cd scripts