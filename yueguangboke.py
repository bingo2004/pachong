#coding:utf-8
#python3
#爬虫月光博客，实现保存到本地txt
import re
from urllib import request
from time import time,localtime

def yueguang():
    t=localtime(time())
    today=str(t.tm_year)+'年'+str(t.tm_mon)+'月'+str(t.tm_mday)+'日'
#    print('today is %s\n'%today)
    FenGeXian='-'*10
    url = 'http://www.williamlong.info/'
    req = request.Request(url)
    header1 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    header2 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0'
    req.add_header('User-Agent',header1)
    with request.urlopen(req) as f:
        data = f.read()
#        print('status: ',f.status, f.reason)
        '''
        for k,v in f.getheaders():
            print('%s: %s' % (k,v))
        '''
        data = data.decode('utf-8')
    #    print(data)
    #    pattern = re.compile(u'content">\s*<span>\s*(\s.*?\s)\s*</span>.*?(\d+)</i>.*?(\d+)</i>',re.S)
        pattern = re.compile(u'<h4.*?>([\d\w]*?)</h4>.*?rel="bookmark">(.*?)</a></h2>.*?/></a>(.*?)<p style',re.S)
        items = re.findall(pattern,data)
        fp = open('jrtt.txt','a')
        n=0
    #    today='2018年3月30日'
        for each in items:
            if each[0]==today:
                print('geted')
                fp.write("%s\n%s\n%s\n%s\n"%(each[0],each[1],each[2],FenGeXian))
                n+=1
        fp.close()
        print('已经为您抓取n=:%d条今日月光博客! '%n)

if __name__=='__main__':
    yueguang()
