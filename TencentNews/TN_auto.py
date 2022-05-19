# coding: utf-8
#
import uiautomator2 as u2
import time

# 滚动到第一行图片上沿到屏幕顶端
NFT_1_1 = (0.5, 0.3)
NFT_2_1 = (0.5, 0.77)

BUY = (0.5, 0.88)

d = u2.connect_usb("3404842878006NG") # serial number

cnt = 0
while True:
    d.click(*NFT_1_1) 
    
    # for if pay failed and dialog box didn't appear in time
    """
    btn_pay_failed = d(resourceId="com.tencent.bamboo:id/tv_left_text")
    if btn_pay_failed.exists:
        btn_pay_failed.click()
    """
    btn_return = d(resourceId="com.tencent.news:id/title_bar_btn_back")
    # 等待页面加载
    while not btn_return.exists:
        pass
    # 等待购买按钮加载
    time.sleep(0.5)
    d.click(*BUY)
    # 等待付款对话框弹出
    time.sleep(3)

    # 付款对话框弹出后，返回按钮不出现，程序暂停
    btn_return = d(resourceId="com.tencent.news:id/title_bar_btn_back")
    while not btn_return.exists:
        pass
    """
    btn_pay_failed = d(resourceId="com.tencent.bamboo:id/tv_left_text")
    if btn_pay_failed.exists:
        btn_pay_failed.click()
    """

    # return to main page
    btn_return.click()

    cnt += 1
    if cnt % 100 == 0:
        print(f"****loop {cnt} times.")