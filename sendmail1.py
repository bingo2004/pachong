#coding:utf-8
#python3
#update: 将附件内容直接放在邮件正文，因为kindle无法识别ｖｐｓ发出的附件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from os import environ

def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(), addr))

def sendMail(body, attachment):
    smtp_server = 'smtp.163.com'
    from_mail = environ.get('MAIL_USERNAME')
    mail_pass = environ.get('MAIL_PASSWORD')
    to_mail = ['zhangbinbin2004@163.com']
    msg = MIMEMultipart()
    #Header对中文进行编码
    msg['From'] = formatAddr('服务器 <%s>'% from_mail)#.encode()
    msg['To'] = ','.join(to_mail)
    msg['Subject'] = Header('来自Python的新闻','utf-8').encode()

    f = open(attachment,'r')
    body = f.read()
    f.close()
    msg.attach(MIMEText(body,'plain','utf-8'))

    try:
        s = smtplib.SMTP_SSL()
        s.connect(smtp_server, '465')
        s.login(from_mail,mail_pass)
        s.sendmail(from_mail, to_mail, msg.as_string())
        s.quit()
    except smtplib.SMTPException as e:
        print("Error: %s"%e)

if __name__ == '__main__':
    sendMail('测试邮件附件','jrtt.txt')
