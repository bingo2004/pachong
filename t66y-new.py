#coding:utf-8
#python3
#通过1024图片目录页找出具体图片的地址
import re
from urllib import request
from time import sleep
from random import uniform
import os

def url_to_file(url_page,num):
    req=request.Request(url_page)
    req.add_header('User-Agent',header2)
    data=request.urlopen(req).read().decode('gbk')
    pattern=re.compile('<title>(.*?\[\d+P\]).*?</title>')
    name=re.search(pattern,data)
    if name:
        name=name.group(1)
    else:
        return
        name='not got name'
    name=name.replace(' ','_')
    name = str(num)+'_'+name
    print("name = '%s'"%name)
    pattern=re.compile('http[s]?://[\w\./_-]+.jpg')
    url_pic=re.findall(pattern,data)
    for i,url in enumerate(url_pic):
        os.system("aria2c -d ./pic/%s %s"%(name,url))
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
num = 0
for each_url in urls[5:6]:#排除掉置顶帖
    num += 1
    each_url = 'http://t66y.com/'+each_url
    url_to_file(each_url,num)
print("get %d url_pages"%len(urls)-5)
