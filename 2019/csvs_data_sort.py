# coding:utf-8
# File Name：     csv_data_sort
# Description :
# Author :       micro
# Date：          2019/9/17
import pandas as pd
import numpy as np
import glob, os

path = r'C:\Users\micro\Desktop\2018流量'
files = glob.glob(os.path.join(path, "*.csv"))

dl= []
for f in files:
    dl.append(pd.read_excel(f,header=[0,1],index_col=None))
df=pd.concat(dl)


def run():
    pass
    #  第一步 遍历读取文件夹，获取每个csv的路径

if __name__ == '__main__':
    run()
