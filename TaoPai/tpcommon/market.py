# coding: utf-8

Contract_Dict = {
    # 通过https://nft.taopainft.com/v1/market/v2/product/list接口返回获得contractId
    # 跟pid不一致
    37: 10, # 佛系惠二
}

Keywords_Dict = {
    # 淘派官方
    "乐淘淘": 50,
    "早鸟勋章": 8,
    "交易精英勋章": 200,
    "创世王者勋章": 5000,
    "清凉": 4,
    "绿码": 15,
    "测试大师": 100,

    # 烤仔的朋友
    "烤仔的朋友": 100,
    "金色款-烤仔的朋友": 800,
    "Evo2k": 200,

    # 百变熊熊
    "N-百变熊熊": 20,
    "R-百变熊熊": 30,
    "SR-百变熊熊 not SR-百变熊熊-父亲节 not SR-百变熊熊-七夕节限定 not SR-百变熊熊-非洲土著 not SR-百变熊熊-熊熊铁粉": 300,
    "SSR-百变熊熊 not SSR-百变熊熊-端午 not SSR-百变熊熊-熊熊铁军 not SSR-百变熊熊-熊熊强者 not SSR-百变熊熊-中秋限定": 1000,
    "SR-百变熊熊-七夕节限定": 50, # 熊熊奶嘴空投
    "SR-百变熊熊-父亲节": 50, # 空投
    "SR-百变熊熊-非洲土著": 50, # 三期购买6N（10）活动
    "SR-百变熊熊-熊熊铁粉": 50, # 三期购买盲盒积分第6-10名
    "SSR-百变熊熊-熊熊强者": 300, # 三期购买盲盒积分第2-5名
    "SSR-百变熊熊-端午": 300, # SSR空投
    "SSR-百变熊熊-熊熊铁军": 300, # 积分满200用户空投
    "SSR-百变熊熊-中秋限定": 300, # SSR、百变熊宝、奶嘴空投
    "熊熊碎片": 30, # 空投
    "熊熊奶嘴": 800, # 8R+20N合成
    #"青铜神像": 15, # 6N空投
    "白银神像": 15, # 3R空投
    "黄金神像": 100, # SR空投
    "钻石神像": 200, # SSR空投
    "熊熊蜜罐": 100, # 钻石神像空投

    # 佛系惠二
    "佛系创世": 3000,
    "大圆满": 500,
    "茶道": 100,
    "友情岁月": 100,

    # 敦煌菩萨
    "美女菩萨": 5.0,
    "美女菩萨-紫": 10.0,
    "美女菩萨-金": 20.0,
    "彩虹": 50.0,
    "满金": 100.0,
    "冥想小星星": 100,
    #"虎头飞天": 100,
    "丝道银河创世勋章": 500, # 1*满金+20普通 | 3*彩虹+1*小星星+1*虎头飞天+2*紫+20*普通 合成

    # 敦煌乐舞
    "乐舞伎楽图": 100,

    # UXON
    "重启柜子": 100.0,
    "无限柜子": 20,
    "憨勇小子": 10, # 合成SR-最勇划手
    "勤劳大叔": 8, # 合成R-劳动模范
    "尖嘴汉": 8, # 合成SR-农大户
    "聪明小子": 15, # 空投龙舟或端午粽子
    #"龙舟":(35,0,50), # 合成最勇划手
    "端午粽子": 20, # 聪明小子空投
    "最勇划手": 60, # 憨勇+龙舟合成
    "富家": 60,
    "怪力": 10, # 合成SR-农大户
    "村口": 8, # 合成R-劳动模范
    "拾荒": 20,
    "农大户": 100, # SR 1*R-怪力+2*N-尖嘴合成
    "劳动模范": 30, # R 1*N-村口+2*N-勤劳合成

    # BOBOSG
    #"曹操": 20,
    "刘备": 20,
    "诸葛亮": 20,
    "桃园结义": 20,

    # 潮虎
    "稀有款 ": 15,
    "史诗款 ": 100,
    "传说款 ": 100,

    # 中国航天
    "中国航天": 5,
    "动态纪念长卷": 100,
    "中国航天日金色版": 1000,
    "空间站": 100,

    # 离碳
    #"春之花": 60,
    #"夏之花": 30,
    "云起龙骧": 60,
    #"蝶恋花": 100,
    "原石": 150,
    "史诗卡牌": 500,
    "传奇卡牌": 300,

    # 天坛波普
    "天坛波普系列SS": 100,
    "天坛波普系列SSS": 100,
    "天坛波普系列": 50,

    # Limitless
    #"ACUEBEE": 15,
    #"ACUEBEE-003": 80,
    #"ACUEBEE-002": 80,
    "ACUEBEE-001": 20,
    "ACUEBEE-SP": 20,

    # 派对猫
    "派对猫首发纪念卡": 60,
    "派对猫#":700,

    # 西游星球
    "孙悟空-盲盒-LP": 20,
    "孙悟空-盲盒-OP": 500,

    # 凹凸世界
    "SSR-卡米尔": 5,
    "SSR-安迷修": 5,
    "UR": 15,
    "XR": 50,
}

