# -*- coding:UTF-8 -*-
import requests
from requests import sessions
from bs4 import BeautifulSoup
import os
import re
from urllib.request import urlretrieve
import time
def init(url):
    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
    s = requests.Session()
    s.headers.update(header)
    s.headers.update({"authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20"})
    ret=s.get(url)
    return s
def get_answer(s,qid,limit,offset):
    params={
        'sort_by':'default',
        'include':'data[*].is_normal,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].author.follower_count,badge[?(type=best_answerer)].topics',
        'limit':limit,
        'offset':offset
    }
    url ="https://www.zhihu.com/api/v4/questions/"+qid+"/answers"
    return s.get(url,params=params,timeout=10)
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
    return(answers,session)
def load_url(i,ans):
    jpg = re.compile(r'https://[^\s]*?_hd\.jpg')
    words = re.findall(jpg, ans)
    img = list(set(words))
    lenth = len(img)
    with open(str(i)+'.txt','w',encoding='utf-8') as f:
        for j in range(lenth):
            f.write(img[j])
            f.write('\n')
def get_picture(folder,ans,session):
    if not os.path.exists(folder):
        os.makedirs(folder)
    print("start")
    jpg = re.compile(r'https://[^\s]*?_hd\.jpg')
    words = re.findall(jpg,ans)
    img=list(set(words))
    lenth=len(img)
    #防止假死可采用try except结构
    for i  in range(lenth):
        try:
            # 设置超时重试次数及超时时间单位秒
            response = session.get(img[i], timeout=20)
            contents = response.content
            with open(folder+"\\"+"image"+str(i)+'.jpg', "wb") as pic:
                pic.write(contents)
            time.sleep(0.2)

        except ConnectionError:
            print ('连接超时,URLgg: ', img[i])
        except IOError:
            print('Io errorgg'+folder+'\\'+'image' + str(i) + ".jpg")

        time.sleep(0.3)
        print(i)
    print('over')
if __name__=="__main__":
    urls = ['https://www.zhihu.com/question/36783201','https://www.zhihu.com/question/28202126','https://www.zhihu.com/question/29134042','https://www.zhihu.com/question/60080785']
    folder='C:\pylearning\\newstart\假死测试'
    i=0
    while i<len(urls):
        answers,session=get_all_answers(urls[i])
        newpath=os.path.join(folder,'part'+str(i))
        get_picture(newpath, str(answers),session)
        i+=1
