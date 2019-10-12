from bs4 import BeautifulSoup

bs = BeautifulSoup('<p><a>惟有痴情难学佛</a>独无媚骨不如人</p>','html.parser')
tag = bs.find('p')
print(tag.text)