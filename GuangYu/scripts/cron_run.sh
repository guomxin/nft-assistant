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

conda activate nft;cd /mnt/ssd01/git/nft-assistant/GuangYu

today=`date +%Y%m%d`
yesterday=`date --date="1 day ago" +%Y%m%d`

echo "------${today}------"

#python scan_circulation_info.py $today

echo "---晴空御风帚---"
python grab_transaction_price.py 3457 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3457 ${yesterday} 50

echo "---梦游阁楼---"
python grab_transaction_price.py 3747 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3747 ${yesterday} 50

echo "---超能墨镜---"
python grab_transaction_price.py 3548 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3548 ${yesterday} 50

echo "---影幕幻纱篷---"
python grab_transaction_price.py 3458 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3458 ${yesterday} 50

echo "---拳击手套---"
python grab_transaction_price.py 3549 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3549 ${yesterday} 50

echo "---摩登中心---"
python grab_transaction_price.py 2457 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2457 ${yesterday} 100

echo "---重轨铁道---"
python grab_transaction_price.py 2466 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2466 ${yesterday} 100

echo "---超闪电磁---"
python grab_transaction_price.py 3550 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3550 ${yesterday} 100

echo "---未来都市---"
python grab_transaction_price.py 2456 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2456 ${yesterday} 500

echo "---远洋渡轮---"
python grab_transaction_price.py 2468 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2468 ${yesterday} 500

echo "---时空穿梭机---"
python grab_transaction_price.py 3646 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3646 ${yesterday} 500

echo "---月球上城---"
python grab_transaction_price.py 3751 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3751 ${yesterday} 500

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-QingKongYuFengZhou" "1-N-MengYouGeLou" "1-N-ChaoNengMoJing" \
"1-SR-YingMuHuanShaPeng" "1-SR-QuanJiShouTao" "1-SSR-MoDengZhongXin" "1-SSR-ZhongGuiTieDao" "1-SSR-ChaoShanDianCi" \
"2-UR-WeiLaiDuShi" "2-UR-YuanYangDuLun" "2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
