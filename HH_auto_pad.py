# coding: utf-8
#
import uiautomator2 as u2

# for 4 NFTs
# scroll to the bottom
NFT_1_1 = (0.254, 0.07)
NFT_1_2 = (0.734, 0.07)
NFT_2_1 = (0.254, 0.486)
NFT_2_2 = (0.734, 0.486)

#d = u2.connect()
d = u2.connect_usb("WER9X19702003497") # serial number

cnt = 0
while True:
    #d.click(*REFRESH)
    d.click(*NFT_2_1)
    
    btn_buy = d(resourceId="com.tencent.bamboo:id/btn_buy") # TODO： try click with coordinates
    btn_return = d(resourceId="com.tencent.bamboo:id/left_icon")
    
    btn_buy.click()
    btn_pay_failed = d(resourceId="com.tencent.bamboo:id/tv_left_text")
    if btn_pay_failed.exists:
        btn_pay_failed.click()

    # return to main page
    btn_return.click()
    
    cnt += 1
    if cnt % 100 == 0:
        print(f"****loop {cnt} times.")

    '''
    btn_buy = d(resourceId="com.tencent.bamboo:id/btn_buy")
    if btn_buy.get_text() == "已售罄":
        d(resourceId="com.tencent.bamboo:id/left_icon").click()
    else:
        btn_buy.click()
    '''