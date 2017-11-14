# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import time
from PIL import Image

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
url = 'https://www.zhihu.com'
post_url = 'https://www.zhihu.com/login/phone_num'
agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
respose = urllib2.urlopen(url)

#获取验证码并存储
def saveImg():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login&lang=cn"
    captcha = urllib2.urlopen(captcha_url)
    data =captcha.read()
    with open('captcha.gif', 'wb') as f:
        f.write(data)
    img = Image.open('captcha.gif')
    img.show()

#获取验证码中倒立文字的位置
def getPoint(n):
    switch = {'1':'20.375,22','2':'45.375,23','3':'70.375,21','4':'95.375,20','5':'120.375,18','6':'145.375,22','7':'170.375,22'}
    return switch[n]

saveImg()
num = raw_input('请输入验证码的个数：')
if int(num)==1:
    first = raw_input('请输入第一个验证码的位置：')
    l = '['+getPoint(first)+']'
else:
    first = raw_input('请输入第一个倒立文字的位置：')
    second = raw_input('请输入第二个倒立文字的位置：')
    l = '['+getPoint(first)+'],['+getPoint(second)+']'
#获取_xsrf
for item in cookie:
    if item.name == '_xsrf':
        _xsrf = item.value
headers = {
	'User-Agent':agent,
    'Referer':'https://www.zhihu.com/',
    'X-Xsrftoken':_xsrf
}
postdata = {
	'_xsrf': _xsrf,
	'password': '******',
    'captcha': '{"img_size":[200,44],"input_points":['+l+']}',
	'captcha_type': 'cn',
	'phone_num': '******'
}
data = urllib.urlencode(postdata)
request = urllib2.Request(post_url, data, headers)
result = urllib2.urlopen(request)
print result.read()