BlindBox_Keywords_Dict = {
    # 百变熊熊
    "百变熊熊第三期": 100,
}

Target_Dict_1 = {
    # 淘派官方
    "乐淘淘": (2,3,50), # 乐淘淘
    #"": (2,5,600), # 光符
    #"内测": (2,1,4000),
    #"公测": (2,2,4000),
    "早鸟勋章": (2,0,10),
    #"钻石": (2,4,10000),
    "精英": (2,0,100),
    "创世王者勋章": (2,0,5000),
    "清凉": (2,0,5),

    # 烤仔的朋友
    "烤仔的朋友": (2,6,100),
    "Evo2k": (2,231,300),
    "金色款": (2,7,500),

    # 烤仔潮物
    #"清明": (7,9,300),
    #"复活": (7,9,300),

    # 凹凸世界
    #"SR-": (34,0,5.0),
    #"SSR-": (34,0,10.0),
    #"UR": (34,0,30.0),
    #"XR": (34,0,90.0),

    # 元气星空
    #"天坛": (22,0,400),

    # 百变熊熊
    "N-百变熊熊":(42,110,45),
    "R-百变熊熊":(42,111,90),
    "SR-百变熊熊":(42,112,500),
    "熊熊碎片":(42,128,50),

    # 佛系惠二
    "佛系创世": (32,0,1000),

    # 潮虎
    #"稀有": (37,27,80.0),
    "史诗": (37,28,300.0),
    "传说": (37,26,500.0),

    # 华策
    #"徽章海报":(26,0,300),
}

"""
Cookie_Dict_1 = {
# 173****6961
    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjM1NTg2MzksImlhdCI6MTY2MDk2NjYzOSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.fpVkL3etr3Svx5CHs6qpfnm7SI8SI1-i792bhgO39e0',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjA5NjcyMzksImlhdCI6MTY2MDk2NjYzOSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.Jw3VZEpO8408irpTmweBm5E_5sc7co4OPIylj5c5uzI',
    'cert': '1',
}
"""

Target_Dict_2 = {
    # 敦煌菩萨
    #"美女菩萨": (15,22,10.0),
    #"美女菩萨-紫": (15,96,50.0),
    #"美女菩萨-金": (15,96,100.0),
    "彩虹": (15,21,100.0),
    #"满金": (15,20,500.0),

    # 元气星空
    #"天坛": (22,0,400),

    # 敦煌乐舞
    #"乐舞伎楽图": (39,78,300),
    #"反弹琵琶": (39,74,50),

    # UXON
    "重启柜子": (35,0,200.0),
    "无限柜子": (35,0,30),
    "憨勇小子":(35,0,20),
    "勤劳大叔":(35,0,10),
    "尖嘴汉":(35,0,20),
    "聪明小子":(35,0,25),
    #"龙舟":(35,0,50),
    "粽子":(35,0,40),
    "划手":(35,0,100),
    "富家":(35,0,60),
    "怪力":(35,0,60),
    "村口":(35,0,25),
    "拾荒":(35,0,20),

    # 中国航天
    #"中国航天日金色版": (0,0,500),
    #"中国航天日绿色版": (40,70,100),
    #"祝融周岁纪念紫色版": (40,70,100),

    # 淘派官方
    #"创世王者勋章": (2,0,5000),
}

"""
Cookie_Dict_2 = {
# 159****9963
    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjUzNjU1MjMsImlhdCI6MTY2Mjc3MzUyMywidXNlclVJRCI6eyJ1c2VySWQiOjEyMDM5fX0.eWd1dPAw2QuCcJEU-JbmgVhUVZllHVs9PcnqYehFLeM',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjI3NzQxMjMsImlhdCI6MTY2Mjc3MzUyMywidXNlclVJRCI6eyJ1c2VySWQiOjEyMDM5fX0.QWiEhV_L8RRoV-TBiFR6m12VdAEUO3YFuB7RgegPDpg',
    'cert': '1',
}
"""