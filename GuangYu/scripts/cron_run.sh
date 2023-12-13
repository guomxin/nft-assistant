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

echo "---仿生培养基---"
python grab_transaction_price.py 4373 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4373 ${yesterday} 50

echo "---晶光胶囊---"
python grab_transaction_price.py 4455 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4455 ${yesterday} 50

echo "---信仰迷城---"
python grab_transaction_price.py 4430 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4430 ${yesterday} 50

echo "---丛中刺玫---"
python grab_transaction_price.py 4397 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4397 ${yesterday} 10

echo "---冰霜冷却系统---"
python grab_transaction_price.py 4417 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4417 ${yesterday} 100

echo "---极光轮毂---"
python grab_transaction_price.py 4425 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4425 ${yesterday} 100

echo "---火风头盔---"
python grab_transaction_price.py 4479 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4479 ${yesterday} 50

echo "---镌花之盏---"
python grab_transaction_price.py 4483 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4483 ${yesterday} 50

echo "---磁感电池---"
python grab_transaction_price.py 4471 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4471 ${yesterday} 50

echo "---炙热狂躁引擎---"
python grab_transaction_price.py 4420 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4420 ${yesterday} 50

echo "---液氮聚能罐---"
python grab_transaction_price.py 4493 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4493 ${yesterday} 50

echo "---向日葵汲能装置---"
python grab_transaction_price.py 4458 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4458 ${yesterday} 50

echo "---磁能悬浮板---"
python grab_transaction_price.py 4502 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4502 ${yesterday} 100

echo "---神谕降赐---"
python grab_transaction_price.py 4481 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4481 ${yesterday} 100

echo "---流光邮匙---"
python grab_transaction_price.py 4500 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4500 ${yesterday} 50

echo "---双华烟火---"
python grab_transaction_price.py 4484 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4484 ${yesterday} 100

echo "---黑巧机械城---"
python grab_transaction_price.py 4499 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4499 ${yesterday} 100

echo "---维度摄像机---"
python grab_transaction_price.py 4473 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4473 ${yesterday} 100

echo "---参数果汁---"
python grab_transaction_price.py 4446 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4446 ${yesterday} 10

echo "---苍穹引灯---"
python grab_transaction_price.py 4576 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4576 ${yesterday} 50

echo "---知更花期---"
python grab_transaction_price.py 4552 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4552 ${yesterday} 50

echo "---液能防御塔---"
python grab_transaction_price.py 4559 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4559 ${yesterday} 50

#--- 赛博狂潮 ---#
echo "---便携式插件---"
python grab_transaction_price.py 4456 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4456 ${yesterday} 50

echo "---外置控制终端---"
python grab_transaction_price.py 4468 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4468 ${yesterday} 50

echo "---捕影黑客---"
python grab_transaction_price.py 4482 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4482 ${yesterday} 50

echo "---征召机甲---"
python grab_transaction_price.py 4562 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4562 ${yesterday} 50

echo "---殊光谱基站---"
python grab_transaction_price.py 4515 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4515 ${yesterday} 50

echo "---多功能腕表---"
python grab_transaction_price.py 4556 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4556 ${yesterday} 50

echo "---全息终端仪---"
python grab_transaction_price.py 4560 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4560 ${yesterday} 100

echo "---移动战略能源---"
python grab_transaction_price.py 4532 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4532 ${yesterday} 50

echo "---电磁元件---"
python grab_transaction_price.py 4575 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4575 ${yesterday} 10

#--- 探险区 ---#
echo "---像素奇晶---"
python grab_transaction_price.py 3998 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3998 ${yesterday} 10

echo "---探险者IV---"
python grab_transaction_price.py 3544 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3544 ${yesterday} 50

echo "---寻宝者I---"
python grab_transaction_price.py 3527 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3527 ${yesterday} 50

echo "---公允啸哨---"
python grab_transaction_price.py 4421 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4421 ${yesterday} 50

echo "---幻彩菇堡---"
python grab_transaction_price.py 2742 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2742 ${yesterday} 50

echo "---芳标指示灯---"
python grab_transaction_price.py 4381 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4381 ${yesterday} 50

echo "---邺菇王城---"
python grab_transaction_price.py 3977 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3977 ${yesterday} 100

#--- 传说区 ---#
echo "---缱卷花驾---"
python grab_transaction_price.py 4454 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4454 ${yesterday} 50

echo "---小小键盘-L仔---"
python grab_transaction_price.py 4149 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4149 ${yesterday} 50

echo "---欢笑曲奇---"
python grab_transaction_price.py 4569 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4569 ${yesterday} 50

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" "2-JinLianLingZhan" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "2-YiShouFuTu" \
"3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ChongHuoFeiYan" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"5-ChuangJieShengDian" "5-ShouHuYiZhi" "5-HuoFengTouKui" "5-FangShengPeiYangJi" "5-JingGuangJiaoNang" \
"5-XinYangMiCheng" "5-CongZhongCiMei" "5-BingShuangLengQueXiTong" "5-JiGuangLunGu" "5-HeiQiaoJiXieCheng" "5-WeiDuSheXiangJi" \
"5-JuanHuaZhiZhan" "5-CiGanDianChi" "5-ZhiReKuangZaoYinQing" "5-ShuangHuaYanHuo" \
"5-YeDanJuNengGuan" "5-XiangRiKuiJiNengZhuangZhi" "5-CiNengXuanFuBan" "5-ShenYuJiangCi" "5-LiuGuangYouShi" \
"5-CanShuGuoZhi" "5-CangQiongYinDeng" "5-ZhiGengHuaQi" "5-YeNengFangYuTa" \
"6-BianXieShiChaJian" "6-WaiZhiKongZhiZhongDuan" "6-BuYingHeiKe" "6-ShuGuangPuJiZhan" \
"6-ZhengZhaoJiJia" "6-DuoGongNengWanBiao" "6-QuanXiZhongDuanYi" "6-YiDongZhanLueNengYuan" "6-DianCiYuanJian" \
"7-XiangSuQiJing" "7-TanXianZheIV" "7-XunBaoZheI" "7-GongYunXiaoShao" "7-HuanCaiGuBao" "7-FangBiaoZhiShiDeng" "7-YeGuWangCheng" \
"8-QianJuanHuaJia" "8-XiaoXiaoJianPan-LZai" "8-HuanXiaoQuQi"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
