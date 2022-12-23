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
tag=`date +%Y%m%d%H`

echo "------${tag}------"

echo "---计算市值---"
python calc_market_value.py ${tag}

echo "---启源I开拓者号---"
python grab_transaction_price.py 54 ${today} ${tag}

echo "---万象龙巢---"
python grab_transaction_price.py 59 ${today} ${tag}

echo "---空间补给站-启能版---"
python grab_transaction_price.py 39 ${today} ${tag}

echo "---云木守护版---"
python grab_transaction_price.py 57 ${today} ${tag}

echo "---小小键盘-Ctrl仔---"
python grab_transaction_price.py 56 ${today} ${tag}

echo "---小小键盘-C仔---"
python grab_transaction_price.py 67 ${today} ${tag}

echo "---小小键盘-V仔---"
python grab_transaction_price.py 66 ${today} ${tag}

echo "---小小键盘-Shift仔---"
python grab_transaction_price.py 60 ${today} ${tag}

echo "---传说奇遇-太空Shift仔---"
python grab_transaction_price.py 61 ${today} ${tag}

echo "---山丘龙灵-厚土---"
python grab_transaction_price.py 31 ${today} ${tag}

echo "---河流龙灵-甘霖---"
python grab_transaction_price.py 32 ${today} ${tag}

echo "---焰火龙灵-灰烬---"
python grab_transaction_price.py 33 ${today} ${tag}

echo "---金晶龙灵-浮金---"
python grab_transaction_price.py 30 ${today} ${tag}

echo "---国庆节限定空投-龙凤筷---"
python grab_transaction_price.py 75 ${today} ${tag}

echo "---龙图腾---"
python grab_transaction_price.py 79 ${today} ${tag}

echo "---龙凤守宝---"
python grab_transaction_price.py 80 ${today} ${tag}

#echo "---探索者I---"
#python grab_transaction_price.py 82 ${today} ${tag}

#echo "---探索者II---"
#python grab_transaction_price.py 231 ${today} ${tag}

echo "---探索者III---"
python grab_transaction_price.py 592 ${today} ${tag}

#echo "---探索者-Ctrl---"
#python grab_transaction_price.py 83 ${today} ${tag}

#echo "---探索者-Shift---"
#python grab_transaction_price.py 84 ${today} ${tag}

echo "---物资传输面板---"
python grab_transaction_price.py 28 ${today} ${tag}

echo "---栖龙云木---"
python grab_transaction_price.py 29 ${today} ${tag}

echo "---梦幻小龙---"
python grab_transaction_price.py 46 ${today} ${tag}

echo "---山岭树龙---"
python grab_transaction_price.py 55 ${today} ${tag}

echo "---凤图腾---"
python grab_transaction_price.py 87 ${today} ${tag}

echo "---阿尔法之眼---"
python grab_transaction_price.py 94 ${today} ${tag}

echo "---魂魄提灯---"
python grab_transaction_price.py 95 ${today} ${tag}

echo "---涅槃之地---"
python grab_transaction_price.py 96 ${today} ${tag}

echo "---奇物碎片-时间磨盘---"
python grab_transaction_price.py 100 ${today} ${tag}

echo "---奇物秘宝-时间磨盘---"
python grab_transaction_price.py 99 ${today} ${tag}

echo "---凤翊泪---"
python grab_transaction_price.py 101 ${today} ${tag}

echo "---国庆节限定空投-平安果---"
python grab_transaction_price.py 71 ${today} ${tag}

echo "---国庆节限定空投-抚琴---"
python grab_transaction_price.py 72 ${today} ${tag}

#echo "---电子通行证---"
#python grab_transaction_price.py 104 ${today} ${tag}

#echo "---充盈不老泉---"
#python grab_transaction_price.py 105 ${today} ${tag}

#echo "---一抨时之砂---"
#python grab_transaction_price.py 106 ${today} ${tag}

echo "---拾荒者---"
python grab_transaction_price.py 111 ${today} ${tag}

echo "---SR-彩猴之神---"
python grab_transaction_price.py 65 ${today} ${tag}

echo "---R-猴格丽特---"
python grab_transaction_price.py 64 ${today} ${tag}

echo "---R-PD猴---"
python grab_transaction_price.py 63 ${today} ${tag}

echo "---N-包租猴---"
python grab_transaction_price.py 62 ${today} ${tag}

#echo "---奇异龙蛋---"
#python grab_transaction_price.py 112 ${today} ${tag}

echo "---虫族骸骨---"
python grab_transaction_price.py 130 ${today} ${tag}

echo "---X型能源电池---"
python grab_transaction_price.py 129 ${today} ${tag}

echo "---罗盘指针---"
python grab_transaction_price.py 128 ${today} ${tag}

echo "---云木方舟---"
python grab_transaction_price.py 140 ${today} ${tag}

