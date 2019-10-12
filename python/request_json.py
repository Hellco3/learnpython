import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

params={'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
'offset':'10',
'limit':'10',
'sort_by':'voteups'}
res = requests.get(url,headers = headers,params = params)
print(res.status_code)

articles = res.json()
data = articles['data']
for i in data:
    print(i['title'])
    print(i['url'])
    print(i['excerpt'],'\n')