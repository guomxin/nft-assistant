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
echo "---十字坡肉包子铺---"
python grab_transaction_price.py 5044 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5044 ${yesterday} 10

echo "---水浒-吴用---"
python grab_transaction_price.py 5048 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5048 ${yesterday} 10

echo "---包子---"
python grab_transaction_price.py 5107 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5107 ${yesterday} 10

echo "---军机处---"
python grab_transaction_price.py 5139 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5139 ${yesterday} 10

echo "---酒肆---"
python grab_transaction_price.py 5142 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5142 ${yesterday} 10

echo "---酒---"
python grab_transaction_price.py 5150 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5150 ${yesterday} 10

echo "---粮草---"
python grab_transaction_price.py 5151 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5151 ${yesterday} 10

echo "---水浒-宋江---"
python grab_transaction_price.py 5181 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5181 ${yesterday} 10

echo "---投名状---"
python grab_transaction_price.py 5228 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5228 ${yesterday} 10

echo "---梁山军---"
python grab_transaction_price.py 5244 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5244 ${yesterday} 10

echo "---宋兵---"
python grab_transaction_price.py 5253 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5253 ${yesterday} 10

echo "---蹴鞠---"
python grab_transaction_price.py 5257 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5257 ${yesterday} 10

echo "---水浒-刘唐---"
python grab_transaction_price.py 5262 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5262 ${yesterday} 10

echo "---水浒-阎婆惜---"
python grab_transaction_price.py 5245 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5245 ${yesterday} 10

echo "---龙牌---"
python grab_transaction_price.py 5295 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5295 ${yesterday} 10

echo "---宋徽宗---"
python grab_transaction_price.py 5296 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5296 ${yesterday} 10

echo "---水浒-柴进---"
python grab_transaction_price.py 5280 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5280 ${yesterday} 10

echo "---王伦---"
python grab_transaction_price.py 5305 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5305 ${yesterday} 10

echo "---水浒-卢俊义---"
python grab_transaction_price.py 5313 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5313 ${yesterday} 10

echo "---神医安道全---"
python grab_transaction_price.py 5259 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5259 ${yesterday} 10

echo "---水浒-段景住---"
python grab_transaction_price.py 5306 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5306 ${yesterday} 10

echo "---水浒-朱仝---"
python grab_transaction_price.py 5285 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5285 ${yesterday} 10

echo "---神秘隧道通行凭证---"
python grab_transaction_price.py 5317 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5317 ${yesterday} 10

echo "---燃料---"
python grab_transaction_price.py 5321 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5321 ${yesterday} 10

echo "---朝廷-韩存保---"
python grab_transaction_price.py 5312 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5312 ${yesterday} 10

echo "---水浒-李俊---"
python grab_transaction_price.py 5290 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5290 ${yesterday} 10

echo "---照夜玉狮子---"
python grab_transaction_price.py 5319 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5319 ${yesterday} 10

echo "---陨石---"
python grab_transaction_price.py 5330 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5330 ${yesterday} 10

echo "---曾弄---"
python grab_transaction_price.py 5336 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5336 ${yesterday} 10

echo "---四库全书-宋史---"
python grab_transaction_price.py 5325 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5325 ${yesterday} 10

echo "---金朝-完颜阿骨打---"
python grab_transaction_price.py 5337 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5337 ${yesterday} 10

echo "---慧星---"
python grab_transaction_price.py 5350 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5350 ${yesterday} 10

echo "---土星---"
python grab_transaction_price.py 5358 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5358 ${yesterday} 10

echo "---地球---"
python grab_transaction_price.py 5362 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5362 ${yesterday} 10

echo "---水浒-张顺---"
python grab_transaction_price.py 5348 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5348 ${yesterday} 10

echo "---爱之星---"
python grab_transaction_price.py 5365 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5365 ${yesterday} 10

echo "---探索飞船-启航号---"
python grab_transaction_price.py 5367 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5367 ${yesterday} 10

echo "---文房四宝-笔---"
python grab_transaction_price.py 5368 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5368 ${yesterday} 10

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
echo "---龙腾华夏---"
python grab_transaction_price.py 4993 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 4993 ${yesterday} 10

echo "---山海经-獙獙---"
python grab_transaction_price.py 5027 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5027 ${yesterday} 10

echo "---桥明月夜---"
python grab_transaction_price.py 5021 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5021 ${yesterday} 10

echo "---星辰奇遇---"
python grab_transaction_price.py 5098 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5098 ${yesterday} 10

echo "---晨曦初现---"
python grab_transaction_price.py 5187 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5187 ${yesterday} 10

echo "---风饶卡片---"
python grab_transaction_price.py 5267 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5267 ${yesterday} 10

echo "---绿野多娇---"
python grab_transaction_price.py 5281 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5281 ${yesterday} 10

