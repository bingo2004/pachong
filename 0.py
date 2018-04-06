#coding:utf-8
import sendmail
from time import time,localtime,ctime,sleep
from qiubai import qiubai
from smth import smth
from yueguangboke import yueguang
from zhihudaily import daily
from dongqiudi import dqd

while 1:
    t=localtime(time())
    today=str(t.tm_year)+'年'+str(t.tm_mon)+'月'+str(t.tm_mday)+'日'
    print('today is %s\n'%today)
    w=ctime().split(' ')[0] #星期几

    if t.tm_hour=21:
        fp = open('jrtt.txt','w')
        fp.write('*'*25+'\n'+ctime()+'\n'+'*'*25+'\n')
        fp.close()
        smth()
        dqd()
        qiubai()
        yueguang()
        daily()
        sendmail.sendMail('正文','jrtt.txt')
        print("邮件已发送！\t Sleeping......")
        sleep(3600)
