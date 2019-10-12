import requests
#引入requests
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
data = {
    'log':'spiderman',
    'pwd':'crawler334566',
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie':'1',
    }
#把有关登录的参数封装成字典，赋值给data
login_in = requests.post(url,headers = headers,data = data)
#用request.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in
cookie = login_in.cookies
#提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
#我们想要评论的文章网址。
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
data_1 = {
    'comment': input('请输入评论'),
    'submit':'发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
comment = requests.post(url_1,headers = headers,data = data_1,cookies = cookie)
#用request.post发起发表评论的请求，放入参数;文章网址、headers、评论参数、cookies，赋值给comment。
#调用cookies的方法就是在post请求中传入cookies=cookies的参数
print(comment.status_code)
