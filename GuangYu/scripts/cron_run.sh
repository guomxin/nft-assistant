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
python analyze_transaction_prices.py 3747 ${yesterday} 10

echo "---幽灵天台---"
python grab_transaction_price.py 3748 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3748 ${yesterday} 10

echo "---超能墨镜---"
python grab_transaction_price.py 3548 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3548 ${yesterday} 10

echo "---拳击手套---"
python grab_transaction_price.py 3549 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3549 ${yesterday} 10

echo "---超闪电磁---"
python grab_transaction_price.py 3550 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3550 ${yesterday} 10

echo "---时空穿梭机---"
python grab_transaction_price.py 3646 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3646 ${yesterday} 100

echo "---月球上城---"
python grab_transaction_price.py 3751 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3751 ${yesterday} 500

echo "---微光飞毯---"
python grab_transaction_price.py 4629 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4629 ${yesterday} 10

echo "---曙光陆舰---"
python grab_transaction_price.py 4630 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4630 ${yesterday} 10

#--- 神话区---#
echo "---载福祥凰---"
python grab_transaction_price.py 3535 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 3535 ${yesterday} 100

echo "---龙吟万象---"
python grab_transaction_price.py 2837 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 2837 ${yesterday} 100

echo "---金躯玺印---"
python grab_transaction_price.py 4014 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4014 ${yesterday} 50

echo "---金莲灵盏---"
python grab_transaction_price.py 4386 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4386 ${yesterday} 50

echo "---异兽浮图---"
python grab_transaction_price.py 4384 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4384 ${yesterday} 50

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
echo "---晶光胶囊---"
python grab_transaction_price.py 4455 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4455 ${yesterday} 50

echo "---冰霜冷却系统---"
python grab_transaction_price.py 4417 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4417 ${yesterday} 100

echo "---液氮聚能罐---"
python grab_transaction_price.py 4493 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4493 ${yesterday} 50

echo "---磁能悬浮板---"
python grab_transaction_price.py 4502 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4502 ${yesterday} 100

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

echo "---液能防御塔---"
python grab_transaction_price.py 4559 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4559 ${yesterday} 50

echo "---彩糖梦乐园---"
python grab_transaction_price.py 4574 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4574 ${yesterday} 100

echo "---圣境之门---"
python grab_transaction_price.py 4589 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4589 ${yesterday} 500

echo "---精炼增产器---"
python grab_transaction_price.py 4605 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4605 ${yesterday} 50

echo "---晨曦之黯---"
python grab_transaction_price.py 4652 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4652 ${yesterday} 50

echo "---智控机械护手---"
python grab_transaction_price.py 4658 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4658 ${yesterday} 100

echo "---炽焰幻显---"
python grab_transaction_price.py 4675 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4675 ${yesterday} 100

echo "---Xmas-光陆雪橇---"
python grab_transaction_price.py 4647 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4647 ${yesterday} 100

echo "---幻影雷霆---"
python grab_transaction_price.py 4665 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4665 ${yesterday} 100

echo "---平安启示蛋---"
python grab_transaction_price.py 4690 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4690 ${yesterday} 50

echo "---草莓奶昔杯---"
python grab_transaction_price.py 4712 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4712 ${yesterday} 50

echo "---轮回花钟---"
python grab_transaction_price.py 4738 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4738 ${yesterday} 10

echo "---花期瞳镜---"
python grab_transaction_price.py 4766 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4766 ${yesterday} 10

echo "---双源之核---"
python grab_transaction_price.py 4717 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4717 ${yesterday} 10

echo "---前夕织章---"
python grab_transaction_price.py 4755 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4755 ${yesterday} 10

echo "---神光之扉---"
python grab_transaction_price.py 4663 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4663 ${yesterday} 10

echo "---江湖令---"
python grab_transaction_price.py 5000 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5000 ${yesterday} 10

echo "---水浒-张青---"
python grab_transaction_price.py 5003 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5003 ${yesterday} 10

echo "---水浒-武松---"
python grab_transaction_price.py 5004 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5004 ${yesterday} 10

#--- 赛博狂潮 ---#
echo "---赛博起飞卡---"
python grab_transaction_price.py 4985 ${yesterday} ${yesterday}

echo "---恶魔勋章---"
python grab_transaction_price.py 4924 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4924 ${yesterday} 10

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
echo "---小小键盘-L仔---"
python grab_transaction_price.py 4149 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4149 ${yesterday} 50

echo "---妙趣糖果盒---"
python grab_transaction_price.py 4622 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4622 ${yesterday} 10

echo "---传说卡片---"
python grab_transaction_price.py 4958 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4958 ${yesterday} 10

echo "---幻联之瞳---"
python grab_transaction_price.py 4814 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4814 ${yesterday} 10

echo "---奶酪梦巢---"
python grab_transaction_price.py 4810 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4810 ${yesterday} 10

echo "---云顶天宫---"
python grab_transaction_price.py 4839 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4839 ${yesterday} 10

echo "---盘古斧---"
python grab_transaction_price.py 4865 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4865 ${yesterday} 10

