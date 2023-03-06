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

#echo "---云木守护版---"
#python grab_transaction_price.py 57 ${today} ${tag}

#echo "---小小键盘-Ctrl仔---"
#python grab_transaction_price.py 56 ${today} ${tag}

#echo "---小小键盘-C仔---"
#python grab_transaction_price.py 67 ${today} ${tag}

#echo "---小小键盘-V仔---"
#python grab_transaction_price.py 66 ${today} ${tag}

#echo "---小小键盘-Shift仔---"
#python grab_transaction_price.py 60 ${today} ${tag}

echo "---传说奇遇-太空Shift仔---"
python grab_transaction_price.py 61 ${today} ${tag}

echo "---山丘龙灵-厚土---"
python grab_transaction_price.py 31 ${today} ${tag}

#echo "---河流龙灵-甘霖---"
#python grab_transaction_price.py 32 ${today} ${tag}

echo "---焰火龙灵-灰烬---"
python grab_transaction_price.py 33 ${today} ${tag}

echo "---金晶龙灵-浮金---"
python grab_transaction_price.py 30 ${today} ${tag}

#echo "---国庆节限定空投-龙凤筷---"
#python grab_transaction_price.py 75 ${today} ${tag}

echo "---龙图腾---"
python grab_transaction_price.py 79 ${today} ${tag}

echo "---龙凤守宝---"
python grab_transaction_price.py 80 ${today} ${tag}

echo "---探索者III---"
python grab_transaction_price.py 592 ${today} ${tag}

echo "---物资传输面板---"
python grab_transaction_price.py 28 ${today} ${tag}

echo "---栖龙云木---"
python grab_transaction_price.py 29 ${today} ${tag}

echo "---梦幻小龙---"
python grab_transaction_price.py 46 ${today} ${tag}

echo "---山岭树龙---"
python grab_transaction_price.py 55 ${today} ${tag}

#echo "---凤图腾---"
#python grab_transaction_price.py 87 ${today} ${tag}

#echo "---阿尔法之眼---"
#python grab_transaction_price.py 94 ${today} ${tag}

echo "---魂魄提灯---"
python grab_transaction_price.py 95 ${today} ${tag}

echo "---涅槃之地---"
python grab_transaction_price.py 96 ${today} ${tag}

echo "---奇物碎片-时间磨盘---"
python grab_transaction_price.py 100 ${today} ${tag}

echo "---奇物秘宝-时间磨盘---"
python grab_transaction_price.py 99 ${today} ${tag}

#echo "---凤翊泪---"
#python grab_transaction_price.py 101 ${today} ${tag}

#echo "---国庆节限定空投-平安果---"
#python grab_transaction_price.py 71 ${today} ${tag}

echo "---国庆节限定空投-抚琴---"
python grab_transaction_price.py 72 ${today} ${tag}

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

echo "---虫族骸骨---"
python grab_transaction_price.py 130 ${today} ${tag}

#echo "---X型能源电池---"
#python grab_transaction_price.py 129 ${today} ${tag}

echo "---罗盘指针---"
python grab_transaction_price.py 128 ${today} ${tag}

echo "---云木方舟---"
python grab_transaction_price.py 140 ${today} ${tag}

echo "---晶石碎块-未鉴定---"
python grab_transaction_price.py 134 ${today} ${tag}

#echo "---合金---"
#python grab_transaction_price.py 148 ${today} ${tag}

echo "---奇物秘宝-非礼勿听木匣---"
python grab_transaction_price.py 132 ${today} ${tag}

#echo "---建木---"
#python grab_transaction_price.py 150 ${today} ${tag}

#echo "---琉璃---"
#python grab_transaction_price.py 151 ${today} ${tag}

echo "---启源II聚能号---"
python grab_transaction_price.py 154 ${today} ${tag}

echo "---奇物秘宝-青铜石像---"
python grab_transaction_price.py 126 ${today} ${tag}

