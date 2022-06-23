for nft in "kaozaifriends" "taopai2022" "xunzhang" "letaotao" "taopaitest" "chuangshi" \
"guizi" "laodongcun" "baibianxiong" "fxpanda2" "shuijing" "tiantanbopu" 
do
    mkdir $nft;mv *$nft*.csv $nft;zip $nft $nft/*
done
