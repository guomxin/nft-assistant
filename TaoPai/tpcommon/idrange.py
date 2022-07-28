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
    elif nft_name == "sdqhchuangshi":
        return SDQHChuangShi_IdRange2Name
    elif nft_name == "lt": # 星儿
        return LT_IdRange2Name
    elif nft_name == "ltcard":
        return LTCard_IdRange2Name
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
    elif nft_name == "kaozaifriends2":
        return KaoZaiFriends2_IdRange2Name
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
    elif nft_name == "taopai2022":
        return TaoPai2022_IdRange2Name
    elif nft_name == "taopaitest":
        return Test_IdRange2Name
    elif nft_name == "taopaichuangshi":
        return TaoPaiChuangShi_IdRange2Name
    elif nft_name == "baibianxiong":
        return BaiBianXiong_IdRange2Name
    elif nft_name == "laodongcun":
        return LaoDongCun_IdRange2Name
    elif nft_name == "laodongcun2":
        return LaoDongCun2_IdRange2Name
    elif nft_name == "xunzhang":
        return XunZhang_IdRange2Name
    elif nft_name == "letaotao":
        return LeTaoTao_IdRange2Name
    elif nft_name == "fxpanda":
        return FXPanda_IdRange2Name
    elif nft_name == "fxpanda2":
        return FXPanda2_IdRange2Name
    elif nft_name == "fxpandaall":
        return FXPandaAll_IdRange2Name
    elif nft_name == "fxxunzhang":
        return FXHEBadge_IdRange2Name
    elif nft_name == "shuijing":
        return ShuiJing_IdRange2Name
    elif nft_name == "kaozaikaituo":
        return KaiZaiKaiTuo_IdRange2Name
    elif nft_name == "saiboyouling":
        return SaiBoYouLing_IdRange2Name
    elif nft_name == "huacedatu":
        return HuaCeDaTu_IdRange2Name
    elif nft_name == "pinglan":
        return PingLan_IdRange2Name
    elif nft_name == "bobosg":
        return BOBOSG_IdRange2Name
    elif nft_name == "huakaiyunqi":
        return HuaKaiYunQi_IdRange2Name
    elif nft_name == "limitless":
        return Limitless_IdRange2Name
    elif nft_name == "pcatmem":
        return PCatMem_IdRange2Name
    elif nft_name == "partycat":
        return PartyCat_IdRange2Name
    elif nft_name == "dftyrb":
        return DFTYRB_IdRange2Name

    #--- 豹豹青春宇宙 ---#
    elif nft_name == "kaoshenglaile":
        return KaoShengLaiLe_IdRange2Name
    elif nft_name == "tongjing":
        return TongJing_IdRange2Name
    #--- 豹豹青春宇宙 ---#
    else:
        return None

def get_name_by_tokenid(idrange2name, token_id):
    for ((min_tid, max_tid), name) in idrange2name.items():
        if (token_id >= min_tid) and (token_id <= max_tid):
            return name

DFTYRB_IdRange2Name = {
    (1,1000): "《东方体育日报》申城花开头版",
    (1001,2000): "《新民体育报》创刊号",
    (2001,3000): "《东方体育日报》创刊号",
    (3001,4000): "《东方体育日报》申花是冠军头版",
    (4001,5000): "《东方体育日报》创刊20周年",
    (5001,6000): "《东方体育日报》荣耀上海头版",
    (6001,7000): "《东方体育日报》势不可挡头版",
    (7001,8000): "《新民体育报》 梦想成真头版",
}

