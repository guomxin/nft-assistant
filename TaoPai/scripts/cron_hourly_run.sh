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

date=`date --date="1 hour ago" +%Y/%m/%d`
hour=`date --date="1 hour ago" +%H`
tag=`date --date="1 hour ago" +%Y%m%d%H`

echo "------${date} ${hour}------"

# 烤仔的朋友
python transaction_conflux_contract_hourly_online.py kaozaifriends $date $hour 100001,109628\;200001,200360\;300001,300012\;2001,2052 PUTONG\;JINSE\;SHENGXIAO\;520DIANCANG $tag

# 勋章
python transaction_conflux_contract_hourly_online.py xunzhang $date $hour 60001,70000\;201,218\;219,303\;70001,82000\;1,200 ZAONIAO\;DASHI\;JINGYING\;QINGLIANG\;WANGZHE $tag

# 2022光符
python transaction_conflux_contract_hourly_online.py taopai2022 $date $hour 30001,32022 ANY $tag

# 内测和公测
python transaction_conflux_contract_hourly_online.py taopaitest $date $hour 10001,10999\;20001,20127 NEICE\;GONGCE $tag

# 乐淘淘
python transaction_conflux_contract_hourly_online.py letaotao $date $hour 50001,51496\;51636,52163 PART1\;PART2 $tag

# 柜子
python transaction_conflux_contract_hourly_online.py guizi $date $hour 1,1000\;1001,4000 GUIZI-SR\;GUIZI-N $tag

# 劳动村
python transaction_conflux_contract_hourly_online.py laodongcun $date $hour 10001,11800\;11801,13000\;13001,14200\;14201,16000\;16001,16600\;16601,17200\;17201,17800 \
QINLAO\;CONGMING\;HANYONG\;JIANZUI\;ZONGZI\;LONGZHOU\;SR-HUASHOU $tag

# 百变熊熊
python transaction_conflux_contract_hourly_online.py baibianxiong $date $hour 1,50\;51,500\;501,3000\;3001,10000\;10001,10015\;11001,12420\;12500,12649 \
SSR\;SR\;R\;N\;SSR-DUANWU\;SUIPIAN\;SR-FATHERDAY $tag

# 天坛波普
python transaction_conflux_contract_hourly_online.py tiantanbopu $date $hour 1001,1240\;1241,1380\;1381,1400 S\;SS\;SSS $tag

# 水晶博物馆
python transaction_conflux_contract_hourly_online.py shuijing $date $hour 1,2000\;2001,4000\;4001,6000\;6001,8000\;8001,9500\;9501,10000 \
R-MA\;R-PING\;R-YIN\;R-E\;SR-RUYI\;SSR-RENWU $tag

#------ 后处理 ------#
cd data/hourly;mkdir $tag;rm -f $tag/*
mv *$tag*.csv $tag;zip -q $tag $tag/*
zip_file=`pwd`/$tag.zip
cd ../..;python upload_baidudisk.py $zip_file `date --date="1 hour ago" +%Y%m%d`
