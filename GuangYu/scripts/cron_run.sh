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

#echo "---空间补给站-启能版---"
#python grab_transaction_price.py 39 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 39 ${yesterday} 50

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

#echo "---龙图腾---"
#python grab_transaction_price.py 79 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 79 ${yesterday} 100

echo "---龙凤守宝---"
python grab_transaction_price.py 80 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 80 ${yesterday} 500

echo "---探索者III---"
python grab_transaction_price.py 592 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 592 ${yesterday} 50

#echo "---物资传输面板---"
#python grab_transaction_price.py 28 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 28 ${yesterday} 50

#echo "---栖龙云木---"
#python grab_transaction_price.py 29 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 29 ${yesterday} 50

#echo "---梦幻小龙---"
#python grab_transaction_price.py 46 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 46 ${yesterday} 50

#echo "---山岭树龙---"
#python grab_transaction_price.py 55 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 55 ${yesterday} 100

#echo "---凤图腾---"
#python grab_transaction_price.py 87 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 87 ${yesterday} 100

#echo "---阿尔法之眼---"
#python grab_transaction_price.py 94 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 94 ${yesterday} 500

#echo "---魂魄提灯---"
#python grab_transaction_price.py 95 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 95 ${yesterday} 50

echo "---涅槃之地---"
python grab_transaction_price.py 96 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 96 ${yesterday} 500

#echo "---奇物碎片-时间磨盘---"
#python grab_transaction_price.py 100 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 100 ${yesterday} 100

echo "---奇物秘宝-时间磨盘---"
python grab_transaction_price.py 99 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 99 ${yesterday} 100

#echo "---凤翊泪---"
#python grab_transaction_price.py 101 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 101 ${yesterday} 50

#echo "---国庆节限定空投-平安果---"
#python grab_transaction_price.py 71 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 71 ${yesterday} 50

#echo "---国庆节限定空投-福琴---"
#python grab_transaction_price.py 72 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 72 ${yesterday} 50

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

#echo "---虫族骸骨---"
#python grab_transaction_price.py 130 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 130 ${yesterday} 50

#echo "---X型能源电池---"
#python grab_transaction_price.py 129 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 129 ${yesterday} 100

echo "---罗盘指针---"
python grab_transaction_price.py 128 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 128 ${yesterday} 100

echo "---云木方舟---"
python grab_transaction_price.py 140 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 140 ${yesterday} 100

#echo "---晶石碎块-未鉴定---"
#python grab_transaction_price.py 134 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 134 ${yesterday} 100

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

#echo "---垂钓许可---"
#python grab_transaction_price.py 153 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 153 ${yesterday} 100

#echo "---小小键盘-Enter仔---"
#python grab_transaction_price.py 156 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 156 ${yesterday} 100

#echo "---国庆节限定空投-可乐---"
#python grab_transaction_price.py 74 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 74 ${yesterday} 50

#echo "---国庆节限定空投-缘结---"
#python grab_transaction_price.py 73 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 73 ${yesterday} 50

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

#echo "---第九区证件---"
#python grab_transaction_price.py 198 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 198 ${yesterday} 100

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

#echo "---答题卡---"
#python grab_transaction_price.py 568 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 568 ${yesterday} 50

#echo "---磁欧晶碎片---"
#python grab_transaction_price.py 187 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 187 ${yesterday} 50

#echo "---天成仪---"
#python grab_transaction_price.py 269 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 269 ${yesterday} 50

#echo "---天成仪II---"
#python grab_transaction_price.py 389 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 389 ${yesterday} 50

#echo "---流光魔方-琥珀---"
#python grab_transaction_price.py 243 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 243 ${yesterday} 100

echo "---超级巡航者---"
python grab_transaction_price.py 593 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 593 ${yesterday} 100

echo "---超级探索者---"
python grab_transaction_price.py 594 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 594 ${yesterday} 100

echo "---战甲厚土---"
python grab_transaction_price.py 595 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 595 ${yesterday} 100

#echo "---流光宝盒-冷翠---"
#python grab_transaction_price.py 246 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 246 ${yesterday} 100

#echo "---冷翠精华---"
#python grab_transaction_price.py 600 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 600 ${yesterday} 100

#echo "---MK魔术帽---"
#python grab_transaction_price.py 175 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 175 ${yesterday} 100

#echo "---MK马卡龙---"
#python grab_transaction_price.py 174 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 174 ${yesterday} 100

#echo "---MK旋转杯---"
#python grab_transaction_price.py 176 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 176 ${yesterday} 100