PartyCat_IdRange2Name = {
    (1,8): "独有版权派对猫",
    
    (901,938): "派对猫#9", #(901,938),(1001,1038), ...一共38*30=1140
    (1001,1038): "派对猫#10",
    (1101,1138): "派对猫#11",
    (1201,1238): "派对猫#12",
    (1301,1338): "派对猫#13",
    (1401,1438): "派对猫#14",
    (1501,1538): "派对猫#15",
    (1601,1638): "派对猫#16",
    (1701,1738): "派对猫#17",
    (1801,1838): "派对猫#18",
    (1901,1938): "派对猫#19",
    (2001,2038): "派对猫#20",
    (2101,2138): "派对猫#21",
    (2201,2238): "派对猫#22",
    (2301,2338): "派对猫#23",
    (2401,2438): "派对猫#24",
    (2501,2538): "派对猫#25",
    (2601,2638): "派对猫#26",
    (2701,2738): "派对猫#27",
    (2801,2838): "派对猫#28",
    (2901,2938): "派对猫#29",
    (3001,3038): "派对猫#30",
    (3101,3138): "派对猫#31",
    (3201,3238): "派对猫#32",
    (3301,3338): "派对猫#33",
    (3401,3438): "派对猫#34",
    (3501,3538): "派对猫#35",
    (3601,3638): "派对猫#36",
    (3701,3738): "派对猫#37",
    (3801,3838): "派对猫#38",
}

SDQHChuangShi_IdRange2Name = {
    (2701,2765): "丝道银河创世勋章", # (2701,2800) 2022/7/20
}

PCatMem_IdRange2Name = {
    (12001,13001): "派对猫首发纪念卡",
}

Limitless_IdRange2Name = {
    (1,500): "SSR-ACUEBEE-001",
    (501,1500): "SR-ACUEBEE-002",
    (1501,2500): "SR-ACUEBEE-003",
    (2501,4000): "R-ACUEBEE-004",
    (4001,5500): "R-ACUEBEE-005",
    (5501,7000): "R-ACUEBEE-006",
    (10001,10050): "SP-ACUEBEE",
}

HuaKaiYunQi_IdRange2Name = {
    (12001,12199): "春之花", #199
    (12201,12499): "夏之花", #299
    (12501,12899): "秋之花", #399
    (12901,13399): "冬之花", #499
    (13401,13659): "云起龙骧", #259，预留20

    (2101,2166): "蝶恋花", # TODO: (2167,2200) 2022/7/13
    (2201,2252): "云起龙骧", # TODO: (2253,2300) 2022/7/13
    (2401,2499): "蝶恋花", # TODO: (2401,2500) 2022/7/14

    (2501,2666): "原石",
}

BOBOSG_IdRange2Name = {
    (1,1800): "R-战神吕布",
    (4001,5800): "R-燕人张飞",
    (8001,9800): "R-武圣关羽",
    (12001,12720): "SR-枭雄曹操",
    (14001,14720): "SR-仁义刘备",
    (16001,16360): "SSR-卧龙诸葛亮",
    (17001,17600): "桃园结义",
}

PingLan_IdRange2Name = {
    (70001,70485): "昆明复华大学",
    (70486,71455): "复华大学",
    (71456,73395): "含光中队",
    (73396,73410): "昆明复华大学",
    (73411,73440): "复华大学",
    (73441,73500): "含光中队",
    (4001,4500): "霍克-3型飞机模型",
}

SaiBoYouLing_IdRange2Name = {
    (1,2850): "普通款",
    (2851,3000): "珍藏款",
    # (3001,3122)区间也是，但普通款和珍藏款穿插，不知什么原因
    # (1,3000)部分tokenid作废
}

KaiZaiKaiTuo_IdRange2Name = {
    (15001,15500): "侦查烤仔",
    (15501,16000): "冲锋烤仔",
    (16001,16500): "医师烤仔",
    (16501,17000): "指挥官烤仔",
    (17001,17500): "猛士烤仔",
}

