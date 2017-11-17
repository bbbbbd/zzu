# -*- coding:utf8 -*-
import requests
import re

indes_url = 'https://passport.csdn.net/account/login'
login_url = 'https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn'
s = requests.Session()
def getInfo(html):
    pattern1 = re.compile('name="lt" value="(.*?)"')
    pattern2 = re.compile('name="execution" value="(.*?)"')
    lt= re.findall(pattern1, html)
    execution = re.findall(pattern2, html)
    return lt[0],execution[0]
page = s.get(indes_url)
lt, execution = getInfo(page.text)
postdata = {
    'username':'******',
    'password':'******',
    'rememberMe':'true',
    'lt':lt,
    'execution':execution,
    '_eventId':'submit'
}
response = s.post(login_url, data=postdata)
print response.status_code
