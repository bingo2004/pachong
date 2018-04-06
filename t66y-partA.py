#coding:utf-8
#python3
#通过1024图片目录页找出具体图片的地址
import re
from urllib import request
from time import sleep
from random import uniform

def url_to_file(url_page):
    req=request.Request(url_page)
    req.add_header('User-Agent',header2)
    data=request.urlopen(req).read().decode('gbk')
#    print(data)
    pattern=re.compile('<title>(.*?\[\d+P\]).*?</title>')
    name=re.search(pattern,data)
    if name:
        name=name.group(1)
    else:
        name='not got name'
    print("name = %s"%name)
    pattern=re.compile('http[s]?://[\w\./_-]+.jpg')
    url_pic=re.findall(pattern,data)
    return name,url_pic

url = 'http://t66y.com/thread0806.php?fid=8'
header1 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
header2 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0'
req = request.Request(url)
req.add_header('User-Agent',header1)
data = request.urlopen(req).read().decode('gbk')

pattern=re.compile('<h3><a href="(.*?)"')
urls=re.findall(pattern,data)
urllist=[]
for j in urls[5:]:
    urllist.append('http://t66y.com/'+j)
print("get %d url_pages"%len(urllist))

name=''
url_pic=[]
f=open('url_pic.txt','wb')
f.write(("get %d url_pages\n"%len(urllist)).encode())
num=1
for url_page in urllist[:]:
    sleep(uniform(0,3))
#    sleep(1)
    name,url_pic=url_to_file(url_page)
    print("get %d url_pics named: %s\n"%(len(url_pic),name))
#    f.write(name.encode())
    f.write(("%d-%s\n"%(num,name)).encode())
    num+=1
    for l in url_pic:
        f.write(("%s\n"%l).encode())
f.close()
