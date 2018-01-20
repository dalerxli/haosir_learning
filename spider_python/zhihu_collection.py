# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
from multiprocessing import Pool
from functools import partial
import time
purl='https://www.zhihu.com/collection/19633591?page='
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
def init(i):
    url=purl+str(i)
    s = requests.Session()
    s.headers.update(header)
    words= s.get(url)
    return words.text
def get_answer(word):
    question=[]
    answer=[]
    soup=BeautifulSoup(word,'lxml')
    ques=soup.find_all('h2',class_="zm-item-title")
    for que in ques:
        question.append(que.get_text())
    anss=soup.find_all('textarea', class_="content")
    for ans in anss:
        temp=[]
        text_hidden=ans.text.encode('utf-8')
        soup_temp = BeautifulSoup(text_hidden, "lxml")
        ptexts = soup_temp.find_all('p')
        for ptext in ptexts:
            temp.append(ptext.get_text())
        answer.append(temp)
    return question,answer
def load(path,ques,ans):
    lenth=len(ques)
    with open(path,'w',encoding='utf-8') as f:
            for i in range(lenth):
                print(i)
                f.write(ques[i])
                f.write('\n')
                for j in range(len(ans[i])):
                    if ans[i][j]!=None:
                        f.write(ans[i][j])
                        f.write('\n')
                f.write('\n')
#单进程
# if __name__=="__main__":
#     i=0
#     while(i<10):
#         i+=1
#         word=init(i)
#         que,ans=get_answer(word)
#         del(que[0])
#         load('知乎收藏\\'+'page'+str(i)+'.txt', que, ans)
#         print('over')
#多进程
def main(page):

    word=init(page)
    que,ans=get_answer(word)
    del(que[0])
    load('知乎收藏\\'+'page'+str(page)+'.txt', que, ans)
    print('over')
if __name__ == "__main__":
    pool = Pool(processes=4)
    start = time.time()
    #如果想全部下载的话 range(1,int(pagenum)+1)
    #测试时候参数可以设置成range(1,3)
    pool.map_async(main, range(1,20))
    pool.close()
    pool.join()
    stop = time.time()
    print (stop-start)







