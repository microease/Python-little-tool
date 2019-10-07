# coding:utf-8
# File Name：     get_all_article
# Description :
# Author :       micro
# Date：          2019/9/13
# 程序通过索引页面获取所有的文章链接。并获取文章链接对应的标题保存成为excel
import requests
from bs4 import BeautifulSoup
from lxml import *
import re


def run():
    # 1 获取所有索引页面的链接
    index_list = get_index()
    # 2 根据文章链接的样式从索引页面获取所有的文章页面链接，并去重。
    article_list = get_article(index_list)
    # 3 根据文章页面的链接 获取文章链接的标题和发布时间，并一一对应
    get_title_and_time(article_list)
    # 4 保存成为excel 格式为 标题,链接


def get_index():
    index_list = []
    for i in range(2 + 1):
        url = "http://www.szffmr.com/map.asp?page="
        url += str(i)
        index_list.append(url)
    print(index_list)
    return index_list


def get_article(index_list):
    article_list = []
    for i in index_list:
        response = requests.get(i)
        soup = BeautifulSoup(response.text, 'lxml')
        for a in soup.find_all('a'):
            link = a['href']
            if link.endswith(".html"):
                article_list.append(link)
    # 去重
    article_list = list(set(article_list))
    print(article_list)
    return article_list


def get_title_and_time(article_list):
    # title_list = []
    # for i in article_list:
    #     response = requests.get(i)
    #     response.encoding = 'gb18030'
    #     soup = BeautifulSoup(response.text, 'lxml')
    #     title_list.append(soup.title.text)
    # print(title_list)
    time_list = []
    for i in article_list:
        response = requests.get(i)
        response.encoding = 'gb18030'
        soup = BeautifulSoup(response.text, 'lxml')
        temp = None
        if (soup.find('div', class_='title')):
            temp = soup.find('div', class_='title').p.text
            temp = temp.split("：")[2]
            print(temp.split("　")[0])
if __name__ == '__main__':
    run()