#echo "---MK老爷车---"
#python grab_transaction_price.py 173 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 173 ${yesterday} 100

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

#echo "---复古红白机---"
#python grab_transaction_price.py 608 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 608 ${yesterday} 50

echo "---魔刃-时之逆转---"
python grab_transaction_price.py 611 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 611 ${yesterday} 100

#echo "---航海卡---"
#python grab_transaction_price.py 664 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 664 ${yesterday} 50

#echo "---陆运卡---"
#python grab_transaction_price.py 662 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 662 ${yesterday} 50

#echo "---指引卡---"
#python grab_transaction_price.py 663 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 663 ${yesterday} 50

echo "---新春福袋---"
python grab_transaction_price.py 736 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 736 ${yesterday} 50

#echo "---双蛇杖---"
#python grab_transaction_price.py 615 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 615 ${yesterday} 50

#echo "---白骨草---"
#python grab_transaction_price.py 614 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 614 ${yesterday} 50

echo "---转轮盘---"
python grab_transaction_price.py 754 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 754 ${yesterday} 50

echo "---小瓶鱼泪---"
python grab_transaction_price.py 1357 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1357 ${yesterday} 10

#echo "---四喜折扇---"
#python grab_transaction_price.py 711 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 711 ${yesterday} 50

echo "---花草团---"
python grab_transaction_price.py 792 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 792 ${yesterday} 50

echo "---圣树种子---"
python grab_transaction_price.py 793 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 793 ${yesterday} 50

echo "---魔法药水---"
python grab_transaction_price.py 709 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 709 ${yesterday} 50

#echo "---永生之花---"
#python grab_transaction_price.py 715 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 715 ${yesterday} 50

echo "---永生守门人---"
python grab_transaction_price.py 815 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 815 ${yesterday} 50

#echo "---小精灵-内测资格卡---"
#python grab_transaction_price.py 844 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 844 ${yesterday} 50

echo "---混沌土---"
python grab_transaction_price.py 854 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 854 ${yesterday} 50

#echo "---黄金树-有灵---"
#python grab_transaction_price.py 855 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 855 ${yesterday} 50

echo "---次空间拉链---"
python grab_transaction_price.py 853 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 853 ${yesterday} 50

#echo "---祈愿卡---"
#python grab_transaction_price.py 861 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 861 ${yesterday} 50

echo "---缚骨圆环---"
python grab_transaction_price.py 856 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 856 ${yesterday} 50

echo "---时间---"
python grab_transaction_price.py 865 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 865 ${yesterday} 50

echo "---灵蛇珠---"
python grab_transaction_price.py 616 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 616 ${yesterday} 100

echo "---魔光骨冕---"
python grab_transaction_price.py 867 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 867 ${yesterday} 100

echo "---小小键盘-Tab仔---"
python grab_transaction_price.py 895 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 895 ${yesterday} 10

#echo "---神秘石板---"
#python grab_transaction_price.py 398 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 398 ${yesterday} 100

#echo "---猩红宝石---"
#python grab_transaction_price.py 127 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 127 ${yesterday} 100

echo "---森之息---"
python grab_transaction_price.py 896 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 896 ${yesterday} 100

#echo "---黄金树-圣树---"
#python grab_transaction_price.py 894 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 894 ${yesterday} 100

#echo "---血菩提---"
#python grab_transaction_price.py 402 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 402 ${yesterday} 50

echo "---未觉者---"
python grab_transaction_price.py 459 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 459 ${yesterday} 50

echo "---觉醒者---"
python grab_transaction_price.py 458 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 458 ${yesterday} 50

echo "---撕裂者---"
python grab_transaction_price.py 457 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 457 ${yesterday} 100

echo "---吞噬者---"
python grab_transaction_price.py 456 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 456 ${yesterday} 100

echo "---灵智者---"
python grab_transaction_price.py 455 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 455 ${yesterday} 100

echo "---封魔灵树---"
python grab_transaction_price.py 897 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 897 ${yesterday} 100

echo "---流苏玉坠---"
python grab_transaction_price.py 902 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 902 ${yesterday} 100

#echo "---黄金圣树---"
#python grab_transaction_price.py 899 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 899 ${yesterday} 100

echo "---八方来风---"
python grab_transaction_price.py 923 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 923 ${yesterday} 100

#echo "---八宝糯米饭---"
#python grab_transaction_price.py 713 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 713 ${yesterday} 50

echo "---聚宝神树---"
python grab_transaction_price.py 898 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 898 ${yesterday} 100

echo "---未来研究院---"
python grab_transaction_price.py 113 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 113 ${yesterday} 100

