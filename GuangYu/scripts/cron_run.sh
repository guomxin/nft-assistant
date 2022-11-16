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

python scan_circulation_info.py $today

echo "---启源I开拓者号---"
python grab_transaction_price.py 54 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 54 ${yesterday} 100

echo "---万象龙巢---"
python grab_transaction_price.py 59 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 59 ${yesterday} 100

echo "---空间补给站-启能版---"
python grab_transaction_price.py 39 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 39 ${yesterday} 50

echo "---云木守护版---"
python grab_transaction_price.py 57 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 57 ${yesterday} 50

echo "---小小键盘-Ctrl仔---"
python grab_transaction_price.py 56 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 56 ${yesterday} 50

echo "---小小键盘-C仔---"
python grab_transaction_price.py 67 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 67 ${yesterday} 50

echo "---小小键盘-V仔---"
python grab_transaction_price.py 66 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 66 ${yesterday} 50

echo "---小小键盘-Shift仔---"
python grab_transaction_price.py 60 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 60 ${yesterday} 50

echo "---传说奇遇-太空Shift仔---"
python grab_transaction_price.py 61 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 61 ${yesterday} 50

echo "---山丘龙灵-厚土---"
python grab_transaction_price.py 31 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 31 ${yesterday} 50

echo "---河流龙灵-甘霖---"
python grab_transaction_price.py 32 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 32 ${yesterday} 50

echo "---焰火龙灵-灰烬---"
python grab_transaction_price.py 33 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 33 ${yesterday} 100

echo "---金晶龙灵-浮金---"
python grab_transaction_price.py 30 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 30 ${yesterday} 100

echo "---国庆节限定空投-龙凤筷---"
python grab_transaction_price.py 75 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 75 ${yesterday} 50

echo "---龙图腾---"
python grab_transaction_price.py 79 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 79 ${yesterday} 50

echo "---龙凤守宝---"
python grab_transaction_price.py 80 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 80 ${yesterday} 50

echo "---探索者I---"
python grab_transaction_price.py 82 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 82 ${yesterday} 50

#echo "---探索者-Ctrl---"
#python grab_transaction_price.py 83 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 83 ${yesterday} 50

#echo "---探索者-Shift---"
#python grab_transaction_price.py 84 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 84 ${yesterday} 50

echo "---物资传输面板---"
python grab_transaction_price.py 28 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 28 ${yesterday} 50

echo "---栖龙云木---"
python grab_transaction_price.py 29 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 29 ${yesterday} 50

echo "---梦幻小龙---"
python grab_transaction_price.py 46 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 46 ${yesterday} 50

echo "---山岭树龙---"
python grab_transaction_price.py 55 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 55 ${yesterday} 50

echo "---凤图腾---"
python grab_transaction_price.py 87 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 87 ${yesterday} 50

echo "---阿尔法之眼---"
python grab_transaction_price.py 94 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 94 ${yesterday} 100

echo "---魂魄提灯---"
python grab_transaction_price.py 95 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 95 ${yesterday} 50

echo "---涅槃之地---"
python grab_transaction_price.py 96 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 96 ${yesterday} 100

echo "---奇物碎片-时间磨盘---"
python grab_transaction_price.py 100 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 100 ${yesterday} 50

echo "---奇物秘宝-时间磨盘---"
python grab_transaction_price.py 99 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 99 ${yesterday} 100

echo "---凤翊泪---"
python grab_transaction_price.py 101 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 101 ${yesterday} 50

echo "---国庆节限定空投-平安果---"
python grab_transaction_price.py 71 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 71 ${yesterday} 50

echo "---国庆节限定空投-抚琴---"
python grab_transaction_price.py 72 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 72 ${yesterday} 50

#echo "---电子通行证---"
#python grab_transaction_price.py 104 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 104 ${yesterday} 50

#echo "---充盈不老泉---"
#python grab_transaction_price.py 105 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 105 ${yesterday} 50

#echo "---一抨时之砂---"
#python grab_transaction_price.py 106 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 106 ${yesterday} 50

