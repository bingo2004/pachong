#coding:utf-8
#python3
#通过1024图片目录页找出具体图片的地址
import re
from urllib import request
from time import sleep
from random import uniform
import os

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
        return
        name='not got name'
    name=name.replace(' ','_')
    os.system('mkdir %s'%name)
    print("name = '%s'"%name)
    pattern=re.compile('http[s]?://[\w\./_-]+.jpg')
    url_pic=re.findall(pattern,data)
    for i,url in enumerate(url_pic):
        os.system("aria2c -d ./%s %s"%(name,url))
    return

#新时代的我们
url = 'http://t66y.com/thread0806.php?fid=8'
#达尔的旗帜
#url = 'http://t66y.com/thread0806.php?fid=16'
header1 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
header2 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0'
req = request.Request(url)
req.add_header('User-Agent',header1)
data = request.urlopen(req).read().decode('gbk')

pattern=re.compile('<h3><a href="(.*?)"')
urls=re.findall(pattern,data)
urllist=[]
for j in urls[:5]:
    urllist.append('http://t66y.com/'+j)
print("get %d url_pages"%len(urllist))

url_pic=[]
num=1
for url_page in urllist[:]:
    url_to_file(url_page)
