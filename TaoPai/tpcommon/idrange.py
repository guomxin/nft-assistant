# coding: utf-8

def get_ranges_by_nftname(nft_name):
    idrange_dict = get_idrangedict_by_nftname(nft_name)
    ranges = []
    for (low, high) in idrange_dict.keys():
        ranges.append((low, high))
    return ranges

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
    elif nft_name == "tiantanbopu":
        return TianTanBoPu_IdRange2Name
    elif nft_name == "feitianpiba":
        return FeiTianPiBa_IdRange2Name
    elif nft_name == "huoxingtance":
        return HuoXingTanCe_IdRange2Name
    elif nft_name == "kaozaifriends":
        return KaoZaiFriends_IdRange2Name
    elif nft_name == "zhongguohangtian":
        return ZhongGuoHangTian_IdRange2Name
    elif nft_name == "hangtiantanwei2":
        return HangTianTanWei2_IdRange2Name
    elif nft_name == "changgexing":
        return ChangGeXing_IdRange2Name
    elif nft_name == "hutoufeitian":
        return HuTouFeiTian_IdRange2Name
    elif nft_name == "yujunqiasi":
        return YuJunQiaSi_IdRange2Name
    else:
        return None

def get_name_by_tokenid(idrange2name, token_id):
    for ((min_tid, max_tid), name) in idrange2name.items():
        if (token_id >= min_tid) and (token_id <= max_tid):
            return name

HuTouFeiTian_IdRange2Name = {
    (40001, 40100): "虎头飞天之福虎生威",
    (40101, 40200): "虎头飞天之柿柿如意",
    (40201, 40300): "虎头飞天之如虎添億",
    (40301, 40400): "虎头飞天之好事花生",
    (40401, 40500): "虎头飞天之萌虎迎春",
}

YuJunQiaSi_IdRange2Name = {
    (50001,51700): '纪云禾',
    (51701,53400): '长意',
    (53401,55400): '林昊青',
    (55401,57400): '顺德仙姬',
    (57401,59400): '空明',
    (59401,61400): '宁清',
    (61401,61700): '纪云禾',
    (61701,62000): '长意',
}

ChangGeXing_IdRange2Name = {
    # R
    (10001,10560): 'R-长安01',
    (10561,11120): 'R-长安02',
    (11121,11680): 'R-长安03',
    (11681,12240): 'R-长安04',

    (12241,12795): 'R-幽州01',
    (12796,13350): 'R-幽州02',
    (13351,13905): 'R-幽州03',
    (13906,14460): 'R-幽州04',

    (14461,15020): 'R-㮶州01',
    (15021,15580): 'R-㮶州02',
    (15581,16140): 'R-㮶州03',
    (16141,16700): 'R-㮶州04',

    # R 预留
    (16701,16740): 'R-长安01',
    (16741,16780): 'R-长安02',
    (16781,16820): 'R-长安03',
    (16821,16860): 'R-长安04',

    (16861,16905): 'R-幽州01',
    (16906,16950): 'R-幽州02',
    (16951,16995): 'R-幽州03',
    (16996,17040): 'R-幽州04',

    (17041,17080): 'R-㮶州01',
    (17081,17120): 'R-㮶州02',
    (17121,17160): 'R-㮶州03',
    (17161,17200): 'R-㮶州04',

    # SR
    (20001,20377): 'SR-鹰师01',
    (20378,20753): 'SR-鹰师02',
    (20754,21128): 'SR-鹰师03',
    (21129,21502): 'SR-鹰师04',

    (21503,21879): 'SR-渭水01',
    (21880,22247): 'SR-渭水02',
    (22248,22618): 'SR-渭水03',
    (22619,22988): 'SR-渭水04',

    (22989,23357): 'SR-王庭01',
    (23358,23727): 'SR-王庭02',
    (23728,24097): 'SR-王庭03',
    (24098,24467): 'SR-王庭04',

    # SR 预留
    (24468,24490): 'SR-鹰师01',
    (24491,24514): 'SR-鹰师02',
    (24515,24539): 'SR-鹰师03',
    (24540,24565): 'SR-鹰师04',

    (24566,24592): 'SR-渭水01',
    (24593,24620): 'SR-渭水02',
    (24621,24649): 'SR-渭水03',
    (24650,24679): 'SR-渭水04',

    (24680,24710): 'SR-王庭01',
    (24711,24740): 'SR-王庭02',
    (24741,24770): 'SR-王庭03',
    (24771,24800): 'SR-王庭04',

    # SSR
    (30001,30186): 'SSR-流云观01',
    (30187,30372): 'SSR-流云观02',
    (30373,30558): 'SSR-流云观03',
    (30559,30744): 'SSR-流云观04',

    (30745,30930): 'SSR-漠北01',
    (30931,31116): 'SSR-漠北02',
    (31117,31302): 'SSR-漠北03',
    (31303,31488): 'SSR-漠北04',

    (31489,31674): 'SSR-定襄01',
    (31675,31860): 'SSR-定襄02',
    (31861,32046): 'SSR-定襄03',
    (32047,32233): 'SSR-定襄04',
    
    ## SSR 预留
    (32234,32247): 'SSR-流云观01',
    (32248,32261): 'SSR-流云观02',
    (32262,32275): 'SSR-流云观03',
    (32276,32289): 'SSR-流云观04',

    (32290,32303): 'SSR-漠北01',
    (32304,32317): 'SSR-漠北02',
    (32318,32331): 'SSR-漠北03',
    (32332,32345): 'SSR-漠北04',

    (32346,32359): 'SSR-定襄01',
    (32360,32373): 'SSR-定襄02',
    (32374,32387): 'SSR-定襄03',
    (32388,32400): 'SSR-定襄04',

    # 完整场景
    (40001,40600): 'R-长安',
    (40601,41200): 'R-幽州',
    (41201,41800): 'R-㮶州',

    (41801,42200): 'SR-鹰师',
    (42201,42600): 'SR-渭水',
    (42601,43000): 'SR-王庭',

    (43001,43200): 'SSR-流云观',
    (43201,43400): 'SSR-漠北',
    (43401,43600): 'SSR-定襄',

    (45001,45600): '大结局碎片A',
    (45601,46000): '大结局碎片B',
    (46001,46200): '大结局碎片C',
}

