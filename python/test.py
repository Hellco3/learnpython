import requests
import bs4
import MyQR


url = 'https://baike.baidu.com/item/%E5%B1%B1%E4%B8%9C%E7%9C%81%E7%9C%81%E7%BA%A7%E9%9D%9E%E7%89%A9%E8%B4%A8%E6%96%87%E5%8C%96%E9%81%97%E4%BA%A7%E5%90%8D%E5%BD%95/4206008?fr=aladdin'
reponse = requests.get(url,allow_redirects=False)
bs_list = bs4.BeautifulSoup(reponse.text,'html.parser')
print(bs_list)
list = bs_list.find(class_='table-responsive')
all_list = list.find_all(class_='para')
n = 0
for item in all_list:
    n =+ 1
    if n % 2 == 0 :
        name = item.text
    else:
        locals = item.text
    print(name)
    print(locals)