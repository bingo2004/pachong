#coding:utf-8
import sendmail1
from time import time,localtime,ctime,sleep
from qiubai import qiubai
from smth import smth
from yueguangboke import yueguang
from zhihudaily import daily
from dongqiudi import dqd

def main():
    fp = open('jrtt.txt','w')
    fp.write('*'*25+'\n'+ctime()+'\n'+'*'*25+'\n')
    fp.close()
    smth()
    dqd()
    qiubai()
    yueguang()
    daily()
    sendmail1.sendMail('正文','jrtt.txt')
    print("邮件已发送！\t Sleeping......")
