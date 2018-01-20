# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.request import urlretrieve
url='https://www.qiushibaike.com/8hr/page/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
def getwords(num):
    newnurl=url+str(num)+'/'
    r = requests.get(newnurl,headers)
    page=[]
    soup=BeautifulSoup(r.text,'lxml')
    words=soup.findAll('div',class_='content')
    for word in words:
        page.append(word.get_text().replace('\n\n\n','\n'))
    return(page)
def listtotext(path,page):
    with open(path, 'a', encoding='utf-8') as f:
        f.writelines(page)
        f.write('\n')
#图片部分重定向，未成功
# def getimage(num):
#     newnurl = 'https://www.qiushibaike.com/imgrank/'
#     r = requests.get(newnurl, headers)
#     pattern = re.compile(r'src="(.*?)" alt=')
#     img = re.findall(pattern, r.text)
#     print(img)
# def listtoimg(pagenum,img):
#     i=0
#     for image in img:
#         if i==0:
#             i += 1
#             continue
#         urlretrieve(image, str(pagenum)+'_'+str(i)+'.png')
#         i+=1

if __name__=="__main__":
    maxpage=13
    i=1
    print('开始下载')
    while(i<maxpage+1):
        page=getwords(i)
        listtotext('糗事百科\\'+'page'+str(i)+'.txt',page)
        # imge=getimage(i)
        # listtoimg(i,imge)
        i=i+1
    print("运行完毕")






