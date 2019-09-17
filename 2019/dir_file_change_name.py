# coding:utf-8
# File Name：     dir_file_change_name
# Description :遍历文件夹修改文件名
# Author :       micro
# Date：          2019/9/17
import glob, os

path = r'C:\Users\micro\Desktop\2018流量'
files = glob.glob(os.path.join(path, "*.csv"))
for i in files:
    newname = i.replace(r'(.*?至))', '')
    os.rename(os.path.join(i),os.path.join(newname))
    print('success : ' + newname)
