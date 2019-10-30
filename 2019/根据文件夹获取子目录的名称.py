# coding:utf-8
# File Name：     111
# Description :
# Author :       micro
# Date：          2019/10/30

import os

file_dir = "C:\\Users\micro\Desktop\新建文件夹\\"
def file_name_listdir(file_dir):
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        print(files)

file_name_listdir(file_dir)