#echo "---万能小键盘---"
#python grab_transaction_price.py 931 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 931 ${yesterday} 100

#echo "---镜花碎片---"
#python grab_transaction_price.py 889 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 889 ${yesterday} 10

echo "---键盘领袖---"
python grab_transaction_price.py 1374 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1374 ${yesterday} 100

echo "---星河念---"
python grab_transaction_price.py 135 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 135 ${yesterday} 100

#echo "---小小键盘-A仔---"
#python grab_transaction_price.py 901 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 901 ${yesterday} 10

#echo "---长生竹---"
#python grab_transaction_price.py 1122 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1122 ${yesterday} 100

#echo "---神秘泉水---"
#python grab_transaction_price.py 1123 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1123 ${yesterday} 50

echo "---精美点心盒---"
python grab_transaction_price.py 1085 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1085 ${yesterday} 50

echo "---点灯器---"
python grab_transaction_price.py 1207 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1207 ${yesterday} 100

#echo "---镜中花---"
#python grab_transaction_price.py 888 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 888 ${yesterday} 50

echo "---初心者布衣---"
python grab_transaction_price.py 1127 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1127 ${yesterday} 10

echo "---两界灯---"
python grab_transaction_price.py 1124 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1124 ${yesterday} 100

#echo "---降临岛信物---"
#python grab_transaction_price.py 1320 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1320 ${yesterday} 10

#echo "---饰品图纸---"
#python grab_transaction_price.py 1342 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1342 ${yesterday} 10

#echo "---裁缝图纸---"
#python grab_transaction_price.py 1346 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1346 ${yesterday} 10

#echo "---锻造图纸---"
#python grab_transaction_price.py 1345 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1345 ${yesterday} 10

#echo "---武器模具---"
#python grab_transaction_price.py 1343 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1343 ${yesterday} 10

#echo "---空间碎片---"
#python grab_transaction_price.py 1391 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1391 ${yesterday} 10

#echo "---天蓝史莱姆---"
#python grab_transaction_price.py 1392 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1392 ${yesterday} 10

#echo "---魔神卷轴---"
#python grab_transaction_price.py 1351 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1351 ${yesterday} 50

echo "---鳞片---"
python grab_transaction_price.py 613 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 613 ${yesterday} 50

echo "---天圆镜---"
python grab_transaction_price.py 1408 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1408 ${yesterday} 50

#echo "---魂珠---"
#python grab_transaction_price.py 399 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 399 ${yesterday} 50

#echo "---天神卷轴---"
#python grab_transaction_price.py 1424 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1424 ${yesterday} 50

#echo "---精灵卷轴---"
#python grab_transaction_price.py 1353 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1353 ${yesterday} 50

#echo "---白银宝箱---"
#python grab_transaction_price.py 1445 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1445 ${yesterday} 50

echo "---仙鹤画卷---"
python grab_transaction_price.py 1438 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1438 ${yesterday} 100

#echo "---流光宝盒-暮霭---"
#python grab_transaction_price.py 245 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 245 ${yesterday} 50

#echo "---Lv2天蓝史莱姆---"
#python grab_transaction_price.py 1447 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1447 ${yesterday} 100

#echo "---降临岛晶体---"
#python grab_transaction_price.py 1321 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1321 ${yesterday} 50

#echo "---幸运星---"
#python grab_transaction_price.py 1488 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1488 ${yesterday} 50

#echo "---黄金宝箱---"
#python grab_transaction_price.py 1517 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1517 ${yesterday} 50

#echo "---秘境宝箱---"
#python grab_transaction_price.py 1516 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1516 ${yesterday} 50

#echo "---神话宝箱---"
#python grab_transaction_price.py 1515 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1515 ${yesterday} 50

#echo "---纹银宝箱---"
#python grab_transaction_price.py 1518 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1518 ${yesterday} 50

echo "---原几II---"
python grab_transaction_price.py 1675 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1675 ${yesterday} 50

echo "---质几II---"
python grab_transaction_price.py 1676 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1676 ${yesterday} 50

echo "---电几---"
python grab_transaction_price.py 1541 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1541 ${yesterday} 50

echo "---五色云泥---"
python grab_transaction_price.py 1563 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1563 ${yesterday} 100

echo "---妙墨心画---"
python grab_transaction_price.py 1565 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1565 ${yesterday} 100

#echo "---墨隐图录---"
#python grab_transaction_price.py 1579 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1579 ${yesterday} 100

echo "---涅槃重生---"
python grab_transaction_price.py 1311 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1311 ${yesterday} 100

