# coding: utf-8
#
import uiautomator2 as u2

NFT_1_1 = (0.254, 0.211)
NFT_1_2 = (0.734, 0.211)
NFT_2_1 = (0.254, 0.522)
NFT_2_2 = (0.734, 0.522)
NFT_3_1 = (0.254, 0.832)
NFT_3_2 = (0.734, 0.832)

REFRESH = (0.5, 0.05)

d = u2.connect()

while True:
    #d.click(*REFRESH)
    d.click(*NFT_2_2)
    
    btn_buy = d(resourceId="com.tencent.bamboo:id/btn_buy") # TODO： try click with coordinates
    btn_return = d(resourceId="com.tencent.bamboo:id/left_icon")
    
    btn_buy.click()
    btn_return.click()
    
    '''
    btn_buy = d(resourceId="com.tencent.bamboo:id/btn_buy")
    if btn_buy.get_text() == "已售罄":
        d(resourceId="com.tencent.bamboo:id/left_icon").click()
    else:
        btn_buy.click()
    '''