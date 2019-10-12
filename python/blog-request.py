import requests

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res = requests.get(url)
html = res.text
print('响应状态码：', res.status_code)
print(html)
with open('html.txt','w',encoding='utf-8') as f:
    f.write(html)
