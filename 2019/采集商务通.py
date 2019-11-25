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
    file_root = r"C:\Users\micro\Desktop\新建文件夹"
    files = glob.glob(os.path.join(file_root, "*.htm"))
    return files


def change_html(files):
    for i in files:
        htmlfile = open(i, 'r', encoding='utf-8')
        htmlhandle = htmlfile.read()
        soup = BeautifulSoup(htmlhandle, 'lxml')
        trs = soup.find_all("tr", style="display:none")
        for j in trs:
            return j


def save_txt(j):
    file_root = r"C:\Users\micro\Desktop\新建文件夹2\\"
    for i in range(100):
        print(file_root+str(i)+".txt")
        fd = open(file_root+str(i)+".txt", mode="w", encoding="utf-8")

def run():
    files = get_all_html()
    j = change_html(files)
    save_txt(j)


if __name__ == '__main__':
    run()
