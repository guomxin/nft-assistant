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

#echo "---云木守护版---"
#python grab_transaction_price.py 57 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 57 ${yesterday} 50

#echo "---小小键盘-Ctrl仔---"
#python grab_transaction_price.py 56 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 56 ${yesterday} 50

#echo "---小小键盘-C仔---"
#python grab_transaction_price.py 67 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 67 ${yesterday} 50

#echo "---小小键盘-V仔---"
#python grab_transaction_price.py 66 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 66 ${yesterday} 50

#echo "---小小键盘-Shift仔---"
#python grab_transaction_price.py 60 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 60 ${yesterday} 50

echo "---传说奇遇-太空Shift仔---"
python grab_transaction_price.py 61 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 61 ${yesterday} 500

echo "---山丘龙灵-厚土---"
python grab_transaction_price.py 31 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 31 ${yesterday} 50

#echo "---河流龙灵-甘霖---"
#python grab_transaction_price.py 32 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 32 ${yesterday} 100

echo "---焰火龙灵-灰烬---"
python grab_transaction_price.py 33 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 33 ${yesterday} 500

echo "---金晶龙灵-浮金---"
python grab_transaction_price.py 30 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 30 ${yesterday} 500

#echo "---国庆节限定空投-龙凤筷---"
#python grab_transaction_price.py 75 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 75 ${yesterday} 100

echo "---龙图腾---"
python grab_transaction_price.py 79 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 79 ${yesterday} 100

echo "---龙凤守宝---"
python grab_transaction_price.py 80 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 80 ${yesterday} 500

echo "---探索者III---"
python grab_transaction_price.py 592 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 592 ${yesterday} 50

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
python analyze_transaction_prices.py 55 ${yesterday} 100

#echo "---凤图腾---"
#python grab_transaction_price.py 87 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 87 ${yesterday} 100

#echo "---阿尔法之眼---"
#python grab_transaction_price.py 94 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 94 ${yesterday} 500

echo "---魂魄提灯---"
python grab_transaction_price.py 95 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 95 ${yesterday} 50

echo "---涅槃之地---"
python grab_transaction_price.py 96 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 96 ${yesterday} 500

echo "---奇物碎片-时间磨盘---"
python grab_transaction_price.py 100 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 100 ${yesterday} 100

echo "---奇物秘宝-时间磨盘---"
python grab_transaction_price.py 99 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 99 ${yesterday} 100

#echo "---凤翊泪---"
#python grab_transaction_price.py 101 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 101 ${yesterday} 50

#echo "---国庆节限定空投-平安果---"
#python grab_transaction_price.py 71 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 71 ${yesterday} 50

echo "---国庆节限定空投-抚琴---"
python grab_transaction_price.py 72 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 72 ${yesterday} 100

echo "---拾荒者---"
python grab_transaction_price.py 111 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 111 ${yesterday} 100

echo "---SR-彩猴之神---"
python grab_transaction_price.py 65 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 65 ${yesterday} 500

echo "---R-猴格丽特---"
python grab_transaction_price.py 64 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 64 ${yesterday} 100

echo "---R-PD猴---"
python grab_transaction_price.py 63 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 63 ${yesterday} 100

echo "---N-包租猴---"
python grab_transaction_price.py 62 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 62 ${yesterday} 50

echo "---虫族骸骨---"
python grab_transaction_price.py 130 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 130 ${yesterday} 50

#echo "---X型能源电池---"
#python grab_transaction_price.py 129 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 129 ${yesterday} 100

echo "---罗盘指针---"
python grab_transaction_price.py 128 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 128 ${yesterday} 100

echo "---云木方舟---"
python grab_transaction_price.py 140 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 140 ${yesterday} 100

echo "---晶石碎块-未鉴定---"
python grab_transaction_price.py 134 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 134 ${yesterday} 100

#echo "---合金---"
#python grab_transaction_price.py 148 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 148 ${yesterday} 100

echo "---奇物秘宝-非礼勿听木匣---"
python grab_transaction_price.py 132 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 132 ${yesterday} 100

#echo "---建木---"
#python grab_transaction_price.py 150 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 150 ${yesterday} 100

#echo "---琉璃---"
#python grab_transaction_price.py 151 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 151 ${yesterday} 100

echo "---启源II聚能号---"
python grab_transaction_price.py 154 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 154 ${yesterday} 100

echo "---奇物秘宝-青铜石像---"
python grab_transaction_price.py 126 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 126 ${yesterday} 100

echo "---垂钓许可---"
python grab_transaction_price.py 153 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 153 ${yesterday} 100

#echo "---小小键盘-Enter仔---"
#python grab_transaction_price.py 156 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 156 ${yesterday} 100

echo "---国庆节限定空投-可乐---"
python grab_transaction_price.py 74 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 74 ${yesterday} 100

echo "---国庆节限定空投-缘结---"
python grab_transaction_price.py 73 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 73 ${yesterday} 100

echo "---奇物秘宝-蓝海幽蝶---"
python grab_transaction_price.py 155 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 155 ${yesterday} 100

