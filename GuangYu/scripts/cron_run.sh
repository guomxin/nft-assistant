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

echo "---黑巧机械城---"
python grab_transaction_price.py 4499 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4499 ${yesterday} 100

echo "---液能防御塔---"
python grab_transaction_price.py 4559 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4559 ${yesterday} 50

echo "---彩糖梦乐园---"
python grab_transaction_price.py 4574 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4574 ${yesterday} 100

echo "---圣境之门---"
python grab_transaction_price.py 4589 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4589 ${yesterday} 500

echo "---智控机械护手---"
python grab_transaction_price.py 4658 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4658 ${yesterday} 100

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

echo "---双源之核---"
python grab_transaction_price.py 4717 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4717 ${yesterday} 10

echo "---前夕织章---"
python grab_transaction_price.py 4755 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4755 ${yesterday} 10

echo "---江湖令---"
python grab_transaction_price.py 5000 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5000 ${yesterday} 10

echo "---水浒-张青---"
python grab_transaction_price.py 5003 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5003 ${yesterday} 10

echo "---聚义厅---"
python grab_transaction_price.py 5109 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5109 ${yesterday} 10

echo "---水浒---"
python grab_transaction_price.py 5041 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5041 ${yesterday} 10

echo "---十字坡肉包子铺---"
python grab_transaction_price.py 5044 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5044 ${yesterday} 10

echo "---能量蓄积单元---"
python grab_transaction_price.py 4676 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4676 ${yesterday} 10

echo "---水浒-吴用---"
python grab_transaction_price.py 5048 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5048 ${yesterday} 10

echo "---武松打虎---"
python grab_transaction_price.py 5063 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5063 ${yesterday} 10

echo "---神算子---"
python grab_transaction_price.py 5115 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5115 ${yesterday} 10

echo "---水浒-林冲---"
python grab_transaction_price.py 5097 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5097 ${yesterday} 10

echo "---小小键盘-L仔---"
python grab_transaction_price.py 4149 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4149 ${yesterday} 10

echo "---包子---"
python grab_transaction_price.py 5107 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5107 ${yesterday} 10

echo "---拳打镇关西---"
python grab_transaction_price.py 5082 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5082 ${yesterday} 10

echo "---大刀关胜---"
python grab_transaction_price.py 5112 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5112 ${yesterday} 10

echo "---水浒-史进---"
python grab_transaction_price.py 5128 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5128 ${yesterday} 10

echo "---军机处---"
python grab_transaction_price.py 5139 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5139 ${yesterday} 10

echo "---水浒-呼延灼---"
python grab_transaction_price.py 5133 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5133 ${yesterday} 10

echo "---水浒-董平---"
python grab_transaction_price.py 5141 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5141 ${yesterday} 10

echo "---酒肆---"
python grab_transaction_price.py 5142 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5142 ${yesterday} 10

echo "---酒---"
python grab_transaction_price.py 5150 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5150 ${yesterday} 10

echo "---粮草---"
python grab_transaction_price.py 5151 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5151 ${yesterday} 10

echo "---水浒-秦明---"
python grab_transaction_price.py 5129 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5129 ${yesterday} 10

echo "---水浒-蔡庆---"
python grab_transaction_price.py 5119 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5119 ${yesterday} 10

echo "---水浒-宋江---"
python grab_transaction_price.py 5181 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5181 ${yesterday} 10

echo "---戒刀---"
python grab_transaction_price.py 5162 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5162 ${yesterday} 10

echo "---水浒-高俅---"
python grab_transaction_price.py 5208 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5208 ${yesterday} 10

echo "---水浒-杨志---"
python grab_transaction_price.py 5179 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5179 ${yesterday} 10

#--- 赛博狂潮 ---#
echo "---赛博起飞卡---"
python grab_transaction_price.py 4985 ${yesterday} ${yesterday}

echo "---恶魔勋章---"
python grab_transaction_price.py 4924 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4924 ${yesterday} 10

echo "---赛博拟羽---"
python grab_transaction_price.py 5019 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5019 ${yesterday} 10

echo "---赛博Top---"
python grab_transaction_price.py 4982 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4982 ${yesterday} 10

echo "---赛博破译核心---"
python grab_transaction_price.py 5018 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5018 ${yesterday} 10

echo "---赛博TopOne---"
python grab_transaction_price.py 5064 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5064 ${yesterday} 10

echo "---赛博姜子牙---"
python grab_transaction_price.py 5049 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5049 ${yesterday} 10

echo "---赛博Kawasaki---"
python grab_transaction_price.py 5050 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5050 ${yesterday} 10

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
echo "---传说卡片---"
python grab_transaction_price.py 4958 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4958 ${yesterday} 10

echo "---龙腾华夏---"
python grab_transaction_price.py 4993 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4993 ${yesterday} 10

echo "---山海经-獙獙---"
python grab_transaction_price.py 5027 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5027 ${yesterday} 10

echo "---桥明月夜---"
python grab_transaction_price.py 5021 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5021 ${yesterday} 10

echo "---繁华盛世---"
python grab_transaction_price.py 5051 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5051 ${yesterday} 10

echo "---璧山琼宇---"
python grab_transaction_price.py 5088 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5088 ${yesterday} 10

echo "---星辰奇遇---"
python grab_transaction_price.py 5098 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5098 ${yesterday} 10

echo "---曜夜灯匣---"
python grab_transaction_price.py 5047 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5047 ${yesterday} 10

