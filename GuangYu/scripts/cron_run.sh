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

#--- 幸运盒 ---#
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

#--- 神话区---#
echo "---载福祥凰---"
python grab_transaction_price.py 3535 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3535 ${yesterday} 500

echo "---龙吟万象---"
python grab_transaction_price.py 2837 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2837 ${yesterday} 500

echo "---金躯玺印---"
python grab_transaction_price.py 4014 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4014 ${yesterday} 500

echo "---幻术师---"
python grab_transaction_price.py 2616 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2616 ${yesterday} 100

echo "---魔术师---"
python grab_transaction_price.py 2617 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2617 ${yesterday} 100

#--- 三国区 ---#
echo "---忠义武圣---"
python grab_transaction_price.py 3982 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3982 ${yesterday} 500

echo "---雏凤明瞳---"
python grab_transaction_price.py 3979 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3979 ${yesterday} 10

echo "---银须箭道---"
python grab_transaction_price.py 3980 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3980 ${yesterday} 100

echo "---虎贲战靴---"
python grab_transaction_price.py 4083 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4083 ${yesterday} 50

echo "---勇猛戍兵---"
python grab_transaction_price.py 4127 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4127 ${yesterday} 50

echo "---丰登百谷---"
python grab_transaction_price.py 4019 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4019 ${yesterday} 100

#--- 推荐区 ---#
echo "---小小键盘-K仔---"
python grab_transaction_price.py 3919 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3919 ${yesterday} 20

echo "---解构光束---"
python grab_transaction_price.py 3818 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3818 ${yesterday} 10

echo "---飞鸿纸扇---"
python grab_transaction_price.py 3988 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3988 ${yesterday} 100

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-QingKongYuFengZhou" "1-N-MengYouGeLou" "1-N-ChaoNengMoJing" \
"1-SR-YingMuHuanShaPeng" "1-SR-QuanJiShouTao" "1-SSR-MoDengZhongXin" "1-SSR-ZhongGuiTieDao" "1-SSR-ChaoShanDianCi" \
"2-UR-WeiLaiDuShi" "2-UR-YuanYangDuLun" "2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-HuanShuShi" "2-MoShuShi" "2-JinQuXiYin" "3-ZhongYiWuSheng" "3-ChuFengMingTong" \
"3-XiaoXiaoJianPan-KZai"  "3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" \
"4-JieGouGuangShu"  "4-FeiHongZhiShan"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
