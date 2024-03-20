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

echo "---聚义厅---"
python grab_transaction_price.py 5075 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5075 ${yesterday} 10

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

echo "---水浒-扈三娘---"
python grab_transaction_price.py 5077 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5077 ${yesterday} 10

echo "---水浒-李逵---"
python grab_transaction_price.py 5055 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5055 ${yesterday} 10

echo "---西门庆---"
python grab_transaction_price.py 5086 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5086 ${yesterday} 10

echo "---神算子---"
python grab_transaction_price.py 5085 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5085 ${yesterday} 10

echo "---水浒-林冲---"
python grab_transaction_price.py 5097 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5097 ${yesterday} 10

echo "---水浒-燕青---"
python grab_transaction_price.py 5070 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5070 ${yesterday} 10

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
echo "---小小键盘-L仔---"
python grab_transaction_price.py 4149 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4149 ${yesterday} 50

echo "---传说卡片---"
python grab_transaction_price.py 4958 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4958 ${yesterday} 10

echo "---盘古斧---"
python grab_transaction_price.py 4865 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4865 ${yesterday} 10

echo "---山海经-鸓鸟---"
python grab_transaction_price.py 4834 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4834 ${yesterday} 10

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

echo "---镂花伞轮---"
python grab_transaction_price.py 5079 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5079 ${yesterday} 10

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
echo "---BabyDragon---"
python grab_transaction_price.py 5029 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5029 ${yesterday} 10

echo "---未来键盘-F仔---"
python grab_transaction_price.py 5046 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5046 ${yesterday} 10

echo "---DragonKing---"
python grab_transaction_price.py 5061 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5061 ${yesterday} 10

echo "---最强王者---"
python grab_transaction_price.py 4227 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4227 ${yesterday} 10

echo "---屠龙勇士---"
python grab_transaction_price.py 5083 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5083 ${yesterday} 10

echo "---风龙---"
python grab_transaction_price.py 5095 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5095 ${yesterday} 10

echo "---火龙---"
python grab_transaction_price.py 5101 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5101 ${yesterday} 10

echo "---地龙---"
python grab_transaction_price.py 5106 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5106 ${yesterday} 10

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "1-WeiGuangFeiTan" "1-ShuGuangLuJian" \
"2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" "2-JinLianLingZhan" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "2-YiShouFuTu" "2-JiuChongTianWaiTian" \
"3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ChongHuoFeiYan" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"5-JingGuangJiaoNang" "5-ShengJingZhiMen" "5-ShuiHu-WuYong" "5-ShuiHu-LiKui" "5-XiMenQing" \
"5-BingShuangLengQueXiTong" "5-HeiQiaoJiXieCheng" "5-ShenSuanZi" "5-ShuiHu-LinChong" \
"5-CaiTangMengLeYuan" "5-Xmas-GuangLuXueQiao" "5-JiangHuLing" "5-WuSongDaHu" "5-ShuiHu-YanQing" \
"5-YeDanJuNengGuan" "5-CiNengXuanFuBan" "5-LiuGuangYouShi" "5-ZhiKongJiXieHuShou" "5-HuanYingLeiTing" \
"5-YeNengFangYuTa" "5-PingAnQiShiDan" "5-ShuiHu-ZhangQing" "5-ShuiHu-WuSong" \
"5-CaoMeiNaiXiBei" "5-ShuangYuanZhiHe" "5-ShiZiPoRouBaoZiPu" "5-ShuiHu-HuSanNiang" \
"5-QianXiZhiZhang" "5-ShenGuangZhiFei" "5-JuYiTing" "5-ShuiHu" "5-NengLiangXuJiDanYuan" \
"6-SaiBoQiFeiKa" "6-EMoXunZhang"  "6-SaiBoNiYu" "6-SaiBoTop" "6-SaiBoPoYiHeXin" "6-SaiBoTopOne" \
"6-SaiBoJiangZiYa" "6-SaiBoKawasaki" \
"7-XiangSuQiJing" "7-TanXianZheIV" "7-XunBaoZheI" "7-GongYunXiaoShao" "7-FangBiaoZhiShiDeng" "7-YeGuWangCheng" \
"8-XiaoXiaoJianPan-LZai" "8-ChuanShuoKaPian" "8-QiaoMingYueYe" "8-XingChenQiYu" \
"8-ShanHaiJing-LeiNiao" "8-PanGuFu" "8-LongTengHuaXia" "8-ShanHaiJing-BiBi" \
"8-FanHuaShengShi" "8-BiShanQiongYu" "8-YaoYeDengXia" "8-LouHuaSanLun" \
"9-WeiLaiShuJu" "9-ChaoJiNengLiang" "9-WeiLaiShiDai" "9-ShenYuanZhenSheZhe20" \
"9-ShuJuDaiMa" "9-XuKongZhanShenKaEr" "9-JiuJiKongJuZhiMen" "9-WeiLaiTanXianJiaEZ" \
"9-EMoZhiWangATuo" "9-XiaoLunLun"  \
"10-BabyDragon" "10-ZuiQiangWangZhe" "10-DragonKing" "10-WeiLaiJianPan-FZai" \
"10-TuLongYongShi" "10-FengLong" "10-HuoLong" "10-DiLong"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