echo "---山海经-鹿蜀---"
python grab_transaction_price.py 4860 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4860 ${yesterday} 10

echo "---山海经-朱厌---"
python grab_transaction_price.py 4952 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4952 ${yesterday} 10

echo "---山海经-虎蛟---"
python grab_transaction_price.py 4948 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4948 ${yesterday} 10

echo "---山海经-鸓鸟---"
python grab_transaction_price.py 4834 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4834 ${yesterday} 10

echo "---山海经-蛊雕---"
python grab_transaction_price.py 4984 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4984 ${yesterday} 10

echo "---山海经-毕方---"
python grab_transaction_price.py 4969 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4969 ${yesterday} 10

echo "---龙腾华夏---"
python grab_transaction_price.py 4993 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4993 ${yesterday} 10

#--- 探索未来 ---#
echo "---数据代码---"
python grab_transaction_price.py 4827 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4827 ${yesterday} 10

echo "---未来数据---"
python grab_transaction_price.py 4909 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4909 ${yesterday} 10

echo "---超级能量---"
python grab_transaction_price.py 4913 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4913 ${yesterday} 10

echo "---未来时代---"
python grab_transaction_price.py 4941 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4941 ${yesterday} 10

echo "---虚空战神卡尔---"
python grab_transaction_price.py 4955 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4955 ${yesterday} 10

echo "---究极恐惧之门---"
python grab_transaction_price.py 4960 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4960 ${yesterday} 10

echo "---未来探险家EZ---"
python grab_transaction_price.py 4959 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4959 ${yesterday} 10

echo "---深渊震慑者20---"
python grab_transaction_price.py 4956 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4956 ${yesterday} 10

echo "---未来键盘-Ctrl仔20---"
python grab_transaction_price.py 4998 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4998 ${yesterday} 10

echo "---恶魔之王阿托---"
python grab_transaction_price.py 4974 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4974 ${yesterday} 10

echo "---小伦伦---"
python grab_transaction_price.py 4961 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4961 ${yesterday} 10

echo "---未来键盘领袖-超级键盘---"
python grab_transaction_price.py 4997 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4997 ${yesterday} 10

echo "---未来时间磨盘---"
python grab_transaction_price.py 5002 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5002 ${yesterday} 10

echo "---未来键盘-Q仔20---"
python grab_transaction_price.py 5012 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5012 ${yesterday} 10

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "1-WeiGuangFeiTan" "1-ShuGuangLuJian" \
"2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" "2-JinLianLingZhan" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "2-YiShouFuTu" "2-JiuChongTianWaiTian" \
"3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ChongHuoFeiYan" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"5-JingGuangJiaoNang" "5-ShengJingZhiMen" "5-JingLianZengChanQi" \
"5-BingShuangLengQueXiTong" "5-HeiQiaoJiXieCheng" "5-WeiDuSheXiangJi" "5-ChiYanHuanXian" \
"5-ShuangHuaYanHuo" "5-CaiTangMengLeYuan" "5-Xmas-GuangLuXueQiao" "5-JiangHuLing" \
"5-YeDanJuNengGuan" "5-CiNengXuanFuBan" "5-LiuGuangYouShi" "5-ZhiKongJiXieHuShou" "5-HuanYingLeiTing" \
"5-YeNengFangYuTa" "5-ChenXiZhiAn" "5-PingAnQiShiDan" "5-ShuiHu-ZhangQing" "5-ShuiHu-WuSong" \
"5-CaoMeiNaiXiBei" "5-LunHuiHuaZhong" "5-HuaQiTongJing" "5-ShuangYuanZhiHe" \
"5-QianXiZhiZhang" "5-ShenGuangZhiFei" \
"6-SaiBoQiFeiKa" "6-EMoXunZhang" \
"7-XiangSuQiJing" "7-TanXianZheIV" "7-XunBaoZheI" "7-GongYunXiaoShao" "7-FangBiaoZhiShiDeng" "7-YeGuWangCheng" \
"8-XiaoXiaoJianPan-LZai" "8-ChuanShuoKaPian" "8-ShanHaiJing-ZhuYan" \
"8-MiaoQuTangGuoHe" "8-HuanLianZhiTong" "8-ShanHaiJing-HuJiao" "8-ShanHaiJing-LeiNiao" \
"8-NaiLaoMengChao" "8-YunDingTianGong" "8-PanGuFu" "8-ShanHaiJing-LuShu" \
"8-ShanHaiJing-GuDiao" "8-ShanHaiJing-BiFang" "8-LongTengHuaXia" \
"9-WeiLaiShuJu" "9-ChaoJiNengLiang" \
"9-ShuJuDaiMa" "9-XuKongZhanShenKaEr" "9-JiuJiKongJuZhiMen" "9-WeiLaiTanXianJiaEZ" \
"9-WeiLaiShiDai" "9-ShenYuanZhenSheZhe20" "9-WeiLaiJianPan-CtrlZai20" "9-WeiLaiShiJianMoPan" \
"9-EMoZhiWangATuo" "9-XiaoLunLun" \
"9-WeiLaiJianPanLingXiu-ChaoJiJianPan" "9-WeiLaiJianPan-QZai20"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