echo "---山河令---"
python grab_transaction_price.py 5293 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5293 ${yesterday} 10

echo "---侠客行---"
python grab_transaction_price.py 5297 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5297 ${yesterday} 10

echo "---龙啸乾坤---"
python grab_transaction_price.py 5298 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5298 ${yesterday} 10

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
echo "---影龙卫---"
python grab_transaction_price.py 5149 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5149 ${yesterday} 10

echo "---龙之遗骸---"
python grab_transaction_price.py 5191 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5191 ${yesterday} 10

echo "---伊甸园---"
python grab_transaction_price.py 5209 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5209 ${yesterday} 10

echo "---夏娃---"
python grab_transaction_price.py 5222 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5222 ${yesterday} 10

echo "---亚当---"
python grab_transaction_price.py 5221 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5221 ${yesterday} 10

echo "---上帝-合成资格卡---"
python grab_transaction_price.py 5225 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 5225 ${yesterday} 10

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-N-MengYouGeLou" "1-N-YouLingTianTai" "1-N-ChaoNengMoJing" \
"1-SR-QuanJiShouTao" "1-SSR-ChaoShanDianCi" "1-WeiGuangFeiTan" "1-ShuGuangLuJian" \
"2-UR-ShiKongChuanSuoJi" "2-UR-YueQiuShangCheng" "2-DaMoHuanShi" "2-JinLianLingZhan" \
"2-ZaiFuXiangHuang" "2-LongYinWanXiang" "2-JinQuXiYin" "2-YiShouFuTu" "2-JiuChongTianWaiTian" \
"3-ZhongYiWuSheng" "3-ChuFengMingTong" "3-ChongHuoFeiYan" \
"3-HuBenZhanXue" "3-YinXuJianDao" "3-FengDengBaiGu" "3-YongMengShuBing" "3-KuaiHuRen" "3-RuiFengJianLing" "3-YunYuYangFeng" \
"5-ShuiHu-WuYong" "5-JunJiChu" "5-JiuSi" "5-ShuiHu-ZhuTong" "5-YunShi" \
"5-ShiZiPoRouBaoZiPu" "5-BaoZi" "5-ShuiHu-LiJun" "5-ZhaoYeYuShiZi" \
"5-Jiu" "5-LiangCao" "5-TouMingZhuang" "5-ShuiHu-LiuTang" "5-SongHuiZong" \
"5-ShuiHu-SongJiang" "5-LiangShanJun" "5-ShuiHu-ChaiJin" "5-ShenYiAnDaoQuan" \
"5-SongBing" "5-CuJu" "5-ShuiHu-YanPoXi" "5-LongPai" "5-DiQiu" "5-ShuiHu-ZhangShun" \
"5-RanLiao" "5-ChaoTing-HanCunBao" "5-ZengNong" "5-AiZhiXing" \
"5-WangLun" "5-ShuiHu-LuJunYi" "5-ShuiHu-DuanJingZhu" "5-ShenMiSuiDaoTongXingPingZheng" \
"5-SiKuQuanShu-SongShi" "5-JinChao-WanYanAGuDa" "5-WenFangSiBao-Bi" \
"5-HuiXing" "5-TuXing" "5-TanSuoFeiChuan-QiHangHao" \
"6-SaiBoQiFeiKa" "6-EMoXunZhang"  "6-SaiBoNiYu" "6-SaiBoTopOne" "6-SaiBoTop" "6-SaiBoPoYiHeXin" \
"6-SaiBoJiangZiYa" "6-SaiBoKawasaki" \
"7-XiangSuQiJing" "7-TanXianZheIV" "7-XunBaoZheI" "7-GongYunXiaoShao" "7-FangBiaoZhiShiDeng" "7-YeGuWangCheng" \
"8-QiaoMingYueYe" "8-XingChenQiYu"  "8-LongTengHuaXia" "8-ShanHaiJing-BiBi" \
"8-ChenXiChuXian" "8-FengRaoKaPian" "8-LvYeDuoJiao" "8-ShanHeLing" \
"8-LongXiaoQianKun" "8-XiaKeXing" \
"9-WeiLaiShuJu" "9-ChaoJiNengLiang" "9-WeiLaiShiDai" "9-ShenYuanZhenSheZhe20" \
"9-ShuJuDaiMa" "9-XuKongZhanShenKaEr" "9-JiuJiKongJuZhiMen" "9-WeiLaiTanXianJiaEZ" \
"9-EMoZhiWangATuo" "9-XiaoLunLun"  \
"10-YingLongWei" "10-XiaWa" "10-YaDang" "10-ShangDi-HeChengZiGeKa" \
"10-LongZhiYiHai" "10-YiDianYuan"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
#python agg_special_transactions.py ${yesterday}
#python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