##echo "---鱼饵---"
##python grab_transaction_price.py 172 ${yesterday} ${yesterday}
##python analyze_transaction_prices.py 172 ${yesterday} 50

##echo "---鱼饵-兑换版本---"
##python grab_transaction_price.py 210 ${yesterday} ${yesterday}
##python analyze_transaction_prices.py 210 ${yesterday} 50

##echo "---精致的钓具-空投版本---"
##python grab_transaction_price.py 169 ${yesterday} ${yesterday}
##python analyze_transaction_prices.py 169 ${yesterday} 50

##echo "---精致的钓具-兑换版本---"
##python grab_transaction_price.py 164 ${yesterday} ${yesterday}
##python analyze_transaction_prices.py 164 ${yesterday} 50

echo "---巡航者I---"
python grab_transaction_price.py 590 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 590 ${yesterday} 50

echo "---梦幻水龙---"
python grab_transaction_price.py 205 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 205 ${yesterday} 100

#echo "---深海气泡---"
#python grab_transaction_price.py 211 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 211 ${yesterday} 100

echo "---快捷组合-复制---"
python grab_transaction_price.py 77 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 77 ${yesterday} 100

echo "---快捷组合-粘贴---"
python grab_transaction_price.py 76 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 76 ${yesterday} 100

echo "---第九区证件---"
python grab_transaction_price.py 198 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 198 ${yesterday} 100

#echo "---深海晶石---"
#python grab_transaction_price.py 201 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 201 ${yesterday} 100

echo "---机械厚土---"
python grab_transaction_price.py 223 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 223 ${yesterday} 100

#echo "---组队卡I---"
#python grab_transaction_price.py 232 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 232 ${yesterday} 100

echo "---修补学徒---"
python grab_transaction_price.py 183 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 183 ${yesterday} 500

echo "---鉴宝学徒---"
python grab_transaction_price.py 185 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 185 ${yesterday} 500

echo "---星辉殿---"
python grab_transaction_price.py 186 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 186 ${yesterday} 100

echo "---寒月寺---"
python grab_transaction_price.py 230 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 230 ${yesterday} 100

echo "---福至宝珠---"
python grab_transaction_price.py 258 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 258 ${yesterday} 100

echo "---噩梦果实---"
python grab_transaction_price.py 133 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 133 ${yesterday} 100

echo "---狩猎者---"
python grab_transaction_price.py 260 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 260 ${yesterday} 100

#echo "---流光魔方-青金---"
#python grab_transaction_price.py 242 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 242 ${yesterday} 100

#echo "---普通武器---"
#python grab_transaction_price.py 266 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 266 ${yesterday} 50

#echo "---精致武器---"
#python grab_transaction_price.py 268 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 268 ${yesterday} 50

echo "---传说武器---"
python grab_transaction_price.py 275 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 275 ${yesterday} 100

#echo "---智慧之心---"
#python grab_transaction_price.py 259 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 259 ${yesterday} 100

#echo "---意志之心---"
#python grab_transaction_price.py 281 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 281 ${yesterday} 100

echo "---炼金学徒---"
python grab_transaction_price.py 184 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 184 ${yesterday} 100

#echo "---流光魔方-珊瑚---"
#python grab_transaction_price.py 241 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 241 ${yesterday} 100

echo "---启源改-忘川飓风---"
python grab_transaction_price.py 453 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 453 ${yesterday} 500

#echo "---未鉴定的武器图纸---"
#python grab_transaction_price.py 203 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 203 ${yesterday} 50

#echo "---神兔-铜蛋---"
#python grab_transaction_price.py 474 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 474 ${yesterday} 50

#echo "---神兔-银蛋---"
#python grab_transaction_price.py 479 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 479 ${yesterday} 100

#echo "---暗黑灵鸽---"
#python grab_transaction_price.py 388 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 388 ${yesterday} 50

#echo "---神兔-金蛋---"
#python grab_transaction_price.py 526 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 526 ${yesterday} 500

echo "---冒险者之心---"
python grab_transaction_price.py 380 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 380 ${yesterday} 100

echo "---答题卡---"
python grab_transaction_price.py 568 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 568 ${yesterday} 50

echo "---磁欧晶碎片---"
python grab_transaction_price.py 187 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 187 ${yesterday} 50

echo "---天成仪---"
python grab_transaction_price.py 269 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 269 ${yesterday} 50

echo "---天成仪II---"
python grab_transaction_price.py 389 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 389 ${yesterday} 50

echo "---流光魔方-琥珀---"
python grab_transaction_price.py 243 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 243 ${yesterday} 100

echo "---超级巡航者---"
python grab_transaction_price.py 593 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 593 ${yesterday} 100

echo "---超级探索者---"
python grab_transaction_price.py 594 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 594 ${yesterday} 100

echo "---战甲厚土---"
python grab_transaction_price.py 595 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 595 ${yesterday} 100

echo "---流光宝盒-冷翠---"
python grab_transaction_price.py 246 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 246 ${yesterday} 100

#echo "---冷翠精华---"
#python grab_transaction_price.py 600 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 600 ${yesterday} 100

