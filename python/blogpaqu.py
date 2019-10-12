from bs4 import BeautifulSoup
import requests

url = 'https://spidermen.cn/'
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
lists = bs.find_all('header',class_='entry-header')
for item in lists:
    publish_time = item.find('time',class_ = 'entry-date published')
    title = item.find(class_ = 'entry-title')
    URL = title.find('a')
    print(publish_time.text,'\n',title.text,'\n',URL['href'],'\n')
