import requests
def res_cookies(log,password):
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    data = {
        'log': log,
        'pwd': password,
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie':'1'

    }
    res = requests.post(url,headers = headers,data = data)
    cookies = res.cookies
    with open ('cookies_test.txt','w',encoding = 'utf-8') as f:
        f.write(str(cookies))
    print('okay')
#提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。
def cookies_get():
    with open ('cookies_test.txt','r',encoding = 'utf-8') as f:
        cookies = f.read()
    return cookies
log = 'spiderman'
password = 'crawler334566'
res_cookies(log,password)   
cookies = cookies_get()
print(cookies)
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data = {
    'comment': input('请输入评论内容：'),
    'submit': '发表评论',
    'comment_post_ID':'23',
    'comment_parent': '0'
}
print('评论成功')