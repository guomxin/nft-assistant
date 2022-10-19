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

echo "---万象龙巢---"
python grab_transaction_price.py 59 ${yesterday} ${yesterday}

echo "---空间补给站-启能版---"
python grab_transaction_price.py 39 ${yesterday} ${yesterday}

echo "---云木守护版---"
python grab_transaction_price.py 57 ${yesterday} ${yesterday}

echo "---小小键盘-Ctrl仔---"
python grab_transaction_price.py 56 ${yesterday} ${yesterday}

echo "---小小键盘-C仔---"
python grab_transaction_price.py 67 ${yesterday} ${yesterday}

echo "---小小键盘-V仔---"
python grab_transaction_price.py 66 ${yesterday} ${yesterday}

echo "---小小键盘-Shift仔---"
python grab_transaction_price.py 60 ${yesterday} ${yesterday}

echo "---传说奇遇-太空Shift仔---"
python grab_transaction_price.py 61 ${yesterday} ${yesterday}

echo "---山丘龙灵-厚土---"
python grab_transaction_price.py 31 ${yesterday} ${yesterday}

echo "---河流龙灵-甘霖---"
python grab_transaction_price.py 32 ${yesterday} ${yesterday}

echo "---焰火龙灵-灰烬---"
python grab_transaction_price.py 33 ${yesterday} ${yesterday}

echo "---金晶龙灵-浮金---"
python grab_transaction_price.py 30 ${yesterday} ${yesterday}

echo "---国庆节限定空投-龙凤筷---"
python grab_transaction_price.py 75 ${yesterday} ${yesterday}

echo "---龙图腾---"
python grab_transaction_price.py 79 ${yesterday} ${yesterday}

echo "---龙凤守宝---"
python grab_transaction_price.py 80 ${yesterday} ${yesterday}

echo "---探索者-Ctrl---"
python grab_transaction_price.py 83 ${yesterday} ${yesterday}

echo "---探索者-Shift---"
python grab_transaction_price.py 84 ${yesterday} ${yesterday}

echo "---物资传输面板---"
python grab_transaction_price.py 28 ${yesterday} ${yesterday}

echo "---栖龙云木---"
python grab_transaction_price.py 29 ${yesterday} ${yesterday}

echo "---梦幻小龙---"
python grab_transaction_price.py 46 ${yesterday} ${yesterday}

echo "---山岭树龙---"
python grab_transaction_price.py 55 ${yesterday} ${yesterday}

echo "---凤图腾---"
python grab_transaction_price.py 87 ${yesterday} ${yesterday}

echo "---阿尔法之眼---"
python grab_transaction_price.py 94 ${yesterday} ${yesterday}

echo "---魂魄提灯---"
python grab_transaction_price.py 95 ${yesterday} ${yesterday}

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "1-KaiTuoZhe" "1-WanXiangLongChao" "1-KongJianBuJi-QiNeng" "1-YunMuShouHu" "2-TaiKongShiftZai" "2-ShiftZai" \
"3-HouTu" "3-GanLin" "3-HuiJin" "3-FuJin" "2-CtrlZai" "2-CZai" "2-VZai" "4-LongFengKuai" "4-LongTuTeng" "1-LongFengShouBao" "4-FengTuTeng" \
"1-ChuanShuMianBan" "1-QiLongYunMu" "1-MengHuanXiaoLong" "1-ShanLingShuLong" "5-AErFaYan" "5-HunPoTiDeng" \
"5-TanSuoZhe-Ctrl" "5-TanSuoZhe-Shift"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done
