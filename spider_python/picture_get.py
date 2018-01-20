# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.request import urlretrieve
purl='https://pixabay.com/zh/photos/?order=ec&pagi='
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
def getimage(url):
    r = requests.get(url, headers)
    pattern = re.compile(r'src="(.*?)" alt="(.*?)" title=')
    img = re.findall(pattern, r.text)
    URL=[]
    title=[]
    for image in img:
        URL.append(image[0])
        title.append(image[1].split(',')[0])
    return URL,title
def getauthor(url):
    r = requests.get(url, headers)
    pattern = re.compile(r'<a href="/users/(.*?)">(.*?)</a>' )
    author=[]
    words = re.findall(pattern, r.text)
    for word in words:
        author.append(word[1])
    return author
def loadimg(URL,page,author,name):
    urlretrieve(URL, '收集图片\\'+'page'+str(page)+'_'+author+'_'+name+".jpg")
if __name__=="__main__":
    i=1
    print('开始收集')
    while(i<10):
        url=purl+str(i)
        img, title = getimage(url)
        author = getauthor(url)
        lenth=len(img)
        j=0
        while(j<15):
            loadimg(img[j],i,author[j],title[j])
            print(i,j)
            j+=1
        i+=1
    print('结束战斗')










