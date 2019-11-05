#本地Chrome 浏览器设置方法
from selenium import webdriver #selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() 
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

label = driver.find_elements_by_tag_name('label')#根据标签名提取所有元素

print(label.text)
driver.close()
'''driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)#等待2秒

labels = driver.find_elements_by_tag_name('label')#根据标签名提取所有元素
print(type(labels))
print(labels)
driver.close()'''