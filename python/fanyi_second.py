import requests
#导入requests模块
url = 'http://fanyi.youdao.com/translate'
headers = {'Referer': 'http://fanyi.youdao.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
data = {
    #i = input('输入想要翻译的词')
    'i': '集合',
    'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '15711100746743',
'sign': '502d954cae836c4155b277a243454990',
'ts': '1571110074674',
'bv': 'ca3dedaa9d15daa003dbdaaa991540d1',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTlME'
}
res = requests.post(url,headers = headers,data = data)
js = res.json()
output = js['smartResult']['entries'][1]
print(res.status_code)
print(output)