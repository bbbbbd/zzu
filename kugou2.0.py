# -*- coding:utf8 -*-
import sys
import requests
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )


#搜索获取歌曲列表
def get_music_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        return parse_music_info(response.text)
    return None

#解析歌曲列表获得重要字段
def parse_music_info(html):
    try:
        result = json.loads(html)
        for item in result['data']['lists']:
            yield [item['FileName'], item['AlbumID'], item['AlbumName'], item['Duration'], item['FileHash']]
    except Exception:
        yield None

#跳转到每个歌曲的播放页面
def get_play_url(hash_id,album_id):
    url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash='+hash_id+'&album_id='+album_id
    response = requests.get(url)
    if response.status_code == 200:
        return parse_play_url(response.text)
    return None

#解析歌曲的播放地址
def parse_play_url(json_text):
    json_dict = json.loads(json_text)
    if json_dict:
        return json_dict['data']['play_url'].replace('\\','')
    return  None

#程序入口
def main(keyword):
    url = 'http://songsearch.kugou.com/song_search_v2?keyword='+keyword+'&page=1&pagesize=480&platform=WebFilter&iscorrection=1'
    for item in get_music_info(url):
        try:
            play_url = get_play_url(item[4],item[1])
            second = int(item[3])%60
            second = str(second) if second > 10 else '0'+str(second)
            print '歌名：'+str(item[0]),'专辑：'+ str(item[2]),'时长：'+str(int(item[3])/60)+':'+second,play_url
        except Exception:
            print '出错啦'


if __name__ == '__main__':
    main('陈奕迅')