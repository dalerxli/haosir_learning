# -*- coding:UTF-8 -*-
from urllib import request
import requests
from bs4 import BeautifulSoup
import sys
def getonecheap(url):
    download_url = url
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
    download_req = request.Request(url = download_url, headers = head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk','ignore')
    soup_texts = BeautifulSoup(download_html, 'lxml')
    # print(soup_texts)
    texts = soup_texts.find_all(id="content")
    soup_text = BeautifulSoup(str(texts), 'lxml')
    result=soup_text.div.text.replace('\xa0\xa0','\n')
    return result

def gettable():
    server = 'http://www.biqubao.com'
    target_url = 'https://www.biqubao.com/book/1716/'
    head = {}
    name=[]
    HREF=[]
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档树,找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',id = 'list')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    a = download_soup.find_all('a')
    for each in a:
        name.append(each.string)
        HREF.append(server + each.get('href'))
    return name,HREF
def writer( name, path, text):
    write_flag = True
    with open(path, 'a', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n\n')
if __name__ == "__main__":
    print('《戮仙》开始下载：')
    name,herf=gettable()
    lenth=len(name)
    i=0
    while(i<lenth):
        noveltext=getonecheap(herf[i])
        writer(name[i], '戮仙.txt', noveltext)
        print("第%d章"%i)
        i=i+1
    print('《戮仙》下载完成')