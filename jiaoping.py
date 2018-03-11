# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import gevent
from gevent import monkey;monkey.patch_all()


def post_save(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        post_url = soup.find('form')['action']
        result = soup.find_all('select')
        data = {}
        for item in result:
            data[item['name']] = item.find(attrs={'selected': ''}).string
        rep = requests.post(post_url, data)
        if rep.status_code == 200:
            print '教评完成'
    except:
        print '已经教评'


url = 'http://jw.zzu.edu.cn/scripts/jpxx/jpxxcgi.exe/check'
data = {
    'zhanghao':'201577f0132',
    'mima':'172655790',
    'shenfen':'stu'
}
response = requests.post(url, data=data)
soup =BeautifulSoup(response.text, 'lxml')
able = soup.find(color='green')
if able:
    href = able.parent.attrs['href']
    response = requests.get(href)
    soup = BeautifulSoup(response.text, 'lxml')
    result = soup.find_all(attrs={'width':'30%'})[2:]
    if result:
        tasks = []
        for item in result:
            a = item.find('a')['href']
            tasks.append(gevent.spawn(post_save, a))
        gevent.joinall(tasks)
else:
    print '教评暂未开放'

