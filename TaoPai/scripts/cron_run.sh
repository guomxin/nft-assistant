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

conda activate nft;cd /mnt/ssd01/git/nft-assistant/TaoPai/scripts

today=`date +%Y%m%d`
yesterday=`date --date="1 day ago" +%Y/%m/%d`
yesterday_short=`date --date="1 day ago" +%Y%m%d`

echo "------${today}------"

# Taopai
echo "---烤仔的朋友---"
sh dig_detail-trans_kaozaifriends.sh $today $yesterday $yesterday
sh dig_detail-trans_kaozaifriends2.sh $today $yesterday $yesterday
echo "---2022幸运光符---"
sh dig_detail-trans_taopai2022.sh  $today $yesterday $yesterday
echo "---勋章---"
sh dig_detail-trans_xunzhang.sh  $today $yesterday $yesterday
echo "---乐淘淘---"
sh dig_detail-trans_letaotao.sh  $today $yesterday $yesterday
echo "---公测内测---"
sh dig_detail-trans_taopaitest.sh  $today $yesterday $yesterday
#sh dig_detail-trans_chuangshi.sh  $today

# UXON
echo "---劳动村---"
sh dig_detail-trans_laodongcun.sh  $today $yesterday $yesterday
sh dig_detail-trans_laodongcun2.sh  $today $yesterday $yesterday
echo "---柜子---"
sh dig_detail-trans_guizi.sh  $today $yesterday $yesterday

# BLOOM
echo "---百变熊熊---"
sh dig_detail-trans_baibianxiong.sh  $today $yesterday $yesterday

# FXHE
echo "---佛系惠二---"
sh dig_detail-trans_fxpanda_all.sh  $today $yesterday $yesterday
sh dig_detail-trans_fxxunzhang.sh  $today $yesterday $yesterday

# YCY 2022/9/7 曝出老鼠仓
#echo "---水晶博物馆---"
#sh dig_detail-trans_shuijing.sh $today $yesterday $yesterday

# YQXK
echo "---天坛波普---"
sh dig_detail-trans_tiantanbopu.sh $today $yesterday $yesterday

# ConFashion
#echo "---烤仔开拓者---"
#sh dig_detail-trans_kaozaikaituo.sh $today $yesterday $yesterday

# XJH
#echo "---赛博幽灵---"
#sh dig_detail-trans_saiboyouling.sh $today $yesterday $yesterday

# HC
#echo "---凭栏一片风云起---"
#sh dig_detail-trans_pinglan.sh  $today $yesterday $yesterday

# BOBOSG
#echo "---BOBO三国---"
#sh dig_detail-trans_bobosg.sh $today $yesterday $yesterday

# LT
echo "---花开四季云起龙骧---"
sh dig_detail-trans_huakaiyunqi.sh $today $yesterday $yesterday

# Limitless
#echo "---Limitless---"
#sh dig_detail-trans_limitless.sh $today $yesterday $yesterday

# 派对猫
echo "---派对猫首发纪念卡---"
sh dig_detail-trans_pcatmem.sh $today $yesterday $yesterday
echo "---派对猫---"
sh dig_detail-trans_partycat.sh $today $yesterday $yesterday

# 西游星球
echo "---西游星球---"
sh dig_detail-trans_xiyouxingqiu.sh $today $yesterday $yesterday

echo "---统计昨日活跃账户情况---"
cd ..
python stat_active_users.py ${yesterday_short}
cd scripts

#------ 后处理 ------#
cd ../data;mkdir -p upload/$today;rm -f upload/$today/*
cp *$today* upload/$today;cp _stat_activeuser_*_result_${yesterday_short}.csv upload/$today;cd upload/$today

for nft in "kaozaifriends" "taopai2022" "xunzhang" "letaotao" "taopaitest"  \
"guizi" "laodongcun" "baibianxiong" "fxpandaall" "shuijing" "tiantanbopu" \
"huakaiyunqi" "pcatmem" "partycat" "xiyouxingqiu" "activeuser"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$today $nft/*
done