echo "---垂钓许可---"
python grab_transaction_price.py 153 ${today} ${tag}

#echo "---小小键盘-Enter仔---"
#python grab_transaction_price.py 156 ${today} ${tag}

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

#echo "---深海晶石---"
#python grab_transaction_price.py 201 ${today} ${tag}

echo "---第九区证件---"
python grab_transaction_price.py 198 ${today} ${tag}

echo "---机械厚土---"
python grab_transaction_price.py 223 ${today} ${tag}

#echo "---组队卡I---"
#python grab_transaction_price.py 232 ${today} ${tag}

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

#echo "---流光魔方-青金---"
#python grab_transaction_price.py 242 ${today} ${tag}

#echo "---普通武器---"
#python grab_transaction_price.py 266 ${today} ${tag}

#echo "---精致武器---"
#python grab_transaction_price.py 268 ${today} ${tag}

echo "---传说武器---"
python grab_transaction_price.py 275 ${today} ${tag}

#echo "---智慧之心---"
#python grab_transaction_price.py 259 ${today} ${tag}

#echo "---意志之心---"
#python grab_transaction_price.py 281 ${today} ${tag}

echo "---炼金学徒---"
python grab_transaction_price.py 184 ${today} ${tag}

#echo "---流光魔方-珊瑚---"
#python grab_transaction_price.py 241 ${today} ${tag}

echo "---启源改-忘川飓风---"
python grab_transaction_price.py 453 ${today} ${tag}

#echo "---未鉴定的武器图纸---"
#python grab_transaction_price.py 203 ${today} ${tag}

#echo "---神兔-铜蛋---"
#python grab_transaction_price.py 474 ${today} ${tag}

#echo "---神兔-银蛋---"
#python grab_transaction_price.py 479 ${today} ${tag}

#echo "---暗黑灵鸽---"
#python grab_transaction_price.py 388 ${today} ${tag}

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

echo "---流光宝盒-冷翠---"
python grab_transaction_price.py 246 ${today} ${tag}

#echo "---冷翠精华---"
#python grab_transaction_price.py 600 ${today} ${tag}

echo "---MK魔术帽---"
python grab_transaction_price.py 175 ${today} ${tag}

echo "---MK马卡龙---"
python grab_transaction_price.py 174 ${today} ${tag}

echo "---MK旋转杯---"
python grab_transaction_price.py 176 ${today} ${tag}

echo "---MK老爷车---"
python grab_transaction_price.py 173 ${today} ${tag}

#echo "---PX市民---"
#python grab_transaction_price.py 602 ${today} ${tag}

#echo "---小小键盘-Z仔---"
#python grab_transaction_price.py 254 ${today} ${tag}

#echo "---复古手柄---"
#python grab_transaction_price.py 604 ${today} ${tag}

#echo "---5号电池---"
#python grab_transaction_price.py 605 ${today} ${tag}

#echo "---选择卡---"
#python grab_transaction_price.py 607 ${today} ${tag}

echo "---复古红白机---"
python grab_transaction_price.py 608 ${today} ${tag}

echo "---魔刃-时之逆转---"
python grab_transaction_price.py 611 ${today} ${tag}

#echo "---航海卡---"
#python grab_transaction_price.py 664 ${today} ${tag}

#echo "---陆运卡---"
#python grab_transaction_price.py 662 ${today} ${tag}

#echo "---指引卡---"
#python grab_transaction_price.py 663 ${today} ${tag}

echo "---新春福袋---"
python grab_transaction_price.py 736 ${today} ${tag}

echo "---双蛇杖---"
python grab_transaction_price.py 615 ${today} ${tag}

echo "---白骨草---"
python grab_transaction_price.py 614 ${today} ${tag}

echo "---转轮盘---"
python grab_transaction_price.py 754 ${today} ${tag}

echo "---小瓶鱼泪---"
python grab_transaction_price.py 240 ${today} ${tag}

#echo "---四喜折扇---"
#python grab_transaction_price.py 711 ${today} ${tag}