echo "---小小键盘-Q仔---"
python grab_transaction_price.py 1347 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1347 ${yesterday} 50

echo "---万卷书阁---"
python grab_transaction_price.py 1581 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1581 ${yesterday} 100

echo "---竹林隐士---"
python grab_transaction_price.py 1485 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1485 ${yesterday} 100

#echo "---竹击心法---"
#python grab_transaction_price.py 1590 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1590 ${yesterday} 100

echo "---羽林尉---"
python grab_transaction_price.py 1597 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1597 ${yesterday} 100

#echo "---寒山远笛---"
#python grab_transaction_price.py 1598 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1598 ${yesterday} 100

#echo "---净心墨砚---"
#python grab_transaction_price.py 1626 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1626 ${yesterday} 100

#echo "---双鹤听泉---"
#python grab_transaction_price.py 1624 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1624 ${yesterday} 100

#echo "---尺竹伍符-初级---"
#python grab_transaction_price.py 1599 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1599 ${yesterday} 100

#echo "---尺竹伍符-中级---"
#python grab_transaction_price.py 1625 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1625 ${yesterday} 100

echo "---凌波莲灯---"
python grab_transaction_price.py 1631 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1631 ${yesterday} 100

#echo "---羽鹤归巢---"
#python grab_transaction_price.py 1628 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1628 ${yesterday} 100

#echo "---U型转化器---"
#python grab_transaction_price.py 1634 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1634 ${yesterday} 100

#echo "---渔舟唱晚---"
#python grab_transaction_price.py 1623 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1623 ${yesterday} 100

echo "---北海---"
python grab_transaction_price.py 1638 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1638 ${yesterday} 100

echo "---尺竹伍符-高级---"
python grab_transaction_price.py 1635 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1635 ${yesterday} 100

#echo "---锦上花开---"
#python grab_transaction_price.py 885 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 885 ${yesterday} 100

echo "---空间转化器---"
python grab_transaction_price.py 1639 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1639 ${yesterday} 100

echo "---焱火小恶魔---"
python grab_transaction_price.py 1641 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1641 ${yesterday} 100

echo "---缘木齿丹---"
python grab_transaction_price.py 1637 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1637 ${yesterday} 100

echo "---大理廷尉---"
python grab_transaction_price.py 1658 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1658 ${yesterday} 100

echo "---国色天香---"
python grab_transaction_price.py 1657 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1657 ${yesterday} 100

#echo "---暗影冥冠---"
#python grab_transaction_price.py 1662 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1662 ${yesterday} 100

#echo "---中书秋毫---"
#python grab_transaction_price.py 1656 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1656 ${yesterday} 100

echo "---光几---"
python grab_transaction_price.py 1672 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1672 ${yesterday} 50

#echo "---地方镜---"
#python grab_transaction_price.py 1467 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1467 ${yesterday} 50

echo "---超能修补匠---"
python grab_transaction_price.py 1659 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1659 ${yesterday} 100

echo "---汀兰水榭---"
python grab_transaction_price.py 1674 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1674 ${yesterday} 100

echo "---希格玛护目镜---"
python grab_transaction_price.py 1681 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1681 ${yesterday} 100

echo "---历练者---"
python grab_transaction_price.py 1698 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1698 ${yesterday} 10

echo "---粘合剂---"
python grab_transaction_price.py 1690 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1690 ${yesterday} 50

echo "---冷却液---"
python grab_transaction_price.py 1691 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1691 ${yesterday} 50

echo "---大炼金术士---"
python grab_transaction_price.py 1699 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1699 ${yesterday} 100

#echo "---葫芦---"
#python grab_transaction_price.py 887 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 887 ${yesterday} 100

echo "---暗影花镜---"
python grab_transaction_price.py 1700 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1700 ${yesterday} 100

echo "---天圆灵境---"
python grab_transaction_price.py 1702 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1702 ${yesterday} 100

echo "---天机牌---"
python grab_transaction_price.py 1125 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1125 ${yesterday} 10

echo "---筑颜簪-叁---"
python grab_transaction_price.py 1706 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1706 ${yesterday} 50

echo "---添香匕-叁---"
python grab_transaction_price.py 1708 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1708 ${yesterday} 50

echo "---玉石翁仲-叁---"
python grab_transaction_price.py 1707 ${yesterday} ${yesterday}
python analyze_transaction_prices.py 1707 ${yesterday} 50

#------ 工人 ------#
#echo "---巧克力工人---"
#python grab_transaction_price.py 1256 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1256 ${yesterday} 50

#echo "---面包工人---"
#python grab_transaction_price.py 1258 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1258 ${yesterday} 50

