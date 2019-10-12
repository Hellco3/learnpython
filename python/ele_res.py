import requests,csv,openpyxl,base64
from PIL import Image
# 注意：此处需要先模拟发送验证码的请求，再模拟登录的请求。
# 请求验证码时，会返回一个json，json里会有validate_token。它在输入账号验证码模拟登录的时候，会用到。
s = requests.session()
mobile_phone = input('请输入你的手机号码:')
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
data = {'captcha_hash': '',
	    'captcha_value': '',
	    'mobile': mobile_phone,
	    'scf': 'ms'
	    }
login_in = s.post(url,headers = headers,data = data)
res_code = login_in.status_code
print('status code of login: ' + str(res_code))
if res_code == 200:
    token = login_in.json()['validate_token']
    code = input('输入手机验证码')
    url_login = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    data_1 = {
    'mobile': mobile_phone,
    'scf': "ms",
    'validate_code': code,
    'validate_token': token
    }

    s.post(url_login,headers = headers,data = data_1)
elif res_code == 400:
    print('有图片验证码')
    url = 'https://h5.ele.me/restapi/eus/v3/captchas'
    data2 = {'captcha_str': mobile_phone}
	# 提取验证码。
    cap = s.post(url, headers=headers, data=data2)
    strCap = cap.json()['captcha_image'].replace('data:image/jpeg;base64,', '')
    #print(cap.json())
    hash1 = cap.json()['captcha_hash']
	# 验证码字符串转图形文件保存到本地
    x = base64.b64decode(strCap)
    file = open('captcha.jpg', "wb")
    file.write(x)
    file.close()
    im = Image.open('captcha.jpg')
    im.show()#展示验证码图形
    captcha_value = input('输入验证码:')
    url_code = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
    data_code = {
        'captcha_hash': hash1,
        'captcha_value': captcha_value,
        'mobile': mobile_phone,
        'scf': "ms"
        }
    login = s.post(url = url_code,headers= headers,data = data_code)
    token = login.json()['validate_token']
    url_login = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    data2 = {
            'mobile': mobile_phone,
            'scf': "ms",
            'validate_code': input('请输入手机验证码：'),
            'validate_token': token
            }
    verify = s.post(url = url_login,headers = headers,data = data2 )
    print('status_code:'+str(verify.status_code))#打印返回值
url_res = 'https://www.ele.me/restapi/shopping/restaurants'
params = {
'extras[]':'activities',
'geohash':'wtw363yg4yqt',
'latitude':'31.167389',
'limit':'24',
'longitude':'121.397336',
'offset':'0',
'terminal':'web'}
res = s.get(url = url_res,params = params,headers = headers)
json_data = res.json()
print(json_data)
lists = {}
for f in json_data:
    name = f['name']
    info = f['promotion_info']
    lists[name] = info
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'new title'
sheet['A1'] = '饿了么'
header = ['店铺名称','介绍']
sheet.append(header)
for key,value in lists.items():
    sheet.append([key,value])
wb.save('restaurants.xlsx')
print('收集完毕')