# coding:utf-8
# File Name：     urllib_test
# Description :
# Author :       micro
# Date：          2019/12/20
import urllib.request
f = urllib.request.urlopen("http://www.baidu.com/")
print(f.read(500).decode("utf-8"))