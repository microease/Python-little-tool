# coding:utf-8
# File Name：     深圳美莱爬虫
# Description :
# Author :       micro
# Date：          2019/10/11
from bs4 import BeautifulSoup
import requests
demo = requests.get("http://www.baidu.com")
soup = BeautifulSoup(demo, "html.parser")
print(soup.a[0].attrs)