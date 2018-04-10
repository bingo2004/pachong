#coding:utf-8
#python3    #爬虫smth
import re
from urllib import request
from time import ctime

def smth():
    url = 'https://m.newsmth.net'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
    try:
        req = request.Request(url,None,header)
        with request.urlopen(req) as f:
            data = f.read()
        data = data.decode('utf-8')
    #   print(data)
        pattern = re.compile(u'<li>(\d{1,2})\|<a href="(.*?)">(.*?)\(<span',re.S)
        items = re.findall(pattern,data)
    except Exception:
        print("Error!")
        return

#    fp = open('smth-top10.txt','w')
    fp = open('jrtt.txt','a')
    fp.write('*'*15+'\n'+'今日水木十大\t%s\n'%ctime()+'*'*15+'\n\n')
    for each in items:
        fp.write(('No%s: %s\n'%(each[0],each[2])))
        urlnew=url+each[1]
        fp.write(urlnew+'\n')
#        print(urlnew)
        req_i=request.Request(urlnew,None,header)
        with request.urlopen(req_i) as fi:
#            print('prepare to open url_i')
            data_new = fi.read().decode('utf-8')
        pattern_i = re.compile(u'<div\sclass=\"sp\">(.*?)<\/div></li>',re.S)
        item = re.search(pattern_i,data_new)
        if item:
            content = item.group(1)[:100]
        else:
            content = "the page has gone!!"
        fp.write(('%s\n\n'%content))
    fp.close()
    print('已经为您抓取今日水木十大! ')

if __name__=='__main__':
    smth()
