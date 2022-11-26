# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import requests
import time
import hashlib

def send_msg(from_addr, password, to_addr, msg_text):
    smtp_server = "smtp.qq.com"

    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    server.login(from_addr, password)
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = msg_text
    msg.attach(MIMEText(msg_text, "plain", "utf-8"))
    server.sendmail(from_addr, to_addr, msg.as_string())

    server.quit()

def get_md5_hash(s3):
    _0x14b4f0 = ["e9", "0a", "9", "29", "e", "c" , "3"]
    merged = str(s3) + "".join(_0x14b4f0)
    return hashlib.md5(merged.encode(encoding="utf-8")).hexdigest()

"""
光予api于2022/11/25发生升级，需要时间戳验证
"""
def decorate_api_data(data):
    s2 = int(time.time() * 1000)
    s1 = s2 - 20000
    s3 = s2 + 20000
    s4 = s2 + 40000
    data["s1"] = s1
    data["s2"] = s2
    data["s3"] = s3
    data["s4"] = s4
    data["s5"] = get_md5_hash(s3)
    return data

def post_requests_json(url, data, timeout, decorate=False):
    for _ in range(100):
        try:
            if decorate:
                data = decorate_api_data(data)
            res = requests.post(url, data=data, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(1)
            print(e)

StockValue_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=692ffa3b-8c4d-4b98-87fe-15561e7e4edb"
TradingValue_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=44b129f9-747b-4797-8ccb-250c1d8b0dbe"
SpecialAccStatus_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6b8b7734-9f97-4d13-b07d-cafed27bac92"
GrabNFTs_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ed5e492a-f936-4cb9-b547-cd49d09b5182"
HoldingShare_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=1d39cbe8-2697-4599-8472-e38ce7ccbd48"

Ext_HeiLongStatus_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=40027396-e35e-43ad-9232-d37850bf2125"

StockValue_MSG = 0
TradingValue_MSG = 1
SpecialAccStatus_MSG = 2
GrabNFTs_MSG = 3
HoldingShare_MSG = 5

Ext_HeiLongStatus_MSG = 4

Notification_Config = {
    StockValue_MSG: [StockValue_WebHook_URL],
    TradingValue_MSG: [TradingValue_WebHook_URL],
    SpecialAccStatus_MSG: [SpecialAccStatus_WebHook_URL],
    GrabNFTs_MSG: [GrabNFTs_WebHook_URL],
    HoldingShare_MSG: [HoldingShare_WebHook_URL],
    
    Ext_HeiLongStatus_MSG: [Ext_HeiLongStatus_WebHook_URL],
}

def send_workwx_msg_agg(msg_id, msg_type, content):
    if msg_id not in Notification_Config:
        return
    for webhook_url in Notification_Config[msg_id]:
        send_workwx_msg(msg_type, content, webhook_url)

def send_workwx_msg(msg_type, content, webhook_url):
    for _ in range(10):
        try:
            data = None
            if msg_type == "text":
                data = {
                    "msgtype": msg_type,
                    "text": {
                        "content": content
                    }
                }
            elif msg_type == "markdown":
                data = {
                    "msgtype": msg_type,
                    "markdown": {
                        "content": content
                    }
                }        

            if data:
                requests.post(webhook_url, data=json.dumps(data))
            return
        except Exception as e:
            print(e)