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

def send_workwx_msg(msg_type, content):
    webhook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=692ffa3b-8c4d-4b98-87fe-15561e7e4edb"
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

def post_requests_json(url, data, timeout):
    for _ in range(100):
        try:
            res = requests.post(url, data=data, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(1)
            print(e)