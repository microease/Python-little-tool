# coding:utf-8
# File Name：     get_all_article
# Description :
# Author :       micro
# Date：          2019/9/13
# 程序通过索引页面获取所有的文章链接。并获取文章链接对应的标题保存成为excel
import requests


def run():
    # 1 获取所有索引页面的链接
    index_list = get_index()
    # 2 根据文章链接的样式从索引页面获取所有的文章页面链接，并去重。
    get_article(index_list)
    # 3 根据文章页面的链接 获取文章链接的标题，并一一对应
    # 4 保存成为excel 格式为 标题,链接


def get_index():
    index_list = []
    for i in range(952 + 1):
        url = "http://www.szffmr.com/map.asp?page="
        url += str(i)
        index_list.append(url)
    print(index_list)
    return index_list


def get_article(index_list):
    for i in index_list:
        response = requests.get(i)
        print(response.content)


if __name__ == '__main__':
    run()
