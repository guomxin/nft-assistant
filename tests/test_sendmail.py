import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_addr = "1621949016@qq.com"
password = "crtlhcujsozpdidc"
to_addr = "1621949016@qq.com"
smtp_server = "smtp.qq.com"

server = smtplib.SMTP_SSL()
server.connect(smtp_server, 465)
server.login(from_addr, password)
msg = MIMEMultipart()
msg['From'] = from_addr
msg["To"] = to_addr
msg["Subject"] = "烤仔的朋友 100.0"
msg.attach(MIMEText("烤仔的朋友 100.0", "plain", "utf-8"))
server.sendmail(from_addr, to_addr, msg.as_string())

server.quit()