# $1-detail tag, $3-start_date, $4-end_date

cd ..

# 1. generate details
python detail_conflux_contract.py baibianxiong $1
python diginfo_from_details_calc_baibianxiong_scores.py data/_details_conflux_baibianxiong_result_$1.csv $1

# 2. dig info for SSR&SR
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 1,17300  ANY $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 1,15\;13501,13501\;14001,14035 SSR $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 10001,10015\;12701,12746\;10060,10063\;19101,19191 SSR-KONGTOU $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 51,185\;13502,13503\;14036,14350 SR $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 12500,12649\;13301,13500\;10021,10026\;10027,10059 SR-KONGTOU $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 11001,12420 SUIPIAN $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 13001,13300 NAIZUI $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 18962,18981\;19000,19100 ZUANSHISX $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 18778,18961\;18992,18999 HUANGJINSX $1
python diginfo_from_details_conflux.py baibianxiong 1 data/_details_conflux_baibianxiong_result_$1.csv 19201,19323 MIGUAN $1

# 3. dig info for fullset
# python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_$1.csv 3001,10000 18 N18 $1
# python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_$1.csv 501,3000 6 R6 $1
# python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_$1.csv 501,3000\;3001,10000 3\;6 FRAGMENT $1
python diginfo_from_details_conflux.py baibianxiong 2 data/_details_conflux_baibianxiong_result_$1.csv \
18001,18437\;18438,18777\;18778,18961\;18982,18984\;18985,18991\;18992,18999 \
1\;1\;1\;1\;1\;1 HECHENG-ZUANSHISX $1

# 4. dig count in circulation
python diginfo_from_details_conflux.py baibianxiong 3 data/_details_conflux_baibianxiong_result_$1.csv $1

# 5. analyze tranctions
python transaction_conflux_contract_online.py baibianxiong $2 $3 \
1,50\;51,500\;501,3000\;3001,10000\;10001,10015\;11001,12420\;12500,12649\;13001,13300\;12701,12746\;12747,12749\;\
13301,13500\;14001,14035\;14036,14350\;14351,15100\;15101,17300\;10021,10059\;10060,10063\;10064,10065\;\
18001,18437\;18438,18777\;18778,18961\;18962,18981\;\
18982,18984\;18985,18991\;18992,18999\;19000,19100\;19101,19191\;19201,19323 \
SSR\;SR\;R\;N\;SSR-KONGTOU\;SUIPIAN\;SR-KONGTOU\;NAIZUI\;SSR-KONGTOU\;XIONGBAO\;\
SR-KONGTOU\;SSR\;SR\;R\;N\;SR-KONGTOU\;SSR-KONGTOU\;XIONGBAO\;\
QINGTONGSX\;BAIYINSX\;HUANGJINSX\;ZUANSHISX\;\
QINGTONGSX\;BAIYINSX\;HUANGJINSX\;ZUANSHISX\;SSR-KONGTOU\;MIGUAN $1

cd scripts