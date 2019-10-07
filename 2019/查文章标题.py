# coding:utf-8
# File Name：     get_txt_title
# Description :
# Author :       micro
# Date：          2019/9/13
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
    try:
        response = requests.get(i)
        response.encoding = 'gb18030'
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(3)
        print("Was a nice sleep, now let me continue...")
        continue
    print(soup.title)
    f = open('feifantitle.txt', 'a+', encoding="utf-8")
    f.write(soup.title.text)
    f.write("\n")
    f.close()
