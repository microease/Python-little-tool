# coding:utf-8
# File Name：     06_proxy_handler
# Description :
# Author :       micro
# Date：          2019/12/22
import urllib.request


def create_proxy_handler():
    url = "http://www.baidu.com"
    proxy = {
        "https": "https://115.221.244.86:9999"
    }
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    data = opener.open(url).read()
    print(data)

create_proxy_handler()