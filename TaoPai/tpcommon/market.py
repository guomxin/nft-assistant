# coding: utf-8

Contract_Dict = {
    # 通过https://nft.taopainft.com/v1/market/v2/product/list接口返回获得contractId
    # 跟pid不一致
    37: 10, # 佛系惠二
}

Keywords_Dict = {
    # 淘派官方
    "乐淘淘": 50,
    "早鸟勋章": 10,
    "交易精英勋章": 100,
    "创世王者勋章": 5000,
    "清凉": 5,
    "绿码": 25,
    "测试大师": 100,

    # 烤仔的朋友
    "烤仔的朋友": 100,
    "金色款-烤仔的朋友": 1000,
    "Evo2k": 300,

    # 百变熊熊
    "N-百变熊熊": 45,
    "R-百变熊熊": 90,
    "SR-百变熊熊 not SR-百变熊熊-父亲节": 800,
    "SSR-百变熊熊 not SSR-百变熊熊-端午": 2000,
    "SR-百变熊熊-父亲节": 120, # 空投
    "SSR-百变熊熊-端午": 500, # 空投
    "熊熊碎片": 45, # 空投
    "熊熊奶嘴": 1000, # 8R+20N合成

    # 佛系惠二
    "佛系创世": 3000,
    "大圆满": 700,

    # 敦煌菩萨
    "美女菩萨": 10.0,
    "美女菩萨-紫": 50.0,
    "美女菩萨-金": 50.0,
    "彩虹": 100.0,
    "满金": 500.0,
    "冥想小星星": 200,
    #"虎头飞天": 100,
    "丝道银河创世勋章": 2000, # 1*满金+20普通 | 3*彩虹+1*小星星+1*虎头飞天+2*紫+20*普通 合成

    # 敦煌乐舞
    "乐舞伎楽图": 100,

    # UXON
    "重启柜子": 200.0,
    "无限柜子": 30,
    "憨勇小子": 20, # 合成SR-最勇划手
    "勤劳大叔": 20, # 合成R-劳动模范
    "尖嘴汉": 20, # 合成SR-农大户
    "聪明小子": 35, # 空投龙舟或端午粽子
    #"龙舟":(35,0,50),
    "端午粽子": 35, # 聪明小子空投
    "最勇划手-SR": 100, 
    "富家": 80,
    "怪力": 20, # 合成SR-农大户
    "村口": 20, # 合成R-劳动模范
    "拾荒": 30,
    "农大户": 200, # SR
    "劳动模范": 80, # R

    # BOBOSG
    "曹操": 20,
    "刘备": 60,
    "诸葛亮": 100,
    "桃园结义": 100,

    # 潮虎
    "稀有款 ": 60,
    "史诗款 ": 200,
    "传说款 ": 200,

    # 中国航天
    "中国航天": 5,
    "动态纪念长卷": 100,

    # 离碳
    #"春之花": 60,
    #"夏之花": 30,
    "云起龙骧": 80,
    "蝶恋花": 100,
    "原石": 250,

    # 天坛波普
    "天坛波普系列SS": 100,
    "天坛波普系列SSS": 100,
    "天坛波普系列": 50,

    # Limitless
    #"ACUEBEE": 15,
    #"ACUEBEE-003": 80,
    #"ACUEBEE-002": 80,
    "ACUEBEE-001": 100,
    "ACUEBEE-SP": 120,

    # 派对猫
    "派对猫首发纪念卡": 150,
    "派对猫#":700,
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

Cookie_Dict_1 = {
# 173****6961
    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjA5NjQ2NTcsImlhdCI6MTY1ODM3MjY1NywidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.JdS1RWd-47WCXHxsWKVUucyQBU3bEvuRmbIbKee2IqA',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTgzNzMyNTcsImlhdCI6MTY1ODM3MjY1NywidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.poUTz32L8U8y5kC7hT7bg4TuGDEOgrPxH6KTUezHPJA',
    'cert': '1',
}

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

Cookie_Dict_2 = {
# 159****9963
    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjAxNzU5MTMsImlhdCI6MTY1NzU4MzkxMywidXNlclVJRCI6eyJ1c2VySWQiOjEyMDM5fX0.2eb5RYfDy8QwEbed1-cYmeQ1W1Ca8TQqJSy9OVo567o',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTc1ODQ1MTMsImlhdCI6MTY1NzU4MzkxMywidXNlclVJRCI6eyJ1c2VySWQiOjEyMDM5fX0.LI36i2XzzsPrrew05YXQ_k7EeTbHGKDOdWn3dzdWjlg',
    'cert': '1',
}