ShuiJing_IdRange2Name = {
    # 水晶博物馆
    (1,2000): "R-唐-琉璃马",
    (2001,4000): "R-唐-琉璃瓶",
    (4001,6000): "R-汉-琉璃印",
    (6001,8000): "R-汉-琉璃鹅",
    (8001,9500): "SR-汉-琉璃如意",
    (9501,10000): "SSR-唐-动作人物",
    (10001,10200): "艺次元勋章",
    (10301,10600): "我是武打巨星",
    (11001,11078): "黑猫少女",
    (11079,11251): "艺次元高级勋章",
    #(11301,11500): "TODO", 2022/7/6
    (11501,11800): "机械少女",
    (12001,12260): "艺次元勋章",
}

FXHEBadge_IdRange2Name = {
    # 勋章证书
    (62001,63000): "佛系证书-金钱的主人",
    (40104,40206): "佛系收藏家虎年勋章",
    (40207,40309): "佛系收藏家熊猫勋章",
    (40310,40517): "佛系大使青铜勋章",
    (40518,40620): "佛系大使白银勋章",
    (40621,40688): "佛系大使黄金勋章",
    (11001,11103): "佛系创世藏家勋章",
}

FXPandaAll_IdRange2Name = {
    # 佛系熊猫第一期
    (30001,30906): "常规款-天天向上",
    (30907,31812): "常规款-嬉戏",
    (31813,32718): "常规款-学无止境",
    (32719,33624): "常规款-观察世界",

    (33625,34332): "稀有款-探索自然",
    (34333,35040): "稀有款-聊天",

    (35041,35348): "传说款-篮球小将",
    (35349,35656): "传说款-足球小将",

    (40001,40103): "传说款-友情岁月",

    # 佛系熊猫第二期
    (50001,50838): "常规款-一起发呆",
    (50839,51676): "常规款-下午茶",
    (51677,52514): "常规款-伸展运动",
    (52515,53352): "常规款-压力山大",
    (53353,54190): "常规款-小伙伴",
    (54191,55028): "常规款-干杯",
    (55029,55866): "常规款-打工人",
    (55867,56704): "常规款-熊猫躺",

    (56705,57292): "稀有款-欢唱",
    (57293,57880): "稀有款-真香",

    (57881,57980): "常规款-一起发呆",
    (57981,58080): "常规款-下午茶",
    (58081,58180): "常规款-伸展运动",
    (58181,58280): "常规款-压力山大",
    (58281,58380): "常规款-小伙伴",
    (58381,58480): "常规款-干杯",
    (58481,58580): "常规款-打工人",
    (58581,58680): "常规款-熊猫躺",

    (58681,58780): "稀有款-欢唱",
    (58781,58880): "稀有款-真香",

    (60001,61000): "稀有款-徒步",
    (61001,61523): "稀有款-跑步",
    (61524,61873): "传说款-高尔夫",

    (64001,64308): "传说款-茶道",
    (65001,65308): "传说款-篮球飞人",
    (66001,66308): "传说款-足球先生",

    (10301,10313): "传说款-茶道",
    (10314,10352): "传说款-篮球飞人",
    (10353,10429): "传说款-足球先生",
}

FXPanda2_IdRange2Name = {
    # 佛系熊猫第二期
    (50001,50838): "常规款-一起发呆",
    (50839,51676): "常规款-下午茶",
    (51677,52514): "常规款-伸展运动",
    (52515,53352): "常规款-压力山大",
    (53353,54190): "常规款-小伙伴",
    (54191,55028): "常规款-干杯",
    (55029,55866): "常规款-打工人",
    (55867,56704): "常规款-熊猫躺",

    (56705,57292): "稀有款-欢唱",
    (57293,57880): "稀有款-真香",

    (57881,57980): "常规款-一起发呆",
    (57981,58080): "常规款-下午茶",
    (58081,58180): "常规款-伸展运动",
    (58181,58280): "常规款-压力山大",
    (58281,58380): "常规款-小伙伴",
    (58381,58480): "常规款-干杯",
    (58481,58580): "常规款-打工人",
    (58581,58680): "常规款-熊猫躺",

    (58681,58780): "稀有款-欢唱",
    (58781,58880): "稀有款-真香",

    (60001,61000): "稀有款-徒步",
    (61001,61523): "稀有款-跑步",
    (61524,61873): "传说款-高尔夫",
}

