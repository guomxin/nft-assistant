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

echo "------${today}------"

# Taopai
sh dig_detail-trans_kaozaifriends.sh $today $yesterday $yesterday
sh dig_detail-trans_taopai2022.sh  $today $yesterday $yesterday
sh dig_detail-trans_xunzhang.sh  $today $yesterday $yesterday
sh dig_detail-trans_letaotao.sh  $today $yesterday $yesterday
sh dig_detail-trans_taopaitest.sh  $today $yesterday $yesterday
#sh dig_detail-trans_chuangshi.sh  $today

# UXON
sh dig_detail-trans_laodongcun.sh  $today $yesterday $yesterday
sh dig_detail-trans_guizi.sh  $today $yesterday $yesterday

# BLOOM
sh dig_detail-trans_baibianxiong.sh  $today $yesterday $yesterday

# FXHE
#sh dig_detail-trans_fxpanda.sh  $today $yesterday $yesterday
sh dig_detail-trans_fxpanda2.sh  $today $yesterday $yesterday

# YCY
sh dig_detail-trans_shuijing.sh $today $yesterday $yesterday

# YQXK
sh dig_detail-trans_tiantanbopu.sh $today $yesterday $yesterday

# ConFashion
sh dig_detail-trans_kaozaikaituo.sh $today $yesterday $yesterday

# XJH
sh dig_detail-trans_saiboyouling.sh $today $yesterday $yesterday

#------ 后处理 ------#
cd ../data;mkdir -p upload/$today;rm -f upload/$today/*
cp *$today* upload/$today;cd upload/$today

for nft in "kaozaifriends" "taopai2022" "xunzhang" "letaotao" "taopaitest"  \
"guizi" "laodongcun" "baibianxiong" "fxpanda2" "shuijing" "tiantanbopu" "kaozaikaituo" \
"saiboyouling"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$today $nft/*
done
