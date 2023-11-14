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
echo "---梦游阁楼---"
python grab_transaction_price.py 3747 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3747 ${yesterday} 50

echo "---幽灵天台---"
python grab_transaction_price.py 3748 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3748 ${yesterday} 50

echo "---超能墨镜---"
python grab_transaction_price.py 3548 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3548 ${yesterday} 50

echo "---拳击手套---"
python grab_transaction_price.py 3549 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3549 ${yesterday} 50

echo "---超闪电磁---"
python grab_transaction_price.py 3550 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3550 ${yesterday} 100

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

echo "---大魔幻师---"
python grab_transaction_price.py 4323 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4323 ${yesterday} 100

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

echo "---刽虎刃---"
python grab_transaction_price.py 4167 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4167 ${yesterday} 50

echo "---锐锋箭翎---"
python grab_transaction_price.py 4078 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4078 ${yesterday} 50

echo "---云羽扬风---"
python grab_transaction_price.py 3981 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3981 ${yesterday} 100

echo "---战鼓擂---"
python grab_transaction_price.py 4243 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4243 ${yesterday} 50

echo "---东风吹---"
python grab_transaction_price.py 4246 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4246 ${yesterday} 50

#--- 推荐区 ---#
echo "---飞鸿纸扇---"
python grab_transaction_price.py 3988 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3988 ${yesterday} 100

#--- 万象之界 ---#
echo "---创界圣殿---"
python grab_transaction_price.py 4067 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4067 ${yesterday} 100

echo "---守护意志---"
python grab_transaction_price.py 4250 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4250 ${yesterday} 100

echo "---三生花械---"
python grab_transaction_price.py 4370 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4370 ${yesterday} 50

echo "---光合储能仓---"
python grab_transaction_price.py 4375 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4375 ${yesterday} 100

cho "---预制果实---"
python grab_transaction_price.py 4374 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4374 ${yesterday} 50

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ZhanGuLei" "3-DongFengChui" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"4-FeiHongZhiShan" \
"5-ChuangJieShengDian" "5-ShouHuYiZhi" "5-SanShengHuaXie" "5-GuangHeChuNengCang" "5-YuZhiGuoShi"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
