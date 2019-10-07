# coding:utf-8
# File Name：     get_txt_time
# Description :
# Author :       micro
# Date：          2019/9/14
import sys
import time
import requests
from bs4 import BeautifulSoup
from lxml import *
import re

result = []
with open('feifanlink.txt', 'r') as f:
    for line in f:
        result.append(line.split("\n")[0])
print(result)

title_list = []
for i in result:
    response = requests.get(i)
    response.encoding = 'gb18030'
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup.find('div','date').text)
    f = open('feifantime.txt', 'a+', encoding="utf-8")
    f.write(soup.find('div','date').text)
    f.write("\n")
    f.close()