echo "---拾荒者---"
python grab_transaction_price.py 111 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 111 ${yesterday} 100

echo "---SR-彩猴之神---"
python grab_transaction_price.py 65 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 65 ${yesterday} 100

echo "---R-猴格丽特---"
python grab_transaction_price.py 64 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 64 ${yesterday} 100

echo "---R-PD猴---"
python grab_transaction_price.py 63 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 63 ${yesterday} 100

echo "---N-包租猴---"
python grab_transaction_price.py 62 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 62 ${yesterday} 50

#echo "---奇异龙蛋---"
#python grab_transaction_price.py 112 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 112 ${yesterday} 100

echo "---虫族骸骨---"
python grab_transaction_price.py 130 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 130 ${yesterday} 50

echo "---X型能源电池---"
python grab_transaction_price.py 129 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 129 ${yesterday} 100

echo "---罗盘指针---"
python grab_transaction_price.py 128 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 128 ${yesterday} 100

echo "---云木方舟---"
python grab_transaction_price.py 140 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 140 ${yesterday} 100

echo "---晶石碎块-未鉴定---"
python grab_transaction_price.py 134 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 134 ${yesterday} 100

echo "---合金---"
python grab_transaction_price.py 148 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 148 ${yesterday} 100

echo "---奇物秘宝-非礼勿听木匣---"
python grab_transaction_price.py 132 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 132 ${yesterday} 100

echo "---建木---"
python grab_transaction_price.py 150 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 150 ${yesterday} 100

echo "---琉璃---"
python grab_transaction_price.py 151 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 151 ${yesterday} 100

echo "---启源II聚能号---"
python grab_transaction_price.py 154 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 154 ${yesterday} 100

echo "---奇物秘宝-青铜石像---"
python grab_transaction_price.py 126 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 126 ${yesterday} 100

echo "---垂钓许可---"
python grab_transaction_price.py 153 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 153 ${yesterday} 100

echo "---小小键盘-Enter仔---"
python grab_transaction_price.py 156 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 156 ${yesterday} 100

echo "---国庆节限定空投-可乐---"
python grab_transaction_price.py 74 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 74 ${yesterday} 100

echo "---国庆节限定空投-缘结---"
python grab_transaction_price.py 73 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 73 ${yesterday} 100

echo "---奇物秘宝-蓝海幽蝶---"
python grab_transaction_price.py 155 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 155 ${yesterday} 500

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-KaiTuoZhe" "1-WanXiangLongChao" "1-KongJianBuJi-QiNeng" "1-YunMuShouHu" "2-TaiKongShiftZai" "2-ShiftZai" \
"3-HouTu" "3-GanLin" "3-HuiJin" "3-FuJin" "2-CtrlZai" "2-CZai" "2-VZai" "4-LongFengKuai" "4-LongTuTeng" "1-LongFengShouBao" "4-FengTuTeng" \
"1-ChuanShuMianBan" "1-QiLongYunMu" "1-MengHuanXiaoLong" "1-ShanLingShuLong" "5-AErFaYan" "5-HunPoTiDeng" \
"5-TanSuoZhe-Ctrl" "5-TanSuoZhe-Shift" "1-NiePanZhiDi" "5-QiWuSuiPian-ShiJianMoPan" "5-QiWuMiBao-ShiJianMoPan" "5-FengYiLei" \
"4-PingAnGuo" "5-ShiHuangZhe" "4-FuQin" "6-SR-CaiHouZhiShen" "6-R-HouGeLiTe" "6-R-PDHou" "6-N-BaoZuHou"  \
"5-ChongZuHaiGu" "5-NengYuanDianChi" "5-LuoPanZhiZhen" "6-YunMuFangZhou" "6-JingShiSuiPian" "7-HeJin" "7-FeiLiWuTingMuXia" \
"7-JianMu" "7-LiuLi" "7-JuNeng" "7-QingTongShiXiang" "7-ChuiDiaoXuKe" "7-EnterZai" "8-KeLe" "8-YuanJie" "8-LanHaiYouDie"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
python agg_special_transactions.py ${yesterday}
python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
