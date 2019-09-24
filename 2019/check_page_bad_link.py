# coding:utf-8
# File Name：     check_page_bad_link
# Description :
# Author :       micro
# Date：          2019/9/24
# 检查页面中的死链接
import requests
import re
from bs4 import BeautifulSoup
from retrying import retry


@retry
def run():
    # 第一步，根据给的页面链接，查出页面中所有的链接。
    url = 'http://www.szffmr.com/map.html'
    r = requests.get(url)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, 'lxml')
    links = []
    for a in soup.find_all('a'):
        link = a['href']
        links.append(link)
    links = list(set(links))
    print(links)
    print("共检查出" + str(len(links)) + "个链接")
    # 第二部，for循环遍历链接列表，查出http标头为404的链接
    for link1 in links:
        r1 = requests.get(link1)
        f = open('feifanlinks.txt', 'a+', encoding="utf-8")
        f.write(link1 + " " + str(r1.status_code))
        f.write("\n")
        f.close()


if __name__ == '__main__':
    run()
