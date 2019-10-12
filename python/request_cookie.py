import requests
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
data = {
    'log':'spiderman',
    'pwd':'crawler334566',
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie':'1',
    }
login_in = requests.post(url,headers=headers,data=data)
print(login_in)
