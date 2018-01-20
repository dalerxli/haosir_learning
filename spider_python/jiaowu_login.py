import requests
import re
import time
import json
import numpy as np
import pandas as pd
from bs4 import  BeautifulSoup
import csv
def get_postinf():
    # 获取xsrf code
    response = session.get('http://idas.uestc.edu.cn/authserver/login', headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    a= soup.find('input', {'name':"lt"}).attrs['value']
    b= soup.find('input', {'name':"dllt"}).attrs['value']
    c = soup.find('input', {'name':"execution"}).attrs['value']
    d = soup.find('input', {'name':"_eventId"}).attrs['value']
    e = soup.find('input', {'name':"rmShown"}).attrs['value']
    return(a,b,c,d,e)
def jiaowu_login(account, password):
        post_url = 'http://idas.uestc.edu.cn/authserver/login'
        post_data = {
            'username': account,
            'password': password,
            'lt': pa,
            'dllt': pb,
            'execution': pc,
            '_eventId': pd,
            'rmShown': pe,
        }
        para={
            'username': account,
            '_':str(time.time() * 1000)
        }
        base_url='http://idas.uestc.edu.cn/authserver/needCaptcha.html'
        session.get(base_url,params=para)
        response_text = session.post(post_url, data=post_data, headers=header)
def grade_get():
    response = session.get('http://eams.uestc.edu.cn/eams/teach/grade/course/person!search.action?semesterId=163&projectType=1')
    soup = BeautifulSoup(response.text, 'lxml')
    biaotis = soup.find('tr').find_all('th')
    columns=[]
    column=[]
    for biaoti in biaotis:
        column.append(biaoti.string)
    columns.append(column)
    datas=soup.find("tbody").find_all("tr")
    for data in datas:
        row=[]
        singles=data.find_all("td")
        for single in singles:
            row.append(single.get_text())
        columns.append(row)
    csvFile = open("mygrade.csv", "w")
    writer = csv.writer(csvFile)
    # 写入的内容都是以列表的形式传入函数
    for col in columns:
        writer.writerow(col)
    csvFile.close()
    print("快去查看你的成绩吧")
if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
    header = {
        'Host': 'idas.uestc.edu.cn',
        'Referer': 'http://idas.uestc.edu.cn/authserver/login',
        'User-agent': agent,
    }
    session = requests.session()
    pa, pb, pc, pd, pe = get_postinf()
    name=input("你的学号")
    password=input("你的密码")
    jiaowu_login(name,password)
    grade_get()