FXPanda_IdRange2Name = {
    # 佛系熊猫第一期
    (30001,30906): "常规款-天天向上",
    (30907,31812): "常规款-嬉戏",
    (31813,32718): "常规款-学无止境",
    (32719,33624): "常规款-观察世界",

    (33625,34332): "稀有款-探索自然",
    (34333,35040): "稀有款-聊天",

    (35041,35348): "传说款-篮球小将",
    (35349,35656): "传说款-足球小将",
}

TongJing_IdRange2Name = {
    # 豹豹青春宇宙
    (1,2500): "唐宝相花铜镜",
    (10001,12500): "汉五乳神兽镜",
    (20001,22500): "仿汉四神博局镜",
    (30001,32500): "唐真子飞霜铜镜", 
}

KaoShengLaiLe_IdRange2Name = {
    # 豹豹青春宇宙
    (1,10000): "满载而归",
    (10001,20000): "喜报三元",
    (20001,30000): "金榜题名",
    (30001,40000): "状元及第",
}

LeTaoTao_IdRange2Name = {
    (50001,50088): "乐淘淘-龙抬头",
    (50089,50176): "乐淘淘-冬残奥会开幕",
    (50177,50264): "乐淘淘-惊蛰",
    (50265,50352): "乐淘淘-雷锋日",
    (50353,50440): "乐淘淘-国际劳动妇女节",
    (50441,50528): "乐淘淘-植树节",
    (50529,50616): "乐淘淘-残奥会闭幕",
    (50617,50704): "乐淘淘-春分",
    (50705,50792): "乐淘淘-地球一小时",
    (50793,50880): "乐淘淘-愚人节",
    (50881,50968): "乐淘淘-清明",
    (50969,51056): "乐淘淘-复活节",
    (51057,51144): "乐淘淘-谷雨",
    (51145,51232): "乐淘淘-国际不打小孩日",
    (51233,51320): "乐淘淘-劳动节",
    (51321,51408): "乐淘淘-立夏",
    (51409,51496): "乐淘淘-母亲节",
    (51636,51723): "乐淘淘-小满",
    (51724,51811): "乐淘淘-儿童节",
    (51812,51899): "乐淘淘-端午节",
    (51900,51987): "乐淘淘-小满",
    (51988,52075): "乐淘淘-芒种",
    (52076,52163): "乐淘淘-纪念版",
    (52164,52201): "乐淘淘-父亲节",
    (52202,52239): "乐淘淘-夏至",
    (52240,52289): "乐淘淘-父亲节",
    (52290,52339): "乐淘淘-夏至",
}

XunZhang_IdRange2Name = {
    (1,200): "创世王者勋章",
    (201,218): "交易大师勋章",
    (219,303): "交易精英勋章",
    (2501,2705): "测试大师勋章",
    (4001,4200): "志愿者勋章", # 目前是到4020 (2022/7/7)，还有2806
    (60001,70000): "早鸟勋章", # 出现其他勋章时需要更改，总数为66470(2022/6/15)
    (70001,82000): "夏日清凉碎片",
    (1101,1700): "迁徙绿码", # 目前是(1101,1630),2022/7/14

    (1001,1005): "淘派大使勋章-钻石",
    (1006,1009): "淘派大使勋章-金",
    (1010,1012): "淘派大使勋章-银",
    (1013,1018): "淘派大使勋章-铜",
}

LaoDongCun2_IdRange2Name = {
    # 二期
    (20001,21111): "R-怪力少女",
    (21112,22222): "R-富家千金",
    (22223,24444): "N-村口大娘",
    (24445,26666): "N-拾荒小孩",
    (5001,5900): "SR-农大户",
    # (4001,4600): "TODO", 2022/7/12
    (6001,6900): "R-劳动模范",
}

