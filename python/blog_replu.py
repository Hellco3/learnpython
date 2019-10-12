import requests

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
#'Origin':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#'Referer':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
data = {
'log':'spiderman',
'pwd':'crawler334566',
'wp-submit':'登录',
'redirect_to':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
'testcookie':'1'
}
login_in = requests.post(url,headers = headers,data= data)
cookie = login_in.cookies

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
headers_1 = {
#'Origin':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#'Referer':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
data_1 = {
'comment':input('请输入评论：'),
'submit':'发表评论',
'comment_post_ID':'23',
'comment_parent':'0'
}
comment = requests.post(url_1,headers=headers_1,data = data_1,cookies = cookie)
print(comment.status_code)