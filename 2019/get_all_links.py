# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.szffmr.com/zhuanti/2019summer/'
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
    if str(i).startswith("http://www.szffmr.com/zhuanti/"):
        zhuanti.append(i)
print(zhuanti)