LaoDongCun_IdRange2Name = {
    # 一期
    (10001,11800): 'N-勤劳大叔',
    (11801,13000): 'R-聪明小子',
    (13001,14200): 'R-憨勇小子',
    (14201,16000): 'N-尖嘴汉',
    (16001,16600): "端午粽子",
    (16601,17200): "龙舟",
    (17201,17800): "SR-最勇划手",
}

BaiBianXiong_IdRange2Name = {
    (1,15): "SSR", # (1,50)
    (51,185): "SR", # (51,500)
    (501,2250): "R", # (501,3000)
    (3001,7800): "N", # (3001,10000)
    (10001,10015): "SSR-端午限定",
    (11001,12420): "熊熊碎片",
    (12500,12649): "SR-父亲节限定",
    (13001,13300): "熊熊奶嘴",
}

TaoPaiChuangShi_IdRange2Name = {
    (10001,10121): "内测纪念", # 实际上121个

    (20001,20003): "公测纪念-S",
    (20004,20004): "公测纪念-SS",
    (20005,20019): "公测纪念-S",
    (20020,20020): "公测纪念-SS",
    (20021,20028): "公测纪念-S",
    (20029,20029): "公测纪念-SS",
    (20030,20032): "公测纪念-S",
    (20033,20033): "公测纪念-SS",
    (20034,20040): "公测纪念-S",
    (20041,20041): "公测纪念-SSS", #1
    (20042,20042): "公测纪念-SS",
    (20043,20043): "公测纪念-S",
    (20044,20044): "公测纪念-SS",
    (20045,20049): "公测纪念-S",
    (20050,20050): "公测纪念-SSS", #2
    (20051,20062): "公测纪念-S",
    (20063,20063): "公测纪念-SS",
    (20064,20065): "公测纪念-S",
    (20066,20066): "公测纪念-SS",
    (20067,20071): "公测纪念-S",
    (20072,20072): "公测纪念-SSS", #3
    (20073,20074): "公测纪念-S",
    (20075,20075): "公测纪念-SS",
    (20076,20077): "公测纪念-S",
    (20078,20078): "公测纪念-SSS", #4
    (20079,20079): "公测纪念-SS",
    (20080,20080): "公测纪念-S",
    (20081,20081): "公测纪念-SSS", #5
    (20082,20083): "公测纪念-S",
    (20084,20085): "公测纪念-SS",
    (20086,20088): "公测纪念-S",
    (20089,20089): "公测纪念-SS",
    (20090,20093): "公测纪念-S",
    (20094,20094): "公测纪念-SS",
    (20095,20097): "公测纪念-S",
    (20098,20098): "公测纪念-SSS", #6
    (20099,20099): "公测纪念-S",
    (20100,20100): "公测纪念-SSS", #7
    (20101,20109): "公测纪念-S",
    (20110,20110): "公测纪念-SS",
    (20111,20112): "公测纪念-S",
    (20113,20115): "公测纪念-SS",
    (20116,20117): "公测纪念-S",
    (20118,20119): "公测纪念-SS",
    (20120,20127): "公测纪念-S",

    (30001,32022): "2022幸运光符",

    (50001,51496): "乐淘淘",
    (51636,52339): "乐淘淘",

    (201,218): "交易大师勋章",
    (200001,200360): '金色款',
}

