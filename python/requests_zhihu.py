import requests
import csv

csvfile = open('articles.csv','a',newline='',encoding='utf-8-sig')
writer = csv.writer(csvfile,dialect='excel')
list2 = ['标题','链接','摘要']
writer.writerow(list2)

url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
offset = 0
list_all= []

while True:


    params = {
    'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset':str(offset),
    'limit':'10',
    'sort_by':'voteups'
    }
    
    res = requests.get(url,headers = headers,params = params)
    js = res.json()
    offset = offset + 20
    data = js['data']
    for i in data:
        list_all.append([i['title'],i['url'],i['excerpt']])
    if offset > 40:
        break
for i in list_all:
    writer.writerow([i[0],i[1],i[2]])
    print('标题：'+i[0]+'\n'+'链接：'+i[1]+'\n'+'摘要：'+i[2])
    print('-------------------------------------','\n')
csvfile.close()

print('okay')