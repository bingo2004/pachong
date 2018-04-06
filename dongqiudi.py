#coding:utf-8
#python3    #爬虫smth
import re
from urllib import request
from time import ctime

def dqd():
    url = 'https://www.dongqiudi.com'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
    req = request.Request(url,None,header)
    with request.urlopen(req) as f:
        data = f.read()
#        print('status: ',f.status, f.reason)
#        for k,v in f.getheaders():
#            print('%s: %s' % (k,v))
    data = data.decode('utf-8')
#   print(data)
    pattern = re.compile(u'<a href="(.{1,50})" target="_blank">.*?<h3>([\S]{10,100})</h3>',re.S)
    items = re.findall(pattern,data)
#    print(items)
    fp = open('jrtt.txt','a')
    fp.write('\n'+'*'*15+'\n'+'今日懂球帝头条\t%s\n'%ctime()+'*'*15+'\n')
    num = 0
    for each in items:
        num+=1
        fp.write(('No%s: %s\n'%(num,each[1])))
        fp.write(each[0]+'\n'*2)
    fp.close()
    print('已经为您抓取今日懂球帝头条! ')
if __name__=='__main__':
    dqd()