echo "---花草团---"
python grab_transaction_price.py 792 ${today} ${tag}

echo "---圣树种子---"
python grab_transaction_price.py 793 ${today} ${tag}

echo "---魔法药水---"
python grab_transaction_price.py 709 ${today} ${tag}

echo "---永生之花---"
python grab_transaction_price.py 715 ${today} ${tag}

echo "---永生守门人---"
python grab_transaction_price.py 815 ${today} ${tag}

#echo "---小精灵-内测资格卡---"
#python grab_transaction_price.py 844 ${today} ${tag}

echo "---混沌土---"
python grab_transaction_price.py 854 ${today} ${tag}

#echo "---黄金树-有灵---"
#python grab_transaction_price.py 855 ${today} ${tag}

echo "---次空间拉链---"
python grab_transaction_price.py 853 ${today} ${tag}

#echo "---祈愿卡---"
#python grab_transaction_price.py 861 ${today} ${tag}

echo "---缚骨圆环---"
python grab_transaction_price.py 856 ${today} ${tag}

echo "---时间---"
python grab_transaction_price.py 865 ${today} ${tag}

echo "---灵蛇珠---"
python grab_transaction_price.py 616 ${today} ${tag}

echo "---魔光骨冕---"
python grab_transaction_price.py 867 ${today} ${tag}

echo "---小小键盘-Tab仔---"
python grab_transaction_price.py 895 ${today} ${tag}

echo "---神秘石板---"
python grab_transaction_price.py 398 ${today} ${tag}

#echo "---猩红宝石---"
#python grab_transaction_price.py 127 ${today} ${tag}

echo "---森之息---"
python grab_transaction_price.py 896 ${today} ${tag}

#echo "---黄金树-圣树---"
#python grab_transaction_price.py 894 ${today} ${tag}

echo "---血菩提---"
python grab_transaction_price.py 402 ${today} ${tag}

echo "---未觉者---"
python grab_transaction_price.py 459 ${today} ${tag}

echo "---觉醒者---"
python grab_transaction_price.py 458 ${today} ${tag}

echo "---撕裂者---"
python grab_transaction_price.py 457 ${today} ${tag}

echo "---吞噬者---"
python grab_transaction_price.py 456 ${today} ${tag}

echo "---灵智者---"
python grab_transaction_price.py 455 ${today} ${tag}

echo "---封魔灵树---"
python grab_transaction_price.py 897 ${today} ${tag}

echo "---流苏玉坠---"
python grab_transaction_price.py 902 ${today} ${tag}

echo "---黄金圣树---"
python grab_transaction_price.py 899 ${today} ${tag}

echo "---八方来风---"
python grab_transaction_price.py 923 ${today} ${tag}

echo "---八宝糯米饭---"
python grab_transaction_price.py 713 ${today} ${tag}

echo "---聚宝神树---"
python grab_transaction_price.py 898 ${today} ${tag}

echo "---未来研究院---"
python grab_transaction_price.py 113 ${today} ${tag}

echo "---万能小键盘---"
python grab_transaction_price.py 931 ${today} ${tag}

echo "---镜花碎片---"
python grab_transaction_price.py 889 ${today} ${tag}

echo "---键盘领袖---"
python grab_transaction_price.py 932 ${today} ${tag}

echo "---星河念---"
python grab_transaction_price.py 135 ${today} ${tag}

echo "---小小键盘-A仔---"
python grab_transaction_price.py 901 ${today} ${tag}

echo "---长生竹---"
python grab_transaction_price.py 1122 ${today} ${tag}

echo "---神秘泉水---"
python grab_transaction_price.py 1123 ${today} ${tag}

echo "---精美点心盒---"
python grab_transaction_price.py 1085 ${today} ${tag}

echo "---点灯器---"
python grab_transaction_price.py 1207 ${today} ${tag}

echo "---镜中花---"
python grab_transaction_price.py 888 ${today} ${tag}

