# coding:utf-8
# File Name：     book_douban_comments_test
# Description :
# Author :       micro
# Date：          2019/12/20
import requests
from bs4 import BeautifulSoup
import pandas
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
r = requests.get("https://book.douban.com/subject/1084336/comments/", headers=headers).text
soup = BeautifulSoup(r, 'lxml')
pattern = soup.find_all('span','short')
comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv("comments.csv")
