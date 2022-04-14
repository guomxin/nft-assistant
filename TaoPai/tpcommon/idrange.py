# coding: utf-8

def get_range_by_nftname(nft_name):
    idrange_dict = get_idrangedict_by_nftname(nft_name)
    min_tid = None
    max_tid = None
    for (low, high) in idrange_dict.keys():
        if (min_tid == None) or (min_tid > low):
            min_tid = low
        if (max_tid == None) or (max_tid < high):
            max_tid = high
    return (min_tid, max_tid)

def get_idrangedict_by_nftname(nft_name):
    if nft_name == "liuangel":
        return TS_IdRange2Name
    elif nft_name == "aprilkaozai":
        return AprilKZIdRange2Name
    elif nft_name == "atsj":
        return ATSJ_IdRange2Name
    elif nft_name == "chaohu":
        return CH_IdRange2Name
    elif nft_name == "dunhuang":
        return DH_IdRange2Name
    elif nft_name == "lt":
        return LT_IdRange2Name
    elif nft_name == "guizi":
        return GuiZi_IdRange2Name
    elif nft_name == "shangshi":
        return ShangShi_IdRange2Name
    else:
        return None

def get_name_by_tokenid(idrange2name, token_id):
    for ((min_tid, max_tid), name) in idrange2name.items():
        if (token_id >= min_tid) and (token_id <= max_tid):
            return name

TianTanBoPu_IdRange2Name = {
    (1001, 1240): '天坛波普S',
    (1241, 1380): '天坛波普SS',
    (1381, 1400): '天坛波普SSS'
}

ShangShi_IdRange2Name = {
    (889, 1152): '衣服-姚子衿掌膳服',
    (1153, 1416): '衣服-姚子衿太子嫔服1',
    (1417, 1680): '衣服-姚子衿太子嫔服2',
    (1681, 1944): '衣服-朱瞻基战服',
    (1945, 2166): '首饰-姚子衿太子嫔服',
    (2167, 2388): '首饰-姚子衿贵妃'
}

GuiZi_IdRange2Name = {
    (1, 1000): '重启柜子',
    (1001, 4000): '无限柜子'
}

AprilKZIdRange2Name = {
    (82398,82444): '复活节',
    (82354,82397): '清明时节',
    (80001,82353): '愚你同乐'
}

TS_IdRange2Name = {
    (20001,20500): '灵禅天使',
    (20501,21000): '风雨天使',
    (21001,21500): '异瞳天使',
    (21501,22000): '黑梦天使',
    (22001,22500): '蓝骨天使',
    (22501,23000): '隐形天使'
}

CH_IdRange2Name = {
    (4976,4985): '传说',
    (4926,4955): '史诗',
    (4676,4900): '稀有',
    (1,3735): '高级'
}

DH_IdRange2Name = {
    (1001, 2000): '彩虹',
    (2001, 2333): '满金幸福',
    (10001,14500): '红',
    (14501,19000): '橙',
    (19001,23500): '黄',
    (23501,28000): '绿',
    (28001,32500): '蓝',
    (32501,37000): '靛',
    (37001,38000): '金',
    (38001,40000): '紫'
}

LT_IdRange2Name = {
    (8382,8680): '19 野餐',
    (8083,8381): '18 未来',
    (7784,8082): '17 梦想',
    (7485,7783): '16 春天',
    (7186,7484): '15 我爱吃水果',
    (6887,7185): '14 亲爱的一家人',
    (6588,6886): '13 星空中的我们',
    (6289,6587): '12 呐喊',
    (5990,6288): '11 海蛞蝓',
    (5691,5989): '10 人与自然2',
    (5392,5690): '9 花开',
    (5093,5391): '8 日出',
    (4794,5092): '7 梦想起航机',
    (4495,4793): '6 宇航员登月球',
    (4196,4494): '5 和蓝天做游戏',
    (3897,4195): '4 丸子公主',
    (3598,3896): '3 布老虎',
    (3299,3597): '2 小陆宇宙探险之回归地球',
    (3000,3298): '1 虎年大吉'
}

ATSJ_IdRange2Name = {
    (101, 200): '隐藏款-嘉德罗斯小队',
    (201, 300): '隐藏款-金小队',
    (301, 400): '隐藏款-雷狮小队',
    (38501,38800): 'XR-全家福',
    (38201,38500): 'UR-金',
    (37901,38200): 'UR-嘉德罗斯',
    (37601,37900): 'UR-雷狮',
    (37301,37600): 'UR-格瑞',
    (37001,37300): 'UR-安迷修',
    (36701,37000): 'SSR-金',
    (36401,36700): 'SSR-凯莉',
    (36101,36400): 'SSR-嘉德罗斯',
    (35801,36100): 'SSR-雷狮',
    (35501,35800): 'SSR-卡米尔',
    (35201,35500): 'SSR-格瑞',
    (34901,35200): 'SSR-安迷修',
    (34601,34900): 'SSR-雷伊',
    (34301,34600): 'SSR-神近耀',
    (34001,34300): 'SSR-帕洛斯',
    (33551,34000): 'SR-安莉洁',
    (33101,33550): 'SR-金',
    (32651,33100): 'SR-凯莉',
    (32201,32650): 'SR-嘉德罗斯',
    (31751,32200): 'SR-雷德',
    (31301,31750): 'SR-紫堂幻',
    (30851,31300): 'SR-秋',
    (30401,30850): 'SR-雷狮',
    (29951,30400): 'SR-佩利',
    (29501,29950): 'SR-卡米尔',
    (29051,29500): 'SR-紫堂真',
    (28601,29050): 'SR-格瑞',
    (28151,28600): 'SR-赞德',
    (27701,28150): 'SR-安迷修',
    (27251,27700): 'SR-埃米',
    (26801,27250): 'SR-雷伊',
    (26351,26800): 'SR-神近耀',
    (25901,26350): 'SR-丹尼尔',
    (25451,25900): 'SR-艾比',
    (25001,25450): 'SR-帕洛斯',
    (24501,25000): 'R-裁判球',
    (24001,24500): 'R-小黑洞',
    (23501,24000): 'R-雷蛰',
    (23001,23500): 'R-鬼狐天冲',
    (22501,23000): 'R-见习天使',
    (22001,22500): 'R-杰德里',
    (21501,22000): 'R-哆莉',
    (21001,21500): 'R-萝洁特',
    (20501,21000): 'R-龙阁',
    (20001,20500): 'R-拉比兹',
    (19501,20000): 'R-莱耶斯',
    (19001,19500): 'R-罗德烈',
    (18501,19000): 'R-雷震',
    (18001,18500): 'R-雷霆',
    (17501,18000): 'R-银爵',
    (17001,17500): 'R-赤星',
    (16501,17000): 'R-梅莉蕾蒂',
    (16001,16500): 'R-霍金斯',
    (15501,16000): 'R-维德',
    (15001,15500): 'R-法尔法拉',
    (14501,15000): 'R-蒙特祖玛',
    (14001,14500): 'R-菲利斯·尼克瑞斯',
    (13501,14000): 'R-安吉拉',
    (13001,13500): 'R-莱娜',
    (12501,13000): 'R-蜜蜜',
    (12001,12500): 'R-紫堂林',
    (11501,12000): 'R-安特',
    (11001,11500): 'R-紫堂陆',
    (10501,11000): 'R-悦然',
    (10001,10500): 'R-京弥'
}