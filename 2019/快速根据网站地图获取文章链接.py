# coding:utf-8
# File Name：     快速根据网站地图获取文章链接
# Description :
# Author :       micro
# Date：          2019/10/21
# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.szffmr.com/sitemap/article/article-15.xml'
r = requests.get(url)
r.encoding = 'gb2312'
soup = BeautifulSoup(r.text, 'lxml')
links = []
for a in soup.find_all('a'):
    link = a['href']
    links.append(link)

print(links)
zhuanti = []
for i in links:
    if str(i).startswith("zhuanti/"):
        zhuanti.append(i)
print(zhuanti)
