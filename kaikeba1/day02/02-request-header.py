# coding:utf-8
# File Name：     02-request-header
# Description :
# Author :       micro
# Date：          2019/12/22
import urllib.request


def load_url():
    url = "https://www.baidu.com/"
    # 创建请求信息
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(url)
    request_headers = request.headers
    print(request_headers)
    print("--------------响应头")
    print(response.headers)

load_url()