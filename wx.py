import requests
import json
import time
from Crypto.Cipher import AES
import base64

r = {"score":275,"times":245,"game_data":"{\"seed\":1514966477825,\"action\":[[0.714,1.29,false],[0.764,1.19,false],[0.781,1.16,false],[0.602,1.53,false],[0.777,1.19,false],[0.492,1.77,false],[0.683,1.36,false],[0.366,2,false],[0.635,1.46,false],[0.648,1.43,false],[0.583,1.56,false],[0.715,1.29,false],[0.652,1.43,false],[0.615,1.5,false],[0.697,1.36,false],[0.563,1.63,false],[0.433,1.87,false],[0.433,1.87,false],[0.86,1.06,false],[0.616,1.53,false],[0.558,1.63,false],[0.9,0.95,false],[0.633,1.5,false],[0.517,1.7,false],[0.762,1.19,false],[0.459,1.84,false],[0.899,0.99,false],[0.5,1.73,false],[0.621,1.5,false],[0.396,1.94,false],[0.599,1.56,false],[0.665,1.43,false],[0.339,2.07,false],[0.361,2,false],[0.551,1.63,false],[0.683,1.39,false],[0.735,1.33,false],[0.618,1.5,false],[0.836,1.06,false],[0.747,1.26,false],[0.651,1.43,false],[0.761,1.19,false],[0.564,1.6,false],[0.418,1.9,false],[0.542,1.63,false],[0.282,2.17,true],[0.71,1.36,false],[0.71,1.36,false],[0.383,2,false],[0.766,1.26,false],[0.524,1.7,false],[0.864,1.06,false],[0.534,1.67,false],[0.307,2.14,true],[0.567,1.6,false],[0.781,1.19,false],[0.466,1.84,false],[0.684,1.36,false],[0.723,1.33,false],[0.47,1.8,true],[0.542,1.67,false],[0.436,1.87,true],[0.719,1.33,true]],\"musicList\":[false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false],\"touchList\":[[178,472],[385,293],[200,312],[35,403],[425,167],[264,141],[233,372],[489,470],[122,111],[242,303],[133,369],[95,122],[305,280],[245,189],[268,165],[344,315],[464,184],[26,442],[214,171],[388,218],[285,428],[385,165],[241,51],[161,109],[259,168],[2,135],[477,186],[190,115],[303,403],[81,236],[453,45],[371,45],[292,233],[385,24],[398,94],[242,93],[35,195],[173,45],[240,432],[275,315],[201.3,200.6],[333.2,111],[166.5,503],[159.5,508.5],[143.5,505.5],[149.5,505.5],[143.5,498],[143,497.5],[142,498.5],[138,493],[135.5,491.5],[130,493],[130.5,495],[127,492.5],[127,491.5],[127,488.5],[133.5,499.5],[136,493.5],[131.5,496],[129,497.5],[118.5,497],[123.5,495],[110.5,497]],\"version\":1}"}

action_data = {
    "times": 0,
    "game_data": json.dumps(r)
}

session_id = ''

aes_key = session_id[0:16]
aes_iv  = aes_key

cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)

str_action_data = json.dumps(action_data)
print "json_str_action_data ", str_action_data

#Pkcs7
length = 16 - (len(str_action_data) % 16)
str_action_data += chr(length)*length

cipher_action_data = base64.b64encode(cryptor.encrypt(str_action_data))
print "action_data ", cipher_action_data

post_data = {
  "base_req": {
    "session_id": session_id,
    "fast": 1,
  },
  "action_data": cipher_action_data
}

headers = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx7c8d593b2c3a7703/5/page-frame.html",
    "content-type": "application/json",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
    "Content-Length": "0",
    "Host": "mp.weixin.qq.com",
    "Connection": "Keep-Alive"
}

url = "https://mp.weixin.qq.com/wxagame/wxagame_settlement"


response = requests.post(url, json=post_data, headers=headers, verify=False)
print json.loads(response.text)
