# coding:utf-8
# File Name：     01-url-open-code
# Description :
# Author :       micro
# Date：          2019/12/19
import urllib.request


def load_data():
    url = "http://www.baidu.com/"
    response = urllib.request.urlopen(url)
    print(response)
    data = response.read()
    print(data)
    str_data = data.decode("utf-8")
    print(str_data)
    with open("baidu.html",'w',encoding="utf-8") as f:
        f.write(str_data)

load_data()