HangTianTanWei2_IdRange2Name = {
    (10001, 11469): '星',
    (11470, 12938): '箭',
    (12939, 14407): '祝融',
    (14408, 15876): '返回舱',
    (15877, 16576): '器',
    (16577, 17000): '空间站'
}

ZhongGuoHangTian_IdRange2Name = {
    (1,5): '中国航天日金色版',
    (6,370): '祝融周岁纪念紫色版',
    (371,794): '中国航天日绿色版',
    (795,2750): '中国航天梦红色版',
    (2751,4772):'中国航天日蓝色款',
    (4773,6794): '中国航天梦蓝色版',
    (6795,8816): '祝融周岁纪念蓝色版',
    (9001,9365):'航天点亮梦想动态长卷'
}

KaoZaiFriends_IdRange2Name = {
    (300001,300012): '十二生肖款',
    (200001,200360): '金色款',
    (100001,109628): '普通款',
    (2001,2052): '520典藏版',
}

HuoXingTanCe_IdRange2Name = {
    (20001,20515): '祝融',
    (20516,21233): '返回',
    (21234,21951): '创新',
    (21952,22669): '神州',
    (22670,23387): '风云',
    (23388,24105): '长征',
    (24106,24823): '北斗',
    (26001,26515): '3D祝融火星车',
}

FeiTianPiBa_IdRange2Name = {
    (1, 800): 'SSR-反弹琵琶',
    (801, 2800): 'SR-弄弦',
    (2801, 4800): 'SR-雅乐',
    (4801, 6800): 'SR-击竹',
    (6801, 9800): 'R-趣鼓',
    (9801, 12800): 'R-奏琴',
    (12801, 15800): 'R-横笛',
    (15801, 16400): '乐舞伎楽图'
}

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
    (80001,82353): '愚你同乐',
    (90001,92022): '大白烤仔'
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
    (5761, 5770): '传说',
    (5001, 5760): '隐藏',
    (4976,4990): '传说',
    (4926,4955): '史诗',
    (4676,4900): '稀有',
    (4176,4575): '珍贵',
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
    (10001,10040): '实名船票',
    (9340,9382): '船票',
    (9001,9339): '证书',
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