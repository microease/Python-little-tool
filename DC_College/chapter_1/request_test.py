# coding:utf-8
# File Name：     request_test
# Description :
# Author :       micro
# Date：          2019/12/20
import requests
r = requests.get("https://www.baidu.com/")
r.encoding = "utf-8"
print(r.text)