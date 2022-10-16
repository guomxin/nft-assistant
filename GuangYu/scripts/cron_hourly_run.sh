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

echo "---探索者-Ctrl---"
python grab_transaction_price.py 83 ${today} ${tag}

echo "---探索者-Shift---"
python grab_transaction_price.py 84 ${today} ${tag}

#------ 后处理 ------#
cd data;mkdir -p upload/$tag;rm -rf upload/$tag/*
mv *$tag* upload/$tag;cd upload/$tag

for nft in "KaiTuoZhe" "WanXiangLongChao" "KongJianBuJi-QiNeng" "YunMuShouHu" "TaiKongShiftZai" "ShiftZai" \
"HouTu" "GanLin" "HuiJin" "FuJin" "CtrlZai" "CZai" "VZai" "LongFengKuai" "LongTuTeng" "LongFengShouBao" \
"TanSuoZhe-Ctrl" "TanSuoZhe-Shift"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$tag $nft/*
done

python /mnt/ssd01/git/nft-assistant/GuangYu/upload_baidudisk.py /mnt/ssd01/git/nft-assistant/GuangYu/data/upload/$tag $today/$tag