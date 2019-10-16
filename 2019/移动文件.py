# coding:utf-8
# File Name：     移动文件
# Description :
# Author :       micro
# Date：          2019/10/16
import os
import shutil


def mycopy(srcpath,dstpath):
    if not os.path.exists(srcpath):
        print ("srcpath not exist!")
    if not os.path.exists(dstpath):
        os.mkdir(dstpath)
        print ("dstpath not exist! but has been creat!")
    for root,dirs,files in os.walk(srcpath,True):
        for eachfile in files:
            shutil.copy(os.path.join(root,eachfile),dstpath)


while True:
    print("欢迎使用胡炎凯开发的自动移动文件程序\n")
    print("选项1：自动移动www.szffmr.com后台到备份文件夹\n")
    print("选项2：自动移动m.szffmr.com后台到备份文件夹\n")
    print("选项3：自动移动mm.szffmr.com后台到备份文件夹\n")
    print("选项4：自动移动www.88833222.com全站文件到备份文件夹\n")
    print("选项5：自动移动www.ffyy.cc全站文件到备份文件夹\n")
    print("选项6：自动执行上述所有操作")
    user_input = input()
    print(user_input)
    if user_input == "1":
        mycopy(r'D:\\www.ffyy.cc', r'D:\beifen\www.ffyy.cc')
