# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import requests
import time

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

def post_requests_json(url, data, timeout):
    for _ in range(100):
        try:
            res = requests.post(url, data=data, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(1)
            print(e)

StockValue_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=692ffa3b-8c4d-4b98-87fe-15561e7e4edb"
TradingValue_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f6aadc37-076c-45ad-85d9-ccfe52df7b5f"
SpecialAccStatus_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6b8b7734-9f97-4d13-b07d-cafed27bac92"
GrabNFTs_WebHook_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ed5e492a-f936-4cb9-b547-cd49d09b5182"

StockValue_MSG = 0
TradingValue_MSG = 1
SpecialAccStatus_MSG = 2
GrabNFTs_MSG = 3

Notification_Config = {
    StockValue_MSG: [StockValue_WebHook_URL],
    TradingValue_MSG: [TradingValue_WebHook_URL],
    SpecialAccStatus_MSG: [SpecialAccStatus_WebHook_URL],
    GrabNFTs_MSG: [GrabNFTs_WebHook_URL],
}

def send_workwx_msg_agg(msg_id, msg_type, content):
    if msg_id not in Notification_Config:
        return
    for webhook_url in Notification_Config[msg_id]:
        send_workwx_msg(msg_type, content, webhook_url)

def send_workwx_msg(msg_type, content, webhook_url):
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
    except Exception as e:
        print(e)