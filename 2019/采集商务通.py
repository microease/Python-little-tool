# coding:utf-8
# File Name：     采集商务通
# Description :
# Author :       micro
# Date：          2019/11/25
# 采集从商务通导出的html聊天记录并转换成txt
# 第一步，读取文件夹内的所有html
# 第二步，遍历html，采用多线程技术读取html，提取每个html中的聊天记录
# 第三步，分别保存为txt，txt命名采用0000000001-9999999999.txt这样命名
import glob, os
from bs4 import BeautifulSoup
import requests


def get_all_html():
    file_root = r"D:\OneDrive - Merced College\南方商务通聊天记录\20190101-20200101用户排序一般\\"
    files = glob.glob(os.path.join(file_root, "*.htm"))
    return files


def change_html(files):
    count = 1
    for i in files:
        htmlfile = open(i, 'r', encoding='utf-8')
        htmlhandle = htmlfile.read()
        soup = BeautifulSoup(htmlhandle, 'lxml')
        trs = soup.find_all("tr", style="display:none")
        for tr in trs:
            file_root = r"D:\南方商务通聊天记录已处理\20190101-20200101用户排序一般\\"
            print(file_root + str(count) + ".htm")
            f = open(file_root + str(count) + ".htm", mode="w", encoding="utf-8")
            f.write(str(tr))
            f.close()
            count += 1



def run():
    files = get_all_html()
    tr = change_html(files)


if __name__ == '__main__':
    run()