echo "---晶石碎块-未鉴定---"
python grab_transaction_price.py 134 ${today} ${tag}

echo "---合金---"
python grab_transaction_price.py 148 ${today} ${tag}

echo "---奇物秘宝-非礼勿听木匣---"
python grab_transaction_price.py 132 ${today} ${tag}

echo "---建木---"
python grab_transaction_price.py 150 ${today} ${tag}

echo "---琉璃---"
python grab_transaction_price.py 151 ${today} ${tag}

echo "---启源II聚能号---"
python grab_transaction_price.py 154 ${today} ${tag}

echo "---奇物秘宝-青铜石像---"
python grab_transaction_price.py 126 ${today} ${tag}

echo "---垂钓许可---"
python grab_transaction_price.py 153 ${today} ${tag}

echo "---小小键盘-Enter仔---"
python grab_transaction_price.py 156 ${today} ${tag}

echo "---国庆节限定空投-可乐---"
python grab_transaction_price.py 74 ${today} ${tag}

echo "---国庆节限定空投-缘结---"
python grab_transaction_price.py 73 ${today} ${tag}

echo "---奇物秘宝-蓝海幽蝶---"
python grab_transaction_price.py 155 ${today} ${tag}

##echo "---鱼饵---"
##python grab_transaction_price.py 172 ${today} ${tag}

##echo "---鱼饵-兑换版本---"
##python grab_transaction_price.py 210 ${today} ${tag}

##echo "---精致的钓具-空投版本---"
##python grab_transaction_price.py 169 ${today} ${tag}

##echo "---精致的钓具-兑换版本---"
##python grab_transaction_price.py 164 ${today} ${tag}

#echo "---巡航者-空投版本---"
#python grab_transaction_price.py 170 ${today} ${tag}

#echo "---巡航者-兑换版本---"
#python grab_transaction_price.py 159 ${today} ${tag}

echo "---巡航者I---"
python grab_transaction_price.py 590 ${today} ${tag}

echo "---梦幻水龙---"
python grab_transaction_price.py 205 ${today} ${tag}

#echo "---深海气泡---"
#python grab_transaction_price.py 211 ${today} ${tag}

echo "---快捷组合-复制---"
python grab_transaction_price.py 77 ${today} ${tag}

echo "---快捷组合-粘贴---"
python grab_transaction_price.py 76 ${today} ${tag}

echo "---深海晶石---"
python grab_transaction_price.py 201 ${today} ${tag}

echo "---第九区证件---"
python grab_transaction_price.py 198 ${today} ${tag}

echo "---机械厚土---"
python grab_transaction_price.py 223 ${today} ${tag}

echo "---组队卡I---"
python grab_transaction_price.py 232 ${today} ${tag}

echo "---修补学徒---"
python grab_transaction_price.py 183 ${today} ${tag}

echo "---鉴宝学徒---"
python grab_transaction_price.py 185 ${today} ${tag}

echo "---星辉殿---"
python grab_transaction_price.py 186 ${today} ${tag}

echo "---寒月寺---"
python grab_transaction_price.py 230 ${today} ${tag}

echo "---福至宝珠---"
python grab_transaction_price.py 258 ${today} ${tag}

echo "---噩梦果实---"
python grab_transaction_price.py 133 ${today} ${tag}

echo "---狩猎者---"
python grab_transaction_price.py 260 ${today} ${tag}

echo "---流光魔方-青金---"
python grab_transaction_price.py 242 ${today} ${tag}

#echo "---普通武器---"
#python grab_transaction_price.py 266 ${today} ${tag}

#echo "---传送戒指-龙血熔洞---"
#python grab_transaction_price.py 272 ${today} ${tag}

#echo "---传送戒指-尖啸废墟---"
#python grab_transaction_price.py 271 ${today} ${tag}

#echo "---传送戒指-飓风峡谷---"
#python grab_transaction_price.py 270 ${today} ${tag}

#echo "---精致武器---"
#python grab_transaction_price.py 268 ${today} ${tag}

echo "---传说武器---"
python grab_transaction_price.py 275 ${today} ${tag}

echo "---智慧之心---"
python grab_transaction_price.py 259 ${today} ${tag}

echo "---意志之心---"
python grab_transaction_price.py 281 ${today} ${tag}

echo "---炼金学徒---"
python grab_transaction_price.py 184 ${today} ${tag}

echo "---流光魔方-珊瑚---"
python grab_transaction_price.py 241 ${today} ${tag}

echo "---启源改-忘川飓风---"
python grab_transaction_price.py 453 ${today} ${tag}

echo "---未鉴定的武器图纸---"
python grab_transaction_price.py 203 ${today} ${tag}

#echo "---神兔-铜蛋---"
#python grab_transaction_price.py 474 ${today} ${tag}