echo "---初心者布衣---"
python grab_transaction_price.py 1127 ${today} ${tag}

echo "---两界灯---"
python grab_transaction_price.py 1124 ${today} ${tag}

echo "---降临岛信物---"
python grab_transaction_price.py 1320 ${today} ${tag}

#------ 工人 ------#
#echo "---巧克力工人---"
#python grab_transaction_price.py 1256 ${today} ${tag}

#echo "---面包工人---"
#python grab_transaction_price.py 1258 ${today} ${tag}

#echo "---布丁工人---"
#python grab_transaction_price.py 1260 ${today} ${tag}

#echo "---棉花糖工人---"
#python grab_transaction_price.py 1259 ${today} ${tag}

#echo "---奶油工人---"
#python grab_transaction_price.py 1257 ${today} ${tag}
#------ 工人 ------#

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
"12-ShenTu-YinDan" "11-AnHeiLingGe" "12-ShenTu-JinDan" "11-MaoXianZheZhiXin" "12-DaTiKa" "11-CiOuJingSuiPian" "11-TianChengYiII" "11-TianChengYi" \
"13-LiuGuangMoFang-HuPo" "13-ChaoJiXunHangZhe" "13-ChaoJiTanSuoZhe" "13-ZhanJiaHouTu" "13-LiuGuangBaoHe-LengCui" "13-LengCuiJingHua" \
"14-MKMoShuMao" "14-MKMaKaLong" "14-MKXuanZhuanBei" "14-MKLaoYeChe" "14-PXShiMin" "14-ZZai" "14-FuGuShouBing" "14-5HaoDianChi" "14-XuanZeKa" \
"14-FuGuHongBaiJi" "14-MoRen-ShiZhiNiZhuan"  "14-XinChunFuDai" "14-ShuangSheZhang" "10-BaiGuCao" \
"15-ZhuanLunPan" "15-XiaoPingYuLei" "15-SiXiZheShan" "15-HuaCaoTuan" "15-ShengShuZhongZi" "15-MoFaYaoShui" "15-YongShengZhiHua" "15-YongShengShouMenRen" \
"16-XiaoJingLing-NeiCeZiGeKa" "16-HunDunTu" "16-HuangJinShu-YouLing" "16-CiKongJianLaLian" "16-QiYuanKa" "16-FuGuYuanHuan" \
"16-ShiJian" "16-LingSheZhu" "13-MoGuangGuMian" "13-TabZai" "13-ShenMiShiBan" "17-XingHongBaoShi" "17-SenZhiXi" "17-HuangJinShu-ShengShu" \
"17-XuePuTi" "18-Kulolo-WeiJueZhe" "18-Kulolo-JueXingZhe" "18-Kulolo-SiLieZhe" "18-Kulolo-TunChiZhe" "18-Kulolo-LingZhiZhe" "17-FengMoLingShu" \
"17-LiuSuYuZhui" "17-HuangJinShengShu" "17-BaFangLaiFeng" "16-BaBaoNuoMiFan" "17-JuBaoShenShu" "16-WeiLaiYanJiuYuan" "16-WanNengXiaoJianPan" \
"17-JingHuaSuiPian" "18-JianPanLingXiu-ChaoJiYingXiong" "18-XingHeNian" "19-ChangShengZhu" "19-ShenMiQuanShui" "19-JingMeiDianXinHe" \
"18-AZai" "20-DianDengQi" "20-JingZhongHua" "20-ChuXinZheBuYi" "20-LiangJieDeng" "19-JiangLinDaoXinWu"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$tag $nft/*
done

cd ../../..
python agg_special_transactions.py ${tag}
python agg_special_transactions_external.py ${tag}
python agg_transactions.py ${tag}

#python /mnt/ssd01/git/nft-assistant/GuangYu/upload_baidudisk.py /mnt/ssd01/git/nft-assistant/GuangYu/data/upload/$tag $today/$tag
