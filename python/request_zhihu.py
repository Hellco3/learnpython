import requests
from bs4 import BeautifulSoup

url='https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes?page=1'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
res = requests.get(url,headers = headers)
print(res.status_code)
'''url='https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes?page=1'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#使用headers是一种默认的习惯，默认你已经掌握啦~
res=requests.get(url,headers=headers)
#用resquest模块发起请求，将响应的结果赋值给变量res。
print(res.status_code)
#检查状态码''' 

bs = BeautifulSoup(res.text,'html.parser') 
content = bs.find_all(class_='ContentItem-title')
print(res.text) 