Test_IdRange2Name = {
    (10001,10999): "内测纪念", # 实际上121个

    (20001,20003): "公测纪念-S",
    (20004,20004): "公测纪念-SS",
    (20005,20019): "公测纪念-S",
    (20020,20020): "公测纪念-SS",
    (20021,20028): "公测纪念-S",
    (20029,20029): "公测纪念-SS",
    (20030,20032): "公测纪念-S",
    (20033,20033): "公测纪念-SS",
    (20034,20040): "公测纪念-S",
    (20041,20041): "公测纪念-SSS", #1
    (20042,20042): "公测纪念-SS",
    (20043,20043): "公测纪念-S",
    (20044,20044): "公测纪念-SS",
    (20045,20049): "公测纪念-S",
    (20050,20050): "公测纪念-SSS", #2
    (20051,20062): "公测纪念-S",
    (20063,20063): "公测纪念-SS",
    (20064,20065): "公测纪念-S",
    (20066,20066): "公测纪念-SS",
    (20067,20071): "公测纪念-S",
    (20072,20072): "公测纪念-SSS", #3
    (20073,20074): "公测纪念-S",
    (20075,20075): "公测纪念-SS",
    (20076,20077): "公测纪念-S",
    (20078,20078): "公测纪念-SSS", #4
    (20079,20079): "公测纪念-SS",
    (20080,20080): "公测纪念-S",
    (20081,20081): "公测纪念-SSS", #5
    (20082,20083): "公测纪念-S",
    (20084,20085): "公测纪念-SS",
    (20086,20088): "公测纪念-S",
    (20089,20089): "公测纪念-SS",
    (20090,20093): "公测纪念-S",
    (20094,20094): "公测纪念-SS",
    (20095,20097): "公测纪念-S",
    (20098,20098): "公测纪念-SSS", #6
    (20099,20099): "公测纪念-S",
    (20100,20100): "公测纪念-SSS", #7
    (20101,20109): "公测纪念-S",
    (20110,20110): "公测纪念-SS",
    (20111,20112): "公测纪念-S",
    (20113,20115): "公测纪念-SS",
    (20116,20117): "公测纪念-S",
    (20118,20119): "公测纪念-SS",
    (20120,20127): "公测纪念-S",
}

TaoPai2022_IdRange2Name = {
    (30001,30100): '颜值爆表',
    (30101,30200): '狂吃不胖',
    (30201,30300): '脱发拜拜',
    (30301,30400): '升职加薪',
    (30401,30500): '财务自由',
    (30501,30600): '一夜暴富',
    (30601,30700): '颜值在线',
    (30701,30800): '大吉大利',
    (30801,30900): '锦鲤附体',
    (30901,31000): '睡到自然醒',
    (31001,31100): '别墅靠着海',
    (31101,31200): '要自由',
    (31201,31300): '去旅行吧',
    (31301,31400): '多喝热水',
    (31401,31500): '记得铲屎',
    (31501,31600): '爱自己',
    (31601,31700): '世界和平',
    (31701,31800): '不空虚',
    (31801,31900): '新生',
    (31901,32000): '涨涨涨',
    (32001,32011): '日进斗金',
    (32012,32022): '桃花旺旺'
}

HuTouFeiTian_IdRange2Name = {
    (40001, 40100): "虎头飞天之福虎生威",
    (40101, 40200): "虎头飞天之柿柿如意",
    (40201, 40300): "虎头飞天之如虎添億",
    (40301, 40400): "虎头飞天之好事花生",
    (40401, 40500): "虎头飞天之萌虎迎春",
}

HuaCeDaTu_IdRange2Name = {
    (46201,46400): '长歌行-大结局视频',    
    (68001,69000): '纪念版人物徽章海报',
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

    (62001,63000): '纪云禾-动态徽章',
    (63001,64000): '长意-动态徽章',
    (64001,65000): '林昊青-动态徽章-',
    (65001,66000): '顺德仙姬-动态徽章',
    (66001,67000): '空明-动态徽章',
    (67001,68000): '宁清-动态徽章',

    (68001,69000): '纪念版人物徽章海报',
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

    (46201,46400): '长歌行-大结局视频',
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

KaoZaiFriends2_IdRange2Name = {
    (7001,9000): "烤仔的朋友-Evo2K",
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
    (1,3735): '高级',
    # (6001,6540): "" TODO:2022/7/27
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
    (38001,40000): '紫',

    (2501,2700): "冥想小星星",
}

LTCard_IdRange2Name = {
    (11001,11066): "史诗卡牌",
}

LT_IdRange2Name = {
    (10001,10047): '实名船票',
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