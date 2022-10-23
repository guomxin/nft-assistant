# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import requests

try:
    from wxauto import WeChat
    WX = WeChat()
except:
    # for linux
    pass

FLAG = "TokenID:"

def get_tokenid_from_html_text(text):
    flag_pos = text.find(FLAG)
    if flag_pos != -1:
        items = text[flag_pos+len(FLAG):].strip().split()
        token_id = int(items[0])
        return token_id

def return_fig_count(idrange2name, fig_name):
    fig_count = 0
    for ((low,high), name) in idrange2name.items():
        if name == fig_name:
            fig_count += (high-low+1)
    return fig_count

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

def send_wx_msg(msg):
    try:
        WX.ChatWith("shark")
        WX.SendMsg(msg)
    except:
        pass

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



def dump_cookie_dict(select_id, cookie_dict):
    if select_id == 1:
        cookie_file_name = "config/cookie_dict_1.json"
    elif select_id == 2:
        cookie_file_name = "config/cookie_dict_2.json"
    with open(cookie_file_name, "w") as cookie_file:
        json.dump(cookie_dict, cookie_file)

def load_cookie_dict(select_id):
    if select_id == 1:
        cookie_file_name = "config/cookie_dict_1.json"
    elif select_id == 2:
        cookie_file_name = "config/cookie_dict_2.json"
    with open(cookie_file_name) as cookie_file:
        cookie_dict = json.load(cookie_file)
        return cookie_dict


if __name__ == "__main__":
    content = """
实时新增用户反馈132例，请相关同事注意。
>类型:用户反馈
>普通用户反馈:117例
>VIP用户反馈:<font color="comment">{}例</font>
""".format("1")
    send_workwx_msg("markdown", content)