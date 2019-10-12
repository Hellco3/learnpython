import requests
from bs4 import BeautifulSoup
import csv

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=56643768213273912&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6'
res_music = requests.get(url)

json_music = res_music.json()
#print(json_music)
songs = json_music['data']['song']['list']
titles = []
album_names = []
song_URLs = []
for number in range(20):
    for song in songs:
        title = song['name']
        album_name = song['album']['name']
        song_URL = 'https://y.qq.com/n/yqq/song/'+song['mid']+'.html\n\n'
        titles.append(title)
        album_names.append(album_name)
        song_URLs.append(song_URL)
with open('assets.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header=['歌曲名','所属专辑','播放链接']
    writer.writerow(header)
for n in range(20):
    name = titles[n]
    album_name = album_names[n]
    song_URL = song_URLs[n]
    with open('songs_collection.csv','a',newline='')as csvfile:
        writer = csv.writer(csvfile,dialect = 'excel')
        writer.writerow([name,akbum_name,song_URL])

    print('歌曲名:',name,'\n','所属专辑：',album_name,'\n','播放链接：',song_URL,'\n')