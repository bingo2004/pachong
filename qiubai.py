#coding:utf-8
#python3
#爬虫糗百，实现保存到本地txt
import re
from urllib import request
from time import ctime

def qiubai():
    url = 'https://www.qiushibaike.com/text/'
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
        pattern = re.compile(u'content">\s*<span>\s*(\s.*?\s)\s*</span>.*?(\d+)</i>.*?(\d+)</i>',re.S)
        items = re.findall(pattern,data)
#        fp = open('qiushibaike-3000like.txt','wb')
        fp = open('jrtt.txt','a')
        fp.write('\n'*5+'*'*15+'\n'+'糗事百科新鲜段子\t'+ctime()+'\n'+'*'*15+'\n')
        n=0
        for each in items:
            if int(each[1])>3000:
                n+=1
                fp.write(('\n\nNo'+str(n)+':\t'+each[1]+' like赞'))
                fp.write(each[0])
        fp.close()
        print('已经为您抓取n=:%d条超过3000赞的段子! '%n)

if __name__=='__main__':
    qiubai()
