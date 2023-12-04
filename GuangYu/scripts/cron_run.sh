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

echo "---金莲灵盏---"
python grab_transaction_price.py 4386 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4386 ${yesterday} 50

echo "---异兽浮图---"
python grab_transaction_price.py 4384 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4384 ${yesterday} 100

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

echo "---重火飞檐---"
python grab_transaction_price.py 4389 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4389 ${yesterday} 50

#--- 推荐区 ---#

#--- 万象之界 ---#
echo "---创界圣殿---"
python grab_transaction_price.py 4067 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4067 ${yesterday} 100

echo "---守护意志---"
python grab_transaction_price.py 4250 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4250 ${yesterday} 100

echo "---三生涟漪---"
python grab_transaction_price.py 4406 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4406 ${yesterday} 50

echo "---仿生培养基---"
python grab_transaction_price.py 4373 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4373 ${yesterday} 50

echo "---梦马奇缘---"
python grab_transaction_price.py 4450 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4450 ${yesterday} 100

echo "---晶光胶囊---"
python grab_transaction_price.py 4455 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4455 ${yesterday} 50

echo "---信仰迷城---"
python grab_transaction_price.py 4430 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4430 ${yesterday} 50

echo "---霓彩风车---"
python grab_transaction_price.py 4410 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4410 ${yesterday} 100

echo "---丛中刺玫---"
python grab_transaction_price.py 4397 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4397 ${yesterday} 10

echo "---冰霜冷却系统---"
python grab_transaction_price.py 4417 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4417 ${yesterday} 100

echo "---极光轮毂---"
python grab_transaction_price.py 4425 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4425 ${yesterday} 100

echo "---超载快充站---"
python grab_transaction_price.py 4444 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4444 ${yesterday} 50

echo "---多维错致虹桥---"
python grab_transaction_price.py 4442 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4442 ${yesterday} 50

echo "---流虹风帆---"
python grab_transaction_price.py 4453 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4453 ${yesterday} 50

echo "---缱卷花驾---"
python grab_transaction_price.py 4454 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4454 ${yesterday} 50

echo "---火风头盔---"
python grab_transaction_price.py 4479 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4479 ${yesterday} 50

#--- 赛博狂潮 ---#
echo "---虚实中枢---"
python grab_transaction_price.py 4443 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4443 ${yesterday} 50

echo "---便携式插件---"
python grab_transaction_price.py 4456 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4456 ${yesterday} 50

echo "---CODR-脉冲手枪---"
python grab_transaction_price.py 4457 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4457 ${yesterday} 50

echo "---免疫抑制剂---"
python grab_transaction_price.py 4459 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4459 ${yesterday} 50

echo "---骇客微工椅---"
python grab_transaction_price.py 4460 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4460 ${yesterday} 50

echo "---外置控制终端---"
python grab_transaction_price.py 4468 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4468 ${yesterday} 50

echo "---移速增幅靴---"
python grab_transaction_price.py 4469 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4469 ${yesterday} 50

echo "---捕影黑客---"
python grab_transaction_price.py 4482 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4482 ${yesterday} 50

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" "2-JinLianLingZhan" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "2-YiShouFuTu" \
"3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ChongHuoFeiYan" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"5-ChuangJieShengDian" "5-ShouHuYiZhi" "5-HuoFengTouKui" "5-FangShengPeiYangJi" "5-MengMaQiYuan" "5-JingGuangJiaoNang" \
"5-XinYangMiCheng" "5-NiCaiFengChe" "5-CongZhongCiMei" "5-BingShuangLengQueXiTong" "5-JiGuangLunGu" "5-ChaoZaiKuaiChongZhan" \
"5-LiuHongFengFan" "5-QianJuanHuaJia" \
"6-XuShiZhongShu" "6-BianXieShiChaJian" "6-CODR-MaiChongShouQiang" "6-MianYiYiZhiJi" "6-HaiKeWeiGongYi" "6-WaiZhiKongZhiZhongDuan" \
"6-YiSuZengFuXue" "6-BuYingHeiKe"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
