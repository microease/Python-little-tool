# coding:utf-8
# File Name：     批量ping
# Description :
# Author :       micro
# Date：          2019/12/9
import socket

host_list = [
    'www.szffmr.com',
    'm.szffmr.com',
    'mm.szffmr.com',
    'www.88833222.com',
    'm.88833222.com',
    'www.ffyy.cc',
    'm.ffyy.cc',
    'm.ffyyshop.com',
    'www.mr91.com',
    'm.mr91.com',
    'pc.mr91.com',
    'wap.mr91.com',
    'baidu.mr91.com',
    'www.feifanbaobei.com',
    'm.feifanbaobei.com',
    'www.feifanhua.com',
    'www.szfeifan.cn',
]

port = 80

for i in host_list:
    ip = socket.gethostbyname(i)
    print(i + '的IP地址是'  + ip)
