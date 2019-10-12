import requests,json

session = requests.session()
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
'log': input('请输入你的账号:'),
'pwd': input('请输入你的密码:'),
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
'testcookie': '1'
}
session.post(url,headers = headers,data = data)

cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
cookies_str = json.dumps(cookie_dict)

with open ('cookies.txt','w',encoding = 'utf-8') as f:
    f.write(cookies_str)

print('succeed')