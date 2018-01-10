# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def post_save(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        post_url = soup.find('form')['action']
        result = soup.find_all('select')
        data = {}
        for item in result:
            data[item['name']] = item.find(attrs={'selected': ''}).string
        rep = requests.post(post_url, data)
        rep.encoding = 'gbk'
        if rep.status_code == 200:
            print '教评完成'
    except:
        print '已经教评'


url = 'http://jw.zzu.edu.cn/scripts/jpxx/jpxxcgi.exe/check'
data = {
    'zhanghao':'*********',
    'mima':'*********',
    'shenfen':'stu'
}
response = requests.post(url, data=data)
response.encoding = 'gbk'
soup =BeautifulSoup(response.text, 'lxml')
able = soup.find(color='green')
if able:
    href = able.parent.attrs['href']
    response = requests.get(href)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'lxml')
    result = soup.find_all(attrs={'width':'30%'})[2:]
    if result:
        for item in result:
            a = item.find('a')['href']
            post_save(a)
else:
    print '教评暂未开放'




