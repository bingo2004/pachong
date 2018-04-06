#coding:utf-8
import re
import requests

words = raw_input("please input keywords you want to search in baidu_image:  \n")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='+words
html = requests.get(url).text
#(.*?),其中 ?的作用是将*转化为懒惰模式
#re.S 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。
pic_url = re.findall('"objURL":"(.*?)"',html,re.S)
i = 1
for each in pic_url:
    print '下载图片',i
    print each
    try:
        pic = requests.get(each,timeout=10)
    except requests.exceptions.ConnectionError:
        print '无法下载图片'
        continue
    string = './pictures_'+words+'_'+str(i)+'.jpg'
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i+=1
    if i>5:
        break
