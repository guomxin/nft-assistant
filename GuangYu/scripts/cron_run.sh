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

echo "---启源I开拓者号---"
python grab_transaction_price.py 54 ${yesterday} ${yesterday}

echo "---万象龙巢---"
python grab_transaction_price.py 59 ${yesterday} ${yesterday}

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

#------ 后处理 ------#
cd data;mkdir -p upload/$yesterday;rm -rf upload/$yesterday/*
cp *$yesterday* upload/$yesterday;cd upload/$yesterday

for nft in "KaiTuoZhe" "WanXiangLongChao" "TaiKongShiftZai" "ShiftZai" \
"HouTu" "GanLin" "HuiJin" "FuJin" "CtrlZai" "CZai" "VZai"
do
    mkdir $nft;mv *$nft*.csv $nft;zip -q $nft-$yesterday $nft/*
done
