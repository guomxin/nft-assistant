# $1-detail tag

cd ..

# 1. generate details
python detail_conflux_contract.py taopaichuangshi $1

# 2. dig info for fullset
python diginfo_from_details_conflux.py taopaichuangshi 2 data/_details_conflux_taopaichuangshi_result_$1.csv \
10001,10999\;30001,32022\;50001,51496\;51636,52075\;20001,20003\;20005,20019\;20021,20028\;20030,20032\;20034,20040\;20043,20043\;20045,20049\;20051,20062\;\
20064,20065\;20067,20071\;20073,20074\;20076,20077\;20080,20080\;20082,20083\;20086,20088\;20090,20093\;20095,20097\;\
20099,20099\;20101,20109\;20111,20112\;20116,20117\;20120,20127 \
1\;5\;10\;10\;1 METHOD1 $1

python diginfo_from_details_conflux.py taopaichuangshi 2 data/_details_conflux_taopaichuangshi_result_$1.csv \
30001,32022\;50001,51496\;51636,52075\;20004,20004\;20020,20020\;20029,20029\;20033,20033\;20042,20042\;20044,20044\;20063,20063\;20066,20066\;20075,20075\;\
20079,20079\;20084,20085\;20089,20089\;20094,20094\;20110,20110\;20113,20115\;20118,20119 \
5\;10\;10\;1 METHOD2 $1

python diginfo_from_details_conflux.py taopaichuangshi 2 data/_details_conflux_taopaichuangshi_result_%1.csv 201,218\;200001,200360 1\;1 METHOD3 $1

# 3. merge results for two methods
python merge_fullset_result.py taopaichuangshi $1 METHOD1\;METHOD2

cd scripts
