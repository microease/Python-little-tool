# coding:utf-8
# File Name：     06_proxy_handler
# Description :
# Author :       micro
# Date：          2019/12/22
import urllib.request


def create_proxy_handler():
    url = "http://www.baidu.com"
    proxy_list = [
        {"https": "aaaaaaaaaaaaadsafdsg"},
        {"https": "https://115.221.244.86:9999"},
        {"https": "https://115.221.244.86:9999"},
        {"https": "https://115.221.244.86:9999"},
        {"https": "https://115.221.244.86:9999"},

    ]
    for proxy in proxy_list:
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        try:
            opener.open("http://www.baidu.com/", timeout=1)
            print("haha")
        except Exception as e:
            print(e)


create_proxy_handler()
