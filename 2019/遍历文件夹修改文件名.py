# coding:utf-8
# File Name：     dir_file_change_name
# Description :遍历文件夹修改文件名
# Author :       micro
# Date：          2019/9/17
import glob, os

path = r'C:\Users\micro\Desktop\2016流量'
files = glob.glob(os.path.join(path, "*.xls"))
print(files)
for i in files:
    newname = i.replace(r'szffmr.com全站-受访域名(', '')
    # newname = i + ".csv"
    os.rename(os.path.join(i), os.path.join(newname))
    print('success : ' + newname)
