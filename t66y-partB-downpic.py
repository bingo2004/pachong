#coding:utf-8
#python3
import re
from urllib import request
from time import sleep
from random import randint

import socket
socket.setdefaulttimeout(30) #urllib.request的timeout

goodint = [10,11,18,20,21,25,26,27,29,30,33,35,42,43,44,45,46,48,49,61,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,91,93,95,96]#手动分辨值得下载的图片
good = [str(i) for i in goodint]
print(good)

download_num=[0,0]

header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
header2 = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0','Cookie': 'AspxAutoDetectCookieSupport=1',}
header3 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
headers=(header1,header2,header3)

def downpic(url,name,n):
    print('begin to download %s %d\n'%(name,n))
    '''
    headers = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'
        ]
        '''
    req = request.Request(url,None,headers[randint(0,2)])
#    req.add_header('User-Agent',headers[randint(0,2)])

    try:
        pic=request.urlopen(req)
        fp=open('pic/'+name+str(n)+'.jpg','wb')
        fp.write(pic.read())
        fp.close()
        print('status:',pic.status,pic.reason)
        download_num[0]+=1
        '''
        for k,v in pic.getheaders():
            print('%s:  %s'%(k,v))
        '''
    except Exception:
        print("download error")
        download_num[1]+=1
        return

ftxt = open('url_pic.txt','rb')
name = 'not named'
num=1
for eachline in ftxt:
    line=eachline.decode('utf-8').strip()
    ##每下载10张，sleep 3-5秒
    if download_num[0]%10:
        sleep(randint(0,2))
    print("read line: %s"%line)
    if re.match('http',line):
        if num>0:  #每个页面不超过30张
#        if name[:2] in good and num>6:  #每个页面不超过30张
            downpic(line,name,num)
        num+=1
        print("download-yes=%s : download-no=%s\n\n\n "%(download_num[0],download_num[1]))
    else:
        name=line
        print("name is: %s"%name)
        num=1
#        sleep(randint(1,3))
ftxt.close()
