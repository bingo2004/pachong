#coding:utf-8
#python3
#爬虫bowen，网页源码无法decode，试图'utf-8'/'gbk'/'latin1'等，都没有成功
import re
from urllib import request
from time import time,localtime

t=localtime(time())
today=str(t.tm_year)+'年'+str(t.tm_mon)+'月'+str(t.tm_mday)+'日'
print('today is %s\n'%today)
FenGeXian='-'*10

def bowen():
    url = 'https://bowenpress.com/news/bowen_192643.html'
#    url = 'https://bowenpress.com/'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    req = request.Request(url,None,header)
    with request.urlopen(req) as f:
        data = f.read()
        print('status: ',f.status, f.reason)
        for k,v in f.getheaders():
            print('%s: %s' % (k,v))
    data = data.decode()
    print(data)
    '''
    data = data.decode('utf-8')
    data = data.decode('latin1')
    data = data.decode("ISO-8859-1")
    data = data.decode()
'''

    '''
    pattern = re.compile(b'title="(.*?)" rel="nofollow">Read More<',re.S)
#    pattern = re.compile(b'(\d{4}年\d{1,2}月\d{1,2}日).*?title="(.*?)" rel="nofollow">Read More<',re.S)
    items = re.findall(pattern,data)
    print(items[0])
#    print(items)

    fp = open('bowen-top.txt','w')
    fp.write('今日博文头条\t%s\n'%today)
    n=1
    for each in items:
        if each[0]==today:
            n+=1
            fp.write('%d: %s\n'%(n,each[1]))
    fp.close()
    print('已经为您抓取今日十大! ')
    '''
if __name__=='__main__':
    bowen()
