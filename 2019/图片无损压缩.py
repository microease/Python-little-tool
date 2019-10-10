# coding:utf-8
# File Name：     图片压缩
# Description :
# Author :       micro
# Date：          2019/10/7
import tinify
import os
tinify.key = 'SHhhzPb7lNm01Gr74j2TGmfxyDrZYpXs'
print("欢迎使用胡炎凯开发的自动图片无损压缩工具。请输入你要转换的图片地址路径,注意必须是绝对地址：")

path = input()  # 图片存放的路径
# path = r"C:\Users\micro\Desktop\input"
print(path)
for dirpath, dirs, files in os.walk(path):
    for file in files:
        imgpath = os.path.join(dirpath, file)
        print("compressing ..." + imgpath)
        tinify.from_file(imgpath).to_file(imgpath)
