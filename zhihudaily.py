#coding:utf-8
#python3
import re
from urllib import request
from time import ctime

def daily():
    url = 'https://daily.zhihu.com'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
    req = request.Request(url,None,header)
    with request.urlopen(req) as f:
        data = f.read()
    data = data.decode('utf-8')
#   print(data)
    pattern = re.compile(u'<a href="(/story.+?)".*?<span class="title">([\S]+)</span>',re.S)
    items = re.findall(pattern,data)
#    print(items)
    fp = open('jrtt.txt','a')
    fp.write('\n'+'*'*15+'\n'+'知乎日报头条\t%s\n'%ctime()+'*'*15+'\n')
    num = 0
    for each in items:
        num+=1
        each_url=url+each[0]
        fp.write(('No%s: %s\n%s\n\n'%(num,each[1],each_url)))
        if num>5:
            break   #只显示５条
    fp.close()
    print('已经为您抓取今日知乎日报! ')
if __name__=='__main__':
    daily()
