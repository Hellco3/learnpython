'''import requests
#导入requests模块
url = 'http://fanyi.youdao.com/translate'
params = {
    'smartresult':'dict',
    'smartresult':'rule'
}
headers = {'Cookie': 'OUTFOX_SEARCH_USER_ID=-1636576015@113.105.128.71',
'Referer': 'http://fanyi.youdao.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#带参数访问，反反爬虫机制
data = {
    'i':input('翻译：'),
    'client': 'fanyideskweb',
    'salt': '15708035959140',
    'sign': '9f87a351151a7725c1e335e1faf09a82',
    'keyfrom': 'fanyi.web',
}
res = requests.post(url,params = params,headers = headers,data = data)
json_res = res.json()
print(json_res['smartResult']['entries'][1]) '''


import requests
import time
import hashlib
import random
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers={
		'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-1503911544@221.226.82.114; JSESSIONID=abcpz17vgvGZ8aL8KiHUw; OUTFOX_SEARCH_USER_ID_NCOO=1634403883.7994204; ___rl__test__cookies='+str(int(time.time()*1000)),
		#'Host': 'fanyi.youdao.com',
		'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.index',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
		 }
ts=str(int(time.time()*1000))
salt=str(int(ts))+str(random.randint(1,10))
t = input('输入要翻译的句子:')
u = 'fanyideskweb'
l = '@6f#X3=cCuncYssPsuRUE'
src = u + t + salt + l    # u 与 l 是固定字符串，t是你要翻译的字符串，i是之前的时间戳
m2 = hashlib.md5()
m2.update(src.encode('utf-8'))
sign = m2.hexdigest()
data={
	'i':t,
	'from': 'AUTO',
	'to': 'AUTO',
	'smartresult': 'dict',
	'client': 'fanyideskweb',
	'salt': salt,
	'sign': sign,
	'ts': ts,
	'bv': 'e2a78ed30c66e16a857c5b6486a1d326',
	'doctype': 'json',
	'version': '2.1',
	'keyfrom': 'fanyi.web',
	'action': 'FY_BY_CLICKBUTTION'
	}
#print('ts='+ts)
#print('salt='+salt)
#print('sign='+sign)
content=requests.post(url,headers=headers,data=data)
#print(content.json())
tgt=content.json()['translateResult'][0][0]['tgt']
print(tgt)