#echo "---布丁工人---"
#python grab_transaction_price.py 1260 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1260 ${yesterday} 50

#echo "---棉花糖工人---"
#python grab_transaction_price.py 1259 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1259 ${yesterday} 50

#echo "---奶油工人---"
#python grab_transaction_price.py 1257 ${yesterday} ${yesterday}
#python analyze_transaction_prices.py 1257 ${yesterday} 50
#------ 工人 ------#

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-KaiTuoZhe" "1-WanXiangLongChao" "2-TaiKongShiftZai" "1-ChaoNengXiuBuJiang" "2-XiGeMaHuMuJing" \
"3-HouTu" "3-HuiJin" "3-FuJin" "1-LongFengShouBao" "14-ZhuLinYinShi" "19-YuLinWei"  "16-ChiZhuWuFu-GaoJi" \
"1-NiePanZhiDi" "5-QiWuMiBao-ShiJianMoPan" "5-TanSuoZheIII" "19-GuoSeTianXiang" "5-TianJiPai" \
"5-ShiHuangZhe" "6-SR-CaiHouZhiShen" "6-R-HouGeLiTe" "6-R-PDHou" "6-N-BaoZuHou" "15-BeiHai" \
"5-LuoPanZhiZhen" "6-YunMuFangZhou" "7-FeiLiWuTingMuXia" "7-JuNeng" "7-QingTongShiXiang" "8-LanHaiYouDie" "8-NianHeJi" \
"8-YuEr" "8-JingZhiDiaoJu-KongTou" "8-JingZhiDiaoJu-DuiHuan" "8-XunHangZheI" "9-MengHuanShuiLong" "8-LengQueYe" \
"9-YuEr-DuiHuan" "9-KuaiJieZuHe-FuZhi" "9-KuaiJieZuHe-ZhanTie" "8-LiLianZhe" \
"9-JiXieHouTu" "10-XiuBuXueTu" "10-JianBaoXueTu" "10-XingHuiDian" "10-HanYueSi" "10-FuZhiBaoZhu" "10-DaLianJinShuShi" \
"10-EMengGuoShi" "10-ShouLieZhe" "11-ChuanShuoWuQi" "12-LianJinXueTu" "12-QiYuanGai-WangChuanJuFeng" \
"11-MaoXianZheZhiXin" "13-ZhuYanZan-San" "13-TianXiangBi-San" "13-YuShiWengZhong-San" \
"13-ChaoJiXunHangZhe" "13-ChaoJiTanSuoZhe" "13-ZhanJiaHouTu" "13-QZai" "13-LingBoLianDeng" \
"14-MoRen-ShiZhiNiZhuan"  "14-XinChunFuDai" "14-XianHeHuaJuan" "21-TingLanShuiXie" \
"15-ZhuanLunPan" "15-XiaoPingYuLei" "15-HuaCaoTuan" "15-ShengShuZhongZi" "15-MoFaYaoShui" "15-YongShengShouMenRen" \
"16-HunDunTu" "16-CiKongJianLaLian" "16-FuGuYuanHuan" \
"16-ShiJian" "16-LingSheZhu" "13-MoGuangGuMian" "13-TabZai" "17-SenZhiXi" "17-KongJianZhuanHuaQi" \
"18-Kulolo-WeiJueZhe" "18-Kulolo-JueXingZhe" "18-Kulolo-SiLieZhe" "18-Kulolo-TunChiZhe" "18-Kulolo-LingZhiZhe" "17-FengMoLingShu" \
"17-LiuSuYuZhui" "17-HuangJinShengShu" "17-BaFangLaiFeng" "17-JuBaoShenShu" "16-WeiLaiYanJiuYuan" "18-YanHuoXiaoEMo" \
"18-JianPanLingXiu-ChaoJiYingXiong" "18-XingHeNian" "19-JingMeiDianXinHe" "19-TianYuanLingJing" \
"20-DianDengQi" "20-ChuXinZheBuYi" "20-LiangJieDeng" "20-LinPian" "19-YuanMuChiDan" "19-DaLiTingWei" \
"21-TianYuanJing" "21-YuanJiII" "21-ZhiJiII" "20-GuangJi" "20-AnYingHuaJing" \
"14-DianJi" "15-WuSeYunNi" "8-MiaoMoXinHua" "16-NiePanChongSheng" "21-WanJuanShuGe"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done

cd ../../..
python agg_special_transactions.py ${yesterday}
python agg_special_transactions_external.py ${yesterday}
python agg_transactions.py ${yesterday}