echo "---MK魔术帽---"
python grab_transaction_price.py 175 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 175 ${yesterday} 100

echo "---MK马卡龙---"
python grab_transaction_price.py 174 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 174 ${yesterday} 100

echo "---MK旋转杯---"
python grab_transaction_price.py 176 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 176 ${yesterday} 100

echo "---MK老爷车---"
python grab_transaction_price.py 173 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 173 ${yesterday} 100

#echo "---PX市民---"
#python grab_transaction_price.py 602 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 602 ${yesterday} 100

#echo "---小小键盘-Z仔---"
#python grab_transaction_price.py 254 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 254 ${yesterday} 100

#echo "---复古手柄---"
#python grab_transaction_price.py 604 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 604 ${yesterday} 50

#echo "---5号电池---"
#python grab_transaction_price.py 605 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 605 ${yesterday} 50

#echo "---选择卡---"
#python grab_transaction_price.py 607 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 607 ${yesterday} 50

echo "---复古红白机---"
python grab_transaction_price.py 608 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 608 ${yesterday} 50

echo "---魔刃-时之逆转---"
python grab_transaction_price.py 611 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 611 ${yesterday} 100

echo "---航海卡---"
python grab_transaction_price.py 664 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 664 ${yesterday} 50

echo "---陆运卡---"
python grab_transaction_price.py 662 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 662 ${yesterday} 50

echo "---指引卡---"
python grab_transaction_price.py 663 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 663 ${yesterday} 50

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-KaiTuoZhe" "1-WanXiangLongChao" "1-KongJianBuJi-QiNeng" "1-YunMuShouHu" "2-TaiKongShiftZai" "2-ShiftZai" \
"3-HouTu" "3-GanLin" "3-HuiJin" "3-FuJin" "2-CtrlZai" "2-CZai" "2-VZai" "4-LongFengKuai" "4-LongTuTeng" "1-LongFengShouBao" "4-FengTuTeng" \
"1-ChuanShuMianBan" "1-QiLongYunMu" "1-MengHuanXiaoLong" "1-ShanLingShuLong" "5-AErFaYan" "5-HunPoTiDeng" \
"1-NiePanZhiDi" "5-QiWuSuiPian-ShiJianMoPan" "5-QiWuMiBao-ShiJianMoPan" "5-FengYiLei" "5-TanSuoZheIII" \
"4-PingAnGuo" "5-ShiHuangZhe" "4-FuQin" "6-SR-CaiHouZhiShen" "6-R-HouGeLiTe" "6-R-PDHou" "6-N-BaoZuHou"  \
"5-ChongZuHaiGu" "5-NengYuanDianChi" "5-LuoPanZhiZhen" "6-YunMuFangZhou" "6-JingShiSuiPian" "7-HeJin" "7-FeiLiWuTingMuXia" \
"7-JianMu" "7-LiuLi" "7-JuNeng" "7-QingTongShiXiang" "7-ChuiDiaoXuKe" "7-EnterZai" "8-KeLe" "8-YuanJie" "8-LanHaiYouDie" \
"8-YuEr" "8-JingZhiDiaoJu-KongTou" "8-JingZhiDiaoJu-DuiHuan" "8-XunHangZheI" "9-MengHuanShuiLong" \
"9-YuEr-DuiHuan" "9-KuaiJieZuHe-FuZhi" "9-KuaiJieZuHe-ZhanTie" "9-ShenHaiJingShi" "9-DiJiuQuZhengJian" \
"9-JiXieHouTu" "9-ZuDuiKaI" "10-XiuBuXueTu" "10-JianBaoXueTu" "10-XingHuiDian" "10-HanYueSi" "10-FuZhiBaoZhu" \
"10-EMengGuoShi" "10-ShouLieZhe" "10-LiuGuangMoFang-QingJin" "11-ChuanShuoWuQi" "11-ZhiHuiZhiXin" "11-YiZhiZhiXin" \
"12-LianJinXueTu" "12-LiuGuangMoFang-ShanHu" "12-QiYuanGai-WangChuanJuFeng" "12-WeiJianDing-WuQiTuZhi" "12-ShenTu-TongDan" \
"12-ShenTu-YinDan" "11-AnHeiLingGe" "12-ShenTu-JinDan" "11-MaoXianZheZhiXin" "12-DaTiKa" "11-CiOuJingSuiPian" "11-TianChengYi" "11-TianChengYiII" \
"13-LiuGuangMoFang-HuPo" "13-ChaoJiXunHangZhe" "13-ChaoJiTanSuoZhe" "13-ZhanJiaHouTu" "13-LiuGuangBaoHe-LengCui" "13-LengCuiJingHua" \
"14-MKMoShuMao" "14-MKMaKaLong" "14-MKXuanZhuanBei" "14-MKLaoYeChe" "14-PXShiMin" "14-ZZai" "14-FuGuShouBing" "14-5HaoDianChi" "14-XuanZeKa" \
"14-FuGuHongBaiJi" "14-MoRen-ShiZhiNiZhuan" "13-HangHaiKa" "13-LuYunKa" "13-ZhiYinKa"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
python agg_special_transactions.py ${yesterday}
python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
