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

echo "---微光飞毯---"
python grab_transaction_price.py 4629 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4629 ${yesterday} 50

echo "---曙光陆舰---"
python grab_transaction_price.py 4630 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4630 ${yesterday} 50

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

echo "---金莲灵盏---"
python grab_transaction_price.py 4386 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4386 ${yesterday} 50

echo "---异兽浮图---"
python grab_transaction_price.py 4384 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4384 ${yesterday} 100

#--- 未归类 ---#
echo "---大魔幻师---"
python grab_transaction_price.py 4323 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4323 ${yesterday} 100

echo "---九重天外天---"
python grab_transaction_price.py 4607 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4607 ${yesterday} 100

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
echo "---仿生培养基---"
python grab_transaction_price.py 4373 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4373 ${yesterday} 50

echo "---晶光胶囊---"
python grab_transaction_price.py 4455 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4455 ${yesterday} 50

echo "---冰霜冷却系统---"
python grab_transaction_price.py 4417 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4417 ${yesterday} 100

echo "---火风头盔---"
python grab_transaction_price.py 4479 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4479 ${yesterday} 50

echo "---磁感电池---"
python grab_transaction_price.py 4471 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4471 ${yesterday} 50

echo "---液氮聚能罐---"
python grab_transaction_price.py 4493 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4493 ${yesterday} 50

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

echo "---苍穹引灯---"
python grab_transaction_price.py 4576 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4576 ${yesterday} 50

echo "---知更花期---"
python grab_transaction_price.py 4552 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4552 ${yesterday} 50

echo "---液能防御塔---"
python grab_transaction_price.py 4559 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4559 ${yesterday} 50

echo "---彩糖梦乐园---"
python grab_transaction_price.py 4574 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4574 ${yesterday} 100

echo "---圣境之门---"
python grab_transaction_price.py 4589 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4589 ${yesterday} 500

echo "---祈福之槌---"
python grab_transaction_price.py 4558 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4558 ${yesterday} 100

echo "---精炼增产器---"
python grab_transaction_price.py 4605 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4605 ${yesterday} 50

echo "---雪漾铃音---"
python grab_transaction_price.py 4646 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4646 ${yesterday} 50

echo "---晨曦之黯---"
python grab_transaction_price.py 4652 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4652 ${yesterday} 50

echo "---智控机械护手---"
python grab_transaction_price.py 4658 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4658 ${yesterday} 100

echo "---千夜之钥---"
python grab_transaction_price.py 4371 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4371 ${yesterday} 10

echo "---炽焰幻显---"
python grab_transaction_price.py 4675 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4675 ${yesterday} 100

echo "---无限未来厂---"
python grab_transaction_price.py 4672 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4672 ${yesterday} 10

echo "---光控卡钳---"
python grab_transaction_price.py 4681 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4681 ${yesterday} 100

echo "---Xmas-光陆雪橇---"
python grab_transaction_price.py 4647 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4647 ${yesterday} 100

#--- 赛博狂潮 ---#
echo "---外置控制终端---"
python grab_transaction_price.py 4468 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4468 ${yesterday} 50

echo "---捕影黑客---"
python grab_transaction_price.py 4482 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4482 ${yesterday} 50

echo "---移动超算机---"
python grab_transaction_price.py 4567 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4567 ${yesterday} 10

echo "---赛博PunK---"
python grab_transaction_price.py 4661 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4661 ${yesterday} 10

echo "---赛博Pig---"
python grab_transaction_price.py 4668 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4668 ${yesterday} 10

echo "---赛博Cat---"
python grab_transaction_price.py 4674 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4674 ${yesterday} 10

echo "---赛博飞翔Pig---"
python grab_transaction_price.py 4678 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4678 ${yesterday} 50

echo "---赛博登陆仓---"
python grab_transaction_price.py 4682 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4682 ${yesterday} 50

echo "---秘彩之环---"
python grab_transaction_price.py 4577 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4577 ${yesterday} 50

echo "---锯齿短匕---"
python grab_transaction_price.py 4636 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4636 ${yesterday} 50

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

echo "---小小键盘-D仔---"
python grab_transaction_price.py 4606 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4606 ${yesterday} 50

echo "---圣诞颂歌---"
python grab_transaction_price.py 4644 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4644 ${yesterday} 50

echo "---蘑钟乐园---"
python grab_transaction_price.py 4572 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4572 ${yesterday} 50

echo "---星耀篮坛---"
python grab_transaction_price.py 4650 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4650 ${yesterday} 50

#--- 探索未来 ---#
echo "---征召机甲---"
python grab_transaction_price.py 4562 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4562 ${yesterday} 50

echo "---探索原石---"
python grab_transaction_price.py 4642 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4642 ${yesterday} 10

echo "---钛岩均质者---"
python grab_transaction_price.py 4654 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4654 ${yesterday} 50

echo "---自由之誓---"
python grab_transaction_price.py 4659 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4659 ${yesterday} 100

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "1-WeiGuangFeiTan" "1-ShuGuangLuJian" \
"2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" "2-JinLianLingZhan" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "2-YiShouFuTu" "2-JiuChongTianWaiTian" \
"3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ChongHuoFeiYan" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"5-HuoFengTouKui" "5-FangShengPeiYangJi" "5-JingGuangJiaoNang" "5-ShengJingZhiMen" "5-QiFuZhiChui" "5-JingLianZengChanQi" \
"5-BingShuangLengQueXiTong" "5-HeiQiaoJiXieCheng" "5-WeiDuSheXiangJi" "5-ChiYanHuanXian" "5-WuXiangWeiLaiChang" \
"5-CiGanDianChi" "5-ShuangHuaYanHuo" "5-CaiTangMengLeYuan" "5-GuangKongKaQian" "5-Xmas-GuangLuXueQiao" \
"5-YeDanJuNengGuan" "5-CiNengXuanFuBan" "5-ShenYuJiangCi" "5-LiuGuangYouShi" "5-XueYangLingYin" "5-ZhiKongJiXieHuShou" \
"5-CangQiongYinDeng" "5-ZhiGengHuaQi" "5-YeNengFangYuTa" "5-ChenXiZhiAn" "5-QianYeZhiYao" \
"6-WaiZhiKongZhiZhongDuan" "6-BuYingHeiKe" "6-SaiBoCat" "6-SaiBoFeiXiangPig" "6-SaiBoDengLuCang" "6-MiCaiZhiHuan" \
"6-YiDongChaoSuanJi" "6-SaiBoPunK" "6-SaiBoPig" "6-JuChiDuanBi" \
"7-XiangSuQiJing" "7-TanXianZheIV" "7-XunBaoZheI" "7-GongYunXiaoShao" "7-FangBiaoZhiShiDeng" "7-YeGuWangCheng" \
"8-QianJuanHuaJia" "8-XiaoXiaoJianPan-LZai" "8-HuanXiaoQuQi" "8-XiaoXiaoJianPan-DZai" "8-ShengDanSongGe" "8-MoZhongLeYuan" \
"8-XingYaoLanTan" \
"9-ZhengZhaoJiJia" "9-TanSuoYuanShi" "9-TaiYanJunZhiZhe" "9-ZiYouZhiShi"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
