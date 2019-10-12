import urllib.request
import time

time.sleep(2)
url = input('请输入网址')
file = urllib.request.urlopen (url)
print( '获取当前url:',file.geturl() )
print('file.getcode,HTTPResponse类型:', file.getcode )
print('file.info,返回当前环境相关的信息：',file.info() )