#echo "---神兔-银蛋---"
#python grab_transaction_price.py 479 ${today} ${tag}

echo "---暗黑灵鸽---"
python grab_transaction_price.py 388 ${today} ${tag}

#echo "---神兔-金蛋---"
#python grab_transaction_price.py 526 ${today} ${tag}

echo "---冒险者之心---"
python grab_transaction_price.py 380 ${today} ${tag}

echo "---答题卡---"
python grab_transaction_price.py 568 ${today} ${tag}

echo "---磁欧晶碎片---"
python grab_transaction_price.py 187 ${today} ${tag}

echo "---天成仪---"
python grab_transaction_price.py 269 ${today} ${tag}

echo "---天成仪II---"
python grab_transaction_price.py 389 ${today} ${tag}

echo "---流光魔方-琥珀---"
python grab_transaction_price.py 243 ${today} ${tag}

echo "---超级巡航者---"
python grab_transaction_price.py 593 ${today} ${tag}

echo "---超级探索者---"
python grab_transaction_price.py 594 ${today} ${tag}

echo "---战甲厚土---"
python grab_transaction_price.py 595 ${today} ${tag}

#------ 后处理 ------#
cd data;mkdir -p upload/$tag;rm -rf upload/$tag/*
mv *$tag* upload/$tag;cd upload/$tag

for nft in "1-KaiTuoZhe" "1-WanXiangLongChao" "1-KongJianBuJi-QiNeng" "1-YunMuShouHu" "2-TaiKongShiftZai" "2-ShiftZai" \
"3-HouTu" "3-GanLin" "3-HuiJin" "3-FuJin" "2-CtrlZai" "2-CZai" "2-VZai" "4-LongFengKuai" "4-LongTuTeng" "1-LongFengShouBao" "4-FengTuTeng" \
"1-ChuanShuMianBan" "1-QiLongYunMu" "1-MengHuanXiaoLong" "1-ShanLingShuLong" "5-AErFaYan" "5-HunPoTiDeng" \
"1-NiePanZhiDi" "5-QiWuSuiPian-ShiJianMoPan" "5-QiWuMiBao-ShiJianMoPan" "5-FengYiLei" "5-TanSuoZheIII"  \
"4-PingAnGuo" "5-ShiHuangZhe" "4-FuQin" "6-SR-CaiHouZhiShen" "6-R-HouGeLiTe" "6-R-PDHou" "6-N-BaoZuHou"  \
"5-ChongZuHaiGu" "5-NengYuanDianChi" "5-LuoPanZhiZhen" "6-YunMuFangZhou" "6-JingShiSuiPian" "7-HeJin" "7-FeiLiWuTingMuXia" \
"7-JianMu" "7-LiuLi" "7-JuNeng" "7-QingTongShiXiang" "7-ChuiDiaoXuKe" "7-EnterZai" "8-KeLe" "8-YuanJie" "8-LanHaiYouDie" \
"8-YuEr" "8-JingZhiDiaoJu-KongTou" "8-JingZhiDiaoJu-DuiHuan" "8-XunHangZheI" "9-MengHuanShuiLong" \
"9-YuEr-DuiHuan" "9-KuaiJieZuHe-FuZhi" "9-KuaiJieZuHe-ZhanTie" "9-ShenHaiJingShi" "9-DiJiuQuZhengJian" \
"9-JiXieHouTu" "9-ZuDuiKaI" "10-XiuBuXueTu" "10-JianBaoXueTu" "10-XingHuiDian" "10-HanYueSi" "10-FuZhiBaoZhu" \
"10-EMengGuoShi" "10-ShouLieZhe" "10-LiuGuangMoFang-QingJin" "11-ChuanShuoWuQi" "11-ZhiHuiZhiXin" "11-YiZhiZhiXin" \
"12-LianJinXueTu" "12-LiuGuangMoFang-ShanHu" "12-QiYuanGai-WangChuanJuFeng" "12-WeiJianDing-WuQiTuZhi" "12-ShenTu-TongDan" \
"12-ShenTu-YinDan" "11-AnHeiLingGe" "12-ShenTu-JinDan" "11-MaoXianZheZhiXin" "12-DaTiKa" "11-CiOuJingSuiPian" "11-TianChengYi" "11-TianChengYiII" \
"13-LiuGuangMoFang-HuPo" "13-ChaoJiXunHangZhe" "13-ChaoJiTanSuoZhe" "13-ZhanJiaHouTu"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$tag $nft/*
done

cd ../../..
python agg_special_transactions.py ${tag}
python agg_special_transactions_external.py ${tag}
python agg_transactions.py ${tag}

#python /mnt/ssd01/git/nft-assistant/GuangYu/upload_baidudisk.py /mnt/ssd01/git/nft-assistant/GuangYu/data/upload/$tag $today/$tag
