#coding:utf-8
#python3
#测试利用163发送邮件成功
import smtplib
from os import environ

def sendMail(body):
    smtp_server = 'smtp.163.com'
    from_mail = 'zhangbinbin2004@163.com'
    mail_pass = environ.get('MAIL_PASSWORD')
    to_mail = ['398778369@qq.com','zhangbinbin2004@163.com']
    cc_mail = []
    from_name = 'bingo'
    subject = u'测试'.encode('utf-8')
    mail = [
            'From: %s <%s>' %(from_name, from_mail),
            'To: %s' %','.join(to_mail),
            'Subject: %s' %subject,
            'Cc: %s' %','.join(cc_mail),
            '',
            body
            ]
    msg = '\n'.join(mail)

    try:
        s = smtplib.SMTP()
        s.connect(smtp_server, '25')
        s.login(from_mail,mail_pass)
        s.sendmail(from_mail,to_mail+cc_mail,msg)
        s.quit()
    except smtplib.SMTPException as e:
        print("Error: %s" %e)

if __name__=='__main__':
    sendMail('This is a test!')

