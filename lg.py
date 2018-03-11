# -*-coding:utf-8 -*-
import json
import re
import requests
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost',27017)
db=client.lagouwang
collection=db.jobs
headers = {
    'Host':'www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_Java?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
r = requests.get('https://www.lagou.com/')
soup = BeautifulSoup(r.text, 'lxml')
menu_sub = soup.find_all(class_='menu_sub dn')
name = []
for menu in menu_sub:
    jobs = menu.find_all('a')
    name += [name.string for name in jobs]

def parse(html):
    result = json.loads(html)
    s = result['content']['positionResult']['result']
    if s:
        for i in s:
            try:
                # collection.insert(i)
                pass
            except:
                print 'Failed'
        return False
    return True

def get_html(data):
    try:
        r = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0',
                          data=data, headers=headers)
        pattern = re.compile(u'您操作太频繁')
        often = re.search(pattern, r.text)
        if often:
            time.sleep(30)
            return get_html(data)
        return r.text
    except:
        time.sleep(120)
        return get_html(data)

for i in name:
    print i,
    data = {
        'kd': i,
        'first':'true',
        'pn':'1'
    }
    html = get_html(data)
    isEmpty = parse(html)
    if isEmpty:
        print ':Null',
    else:
        print ':1',
        for j in range(2,31):
            data = {
                'kd': i,
                'first': 'false',
                'pn': j
            }
            html = get_html(data)
            isEmpty = parse(html)
            if isEmpty:
                break
            else:
                print j,
    print

