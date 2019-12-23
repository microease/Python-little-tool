# coding:utf-8
# File Name：     02-params2
# Description :
# Author :       micro
# Date：          2019/12/20
import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?"
    params = {
        "wd": "中文",
        "key": "zhang",
        "value": "san",
    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)


get_params()
