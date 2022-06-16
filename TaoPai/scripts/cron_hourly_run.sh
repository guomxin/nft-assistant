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

conda activate nft;cd /mnt/ssd01/git/nft-assistant/TaoPai

date=`date --date="1 hour ago" +%Y/%m/%d`
hour=`date --date="1 hour ago" +%H`
tag=`date --date="1 hour ago" +%Y%m%d%H`

echo "------${date} ${hour}------"

python transaction_conflux_contract_hourly_online.py laodongcun $date $hour 10001,11800\;11801,13000\;13001,14200\;14201,16000\;16001,16600\;16601,17200\;17201,17800 \
QINLAO\;CONGMING\;HANYONG\;JIANZUI\;ZONGZI\;LONGZHOU\;SR-HUASHOU $tag