echo "---云霞华宝---"
python grab_transaction_price.py 5122 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5122 ${yesterday} 10

echo "---繁星点点---"
python grab_transaction_price.py 5123 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5123 ${yesterday} 10

echo "---静水深潭---"
python grab_transaction_price.py 5102 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5102 ${yesterday} 10

echo "---碧水青天---"
python grab_transaction_price.py 5144 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5144 ${yesterday} 10

echo "---龙游四海---"
python grab_transaction_price.py 5160 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5160 ${yesterday} 10

echo "---晨曦初现---"
python grab_transaction_price.py 5187 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5187 ${yesterday} 10

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

echo "---恶魔之王阿托---"
python grab_transaction_price.py 4974 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4974 ${yesterday} 10

echo "---小伦伦---"
python grab_transaction_price.py 4961 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4961 ${yesterday} 10

#--- 趣梦区 ---#
echo "---小小键盘-F仔---"
python grab_transaction_price.py 5127 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5127 ${yesterday} 10

echo "---龙魂---"
python grab_transaction_price.py 5143 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5143 ${yesterday} 10

echo "---影龙卫---"
python grab_transaction_price.py 5149 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5149 ${yesterday} 10

echo "---龙血---"
python grab_transaction_price.py 5184 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5184 ${yesterday} 10

echo "---龙之遗骸---"
python grab_transaction_price.py 5191 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5191 ${yesterday} 10

echo "---龙骨---"
python grab_transaction_price.py 5192 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5192 ${yesterday} 10

echo "---应龙-蓄水---"
python grab_transaction_price.py 5193 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5193 ${yesterday} 10

echo "---伊甸园---"
python grab_transaction_price.py 5209 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5209 ${yesterday} 10

echo "---亚当-合成资格卡---"
python grab_transaction_price.py 5210 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5210 ${yesterday} 10

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "1-WeiGuangFeiTan" "1-ShuGuangLuJian" \
"2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" "2-JinLianLingZhan" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "2-YiShouFuTu" "2-JiuChongTianWaiTian" \
"3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ChongHuoFeiYan" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"5-ShengJingZhiMen" "5-ShuiHu-WuYong" "5-JunJiChu" "5-ShuiHu-DongPing" "5-JiuSi" \
"5-BingShuangLengQueXiTong" "5-HeiQiaoJiXieCheng" "5-ShenSuanZi" "5-ShuiHu-LinChong" \
"5-CaiTangMengLeYuan" "5-Xmas-GuangLuXueQiao" "5-JiangHuLing" "5-WuSongDaHu" \
"5-YeDanJuNengGuan" "5-CiNengXuanFuBan" "5-LiuGuangYouShi" "5-ZhiKongJiXieHuShou" "5-HuanYingLeiTing" \
"5-YeNengFangYuTa" "5-PingAnQiShiDan" "5-ShuiHu-ZhangQing" "5-XiaoXiaoJianPan-LZai" \
"5-CaoMeiNaiXiBei" "5-ShuangYuanZhiHe" "5-ShiZiPoRouBaoZiPu" "5-QuanDaZhenGuanXi" \
"5-QianXiZhiZhang" "5-JuYiTing" "5-NengLiangXuJiDanYuan" "5-ShuiHu-HuYanZhuo" \
"5-BaoZi" "5-DaDaoGuanSheng"  "5-ShuiHu-ShiJin" \
"5-Jiu" "5-LiangCao" "5-ShuiHu-QinMing" "5-ShuiHu-CaiQing" "5-ShuiHu-YangZhi" \
"5-ShuiHu-SongJiang" "5-JieDao" "5-ShuiHu-GaoQiu" \
"5-ShuiHu" \
"6-SaiBoQiFeiKa" "6-EMoXunZhang"  "6-SaiBoNiYu" "6-SaiBoTopOne" "6-SaiBoTop" "6-SaiBoPoYiHeXin" \
"6-SaiBoJiangZiYa" "6-SaiBoKawasaki" \
"7-XiangSuQiJing" "7-TanXianZheIV" "7-XunBaoZheI" "7-GongYunXiaoShao" "7-FangBiaoZhiShiDeng" "7-YeGuWangCheng" \
"8-ChuanShuoKaPian" "8-QiaoMingYueYe" "8-XingChenQiYu" "8-YunXiaHuaBao" "8-BiShuiQingTian" \
"8-LongTengHuaXia" "8-ShanHaiJing-BiBi" "8-FanXingDianDian" "8-JingShuiShenTan" \
"8-FanHuaShengShi" "8-BiShanQiongYu" "8-YaoYeDengXia" "8-LongYouSiHai" "8-ChenXiChuXian" \
"9-WeiLaiShuJu" "9-ChaoJiNengLiang" "9-WeiLaiShiDai" "9-ShenYuanZhenSheZhe20" \
"9-ShuJuDaiMa" "9-XuKongZhanShenKaEr" "9-JiuJiKongJuZhiMen" "9-WeiLaiTanXianJiaEZ" \
"9-EMoZhiWangATuo" "9-XiaoLunLun"  \
"10-XiaoXiaoJianPan-FZai" "10-LongHun" "10-LongXue" "10-YingLongWei" \
"10-LongZhiYiHai" "10-LongGu" "10-YingLong-XuShui" "10-YiDianYuan" "10-YaDang-HeChengZiGeKa"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
