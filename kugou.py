# -*- coding:utf8 -*-
import sys
import requests
import re
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )


def get_music_info(url):
    response = requests.get(url)
    return parse_music_info(response.text)

def parse_music_info(html):
    pattern = re.compile('{"SongName":.*?}.*?}')
    result = re.findall(pattern, html)
    for item in result:
        item = json.loads(item )
        yield [item['FileName'],item['AlbumID'],item['AlbumName'],item['Duration'],item['FileHash']]

def get_play_url(hash_id,album_id):
    url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash='+hash_id+'&album_id='+album_id+'&_=1505738969338'
    response = requests.get(url)
    return parse_play_url(response.text)

def parse_play_url(html):
    pattern = re.compile('"play_url":"(.*?)"')
    result = re.findall(pattern, html)
    if result:
        return result[0].replace('\\','')

def main(keyword):
    url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery112405213552049562944_1505739248953&keyword='+keyword+'&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter'
    # html = get_music_info(url)
    for item in get_music_info(url):
        play_url = get_play_url(item[4],item[1])
        second = int(item[3])%60
        second = str(second) if second > 10 else '0'+str(second)
        print '歌名：'+str(item[0]),'专辑：'+ str(item[2]),'时长：'+str(int(item[3])/60)+':'+second,play_url

if __name__ == '__main__':
    main('梦然')
