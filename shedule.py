#coding:utf-8
import sendmail1
from time import time,localtime,ctime,sleep
from qiubai import qiubai
from smth import smth
from yueguangboke import yueguang
from zhihudaily import daily
from dongqiudi import dqd
from main import main

while 1:
    t=localtime(time())
    today=str(t.tm_year)+'年'+str(t.tm_mon)+'月'+str(t.tm_mday)+'日'
    print('today is %s\n'%today)
    w=ctime().split(' ')[0] #星期几

    if t.tm_hour==6:
        try:
            main()
        except Excption:
            print('error!')
        sleep(30000)
    if t.tm_hour==16 and t.tm_min>30:
        try:
            main()
        except Excption:
            print('error!')
        sleep(30000)
    sleep(1800)
