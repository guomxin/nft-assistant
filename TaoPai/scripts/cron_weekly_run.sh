# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/mnt/ssd01/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/mnt/ssd01/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/mnt/ssd01/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/mnt/ssd01/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<

conda activate nft;cd /mnt/ssd01/git/nft-assistant/TaoPai

tag=`date +%Y%m%d`
yesterday=`date --date="1 day ago" +%Y/%m/%d`
oneweekago=`date --date="7 days ago" +%Y/%m/%d`

echo "------${tag}------"

echo "---烤仔的朋友---"
python transaction_conflux_contract_online.py kaozaifriends $oneweekago $yesterday 100001,109628\;200001,200360\;300001,300012\;2001,2052 PUTONG\;JINSE\;SHENGXIAO\;520DIANCANG $tag
python transaction_conflux_contract_online.py kaozaifriends2 $oneweekago $yesterday 6001,6120 EVO2K $tag

echo "---勋章---"
python transaction_conflux_contract_online.py xunzhang $oneweekago $yesterday 60001,70000\;201,218\;219,303\;70001,82000\;1,200 ZAONIAO\;DASHI\;JINGYING\;QINGLIANG\;WANGZHE $tag

echo "---2022光符---"
python transaction_conflux_contract_online.py taopai2022 $oneweekago $yesterday 30001,32022 ANY $tag

echo "---内测和公测---"
python transaction_conflux_contract_online.py taopaitest $oneweekago $yesterday 10001,10999\;20001,20127 NEICE\;GONGCE $tag

echo "---乐淘淘---"
python transaction_conflux_contract_online.py letaotao $oneweekago $yesterday 50001,51496\;51636,52163 PART1\;PART2 $tag

echo "---柜子---"
python transaction_conflux_contract_online.py guizi $oneweekago $yesterday 1,1000\;1001,4000 GUIZI-SR\;GUIZI-N $tag

echo "---劳动村---"
python transaction_conflux_contract_online.py laodongcun $oneweekago $yesterday 10001,11800\;11801,13000\;13001,14200\;14201,16000\;16001,16600\;16601,17200\;17201,17800 \
QINLAO\;CONGMING\;HANYONG\;JIANZUI\;ZONGZI\;LONGZHOU\;SR-HUASHOU $tag
python transaction_conflux_contract_online.py laodongcun2 $oneweekago $yesterday \
20001,21111\;21112,22222\;22223,24444\;24445,26666 \
GUAILI\;FUJIA\;CUNKOU\;SHIHUANG $tag

echo "---百变熊熊---"
python transaction_conflux_contract_online.py baibianxiong $oneweekago $yesterday 1,50\;51,500\;501,3000\;3001,10000\;10001,10015\;11001,12420\;12500,12649 \
SSR\;SR\;R\;N\;SSR-DUANWU\;SUIPIAN\;SR-FATHERDAY $tag

echo "---天坛波普---"
python transaction_conflux_contract_online.py tiantanbopu $oneweekago $yesterday 1001,1240\;1241,1380\;1381,1400 S\;SS\;SSS $tag

echo "---水晶博物馆---"
python transaction_conflux_contract_online.py shuijing $oneweekago $yesterday \
1,2000\;2001,4000\;4001,6000\;6001,8000\;8001,9500\;9501,10000\;10301,10600\;11001,11078 \
R-MA\;R-PING\;R-YIN\;R-E\;SR-RUYI\;SSR-RENWU\;WUDAJUXING\;HEIMAO $tag

echo "---佛系熊猫---"
python transaction_conflux_contract_online.py fxpandaall $oneweekago $yesterday \
30001,33624\;33625,35040\;35041,35656\;50001,56704\;56705,57880\;57881,58680\;58681,58880\;60001,61523\;61524,61873 \
PUTONG\;XIYOU\;CHUANSHUO\;PUTONG\;XIYOU\;PUTONG\;XIYOU\;XIYOU\;CHUANSHUO $tag

echo "---烤仔开拓者---"
python transaction_conflux_contract_online.py kaozaikaituo $oneweekago $yesterday \
15001,15500\;15501,16000\;16001,16500\;16501,17000\;17001,17500 \
ZHENCHA\;CHONGFENG\;YISHI\;ZHIHUIGUAN\;MENGSHI $tag

echo "---凹凸世界---"
python transaction_conflux_contract_online.py atsj $oneweekago $yesterday \
10001,25000\;25001,34000\;34001,37000\;37001,38500\;38501,38800\;101,200\;201,300\;301,400 \
R\;SR\;SSR\;UR\;QuanJiaFu\;Team-JiaDeLuoSi\;Team-Jin\;Team-LeiShi $tag

echo "---凭栏一片风云起---"
python transaction_conflux_contract_online.py pinglan $oneweekago $yesterday \
70001,70485\;70486,71455\;71456,73395\;73396,73410\;73411,73440\;73441,73500 \
KUNMINGFUHUA\;FUHUA\;HANGUANG\;KUNMINGFUHUA\;FUHUA\;HANGUANG $tag