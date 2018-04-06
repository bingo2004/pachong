#coding:utf-8
#python3
import re
from urllib import request
from time import sleep
from random import randint 

url = 'http://www.360docs.net/doc/info-c0974771bb68a98271fefae2-'
#i-页数
url2 = '.html'

header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
header2 = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Cookie': 'AspxAutoDetectCookieSupport=1',}
header3 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
headers=(header1,header2,header3)

name='scttwl'
for i in range(66,180):
    i+=1
    print("begin to download page%s "%i)
    urli=url+str(i)+url2
#    req=request.Request(urli)
    req=request.Request(urli,None,headers[randint(0,1)])
#    req.add_header('User-Agent',header1)
    data=request.urlopen(req).read().decode('utf-8')
    pattern=re.compile('class="img"><img src="(.*?)" alt')
    m=re.search(pattern,data)
    if m:
        url_pic = 'http://appwk.baidu.com/naapi/doc'+m.group(1)[4:]
#        print(url_pic)
        print("the url address of page%d is getted"%i)
    else:
        print("page%d is not found"%i)
        break
#    req = request.Request(url_pic)
    req=request.Request(url_pic,None,headers[randint(1,2)])
#    req.add_header('User-Agent',header1)
    try:
        pic=request.urlopen(req)
        fp=open('实测天体物理/'+name+str(i),'wb')
        fp.write(pic.read())
        fp.close()
        print('status:',pic.status,pic.reason,'\n page%s has been downloaded'%i)
        '''
        for k,v in pic.getheaders():
            print('%s: %s' %(k,v))
        '''
    except Exception:
        print('download error\n')
    print("sleep...\n\n\n")
    sleep(randint(0,10))
