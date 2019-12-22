# coding:utf-8
# File Name：     03-handler_openner
# Description :
# Author :       micro
# Date：          2019/12/22
import urllib.request

url = "http://www.baidu.com"
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(url)
data = response.read()
print(data)
