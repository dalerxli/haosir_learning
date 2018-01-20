# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.request import urlretrieve
from multiprocessing import Pool
from multiprocessing import Process
from functools import partial
import time
def init(url):
    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
    s = requests.Session()
    s.headers.update(header)
    s.headers.update({"authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20"})
    ret=s.get(url,timeout=5)
    return s
def get_answer(s,qid,limit,offset):
    params={
        'sort_by':'default',
        'include':'data[*].is_normal,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].author.follower_count,badge[?(type=best_answerer)].topics',
        'limit':limit,
        'offset':offset
    }
    url ="https://www.zhihu.com/api/v4/questions/"+qid+"/answers"
    return s.get(url,params=params,timeout=5)
def get_all_answers(url):
    session = init(url)
    q_id = url.split('/')[-1]
    offset = 0
    limit=20
    answers=[]
    is_end=False
    while not is_end:
        ret=get_answer(session,q_id,limit,offset)
        #total = ret.json()['paging']['totals']
        answers+=ret.json()['data']
        is_end= ret.json()['paging']['is_end']
        print("Offset: ",offset)
        print("is_end: ",is_end)
        offset+=limit
    return(answers)
def get_picture(folder,ans):
    if not os.path.exists(folder):
        os.makedirs(folder)
    print("start")
    jpg = re.compile(r'https://[^\s]*?_hd\.jpg')
    words = re.findall(jpg,ans)
    img=list(set(words))
    lenth=len(img)
    for i  in range(lenth):
        urlretrieve(img[i], folder+'\\'+'img_' + str(i) + ".jpg")
        print(i)
    print('over')
#使用多进程Pool库
# def main(i):
#     urls = ['https://www.zhihu.com/question/28853910','https://www.zhihu.com/question/67553801','https://www.zhihu.com/question/20196263','https://www.zhihu.com/question/25911498']
#     folder='C:\pylearning\\newtest\知乎test'
#     answers = get_all_answers(urls[i])
#     newpath = os.path.join(folder, 'part' + str(i))
#     get_picture(newpath, str(answers))
#
# if __name__=="__main__":
#     pool = Pool(processes=4)
#     start = time.time()
#     #如果想全部下载的话 range(1,int(pagenum)+1)
#     #测试时候参数可以设置成range(1,3)
#     pool.map_async(main, range(4))
#     pool.close()
#     pool.join()
#     stop = time.time()
#     print (stop-start)
#46s

# #使用多进程Process库
# def main(i):
#     urls = ['https://www.zhihu.com/question/28853910','https://www.zhihu.com/question/67553801','https://www.zhihu.com/question/20196263','https://www.zhihu.com/question/25911498']
#     folder='C:\pylearning\\newtest\知乎test'
#     answers = get_all_answers(urls[i])
#     newpath = os.path.join(folder, 'part_' + str(i))
#     get_picture(newpath, str(answers))
#
# if __name__=="__main__":
#     start = time.time()
#     p0 = Process(target=main, args=(0,))
#     p1 = Process(target=main, args=(1,))
#     p2 = Process(target=main, args=(2,))
#     p3 = Process(target=main, args=(3,))
#     p3.start()
#     p2.start()
#     p1.start()
#     p0.start()
#     p0.join()
#     p1.join()
#     p2.join()
#     p3.join()
#     stop = time.time()
#     print (stop-start)
# #43s

# #不使用多进程
# if __name__=="__main__":
#     urls = ['https://www.zhihu.com/question/28853910','https://www.zhihu.com/question/67553801','https://www.zhihu.com/question/20196263','https://www.zhihu.com/question/25911498']
#     folder='C:\pylearning\\newtest\知乎test'
#     i=0
#     a=time.time()
#     while i<len(urls):
#         answers=get_all_answers(urls[i])
#         newpath=os.path.join(folder,'part'+str(i))
#         get_picture(newpath, str(answers))
#         i+=1
#     print(time.time()-a)
# #112s

#只对get_picture使用多进程
# if __name__=="__main__":
#     urls = ['https://www.zhihu.com/question/28853910','https://www.zhihu.com/question/67553801','https://www.zhihu.com/question/20196263','https://www.zhihu.com/question/25911498']
#     folder='C:\pylearning\\newtest\知乎test'
#     i=0
#     a=time.time()
#     ANS=[]
#     PATH=[]
#     while i<len(urls):
#         answers=get_all_answers(urls[i])
#         newpath=os.path.join(folder,'partx'+str(i))
#         ANS.append(str(answers))
#         PATH.append(newpath)
#         i+=1
#     p0 = Process(target=get_picture, args=(PATH[0],ANS[0]))
#     p1 = Process(target=get_picture, args=(PATH[1],ANS[1]))
#     p2 = Process(target=get_picture, args=(PATH[2],ANS[2]))
#     p3 = Process(target=get_picture, args=(PATH[3],ANS[3]))
#     p3.start()
#     p2.start()
#     p1.start()
#     p0.start()
#     p0.join()
#     p1.join()
#     p2.join()
#     p3.join()
#
#     print(time.time()-a)
# #79s
