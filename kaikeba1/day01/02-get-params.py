# coding:utf-8
# File Name：     02-get-params
# Description :
# Author :       micro
# Date：          2019/12/20
import urllib.request
import urllib.parse
import string


def get_method_params():
    url = "https://www.baidu.com/s?wd="
    name = "美女"
    final_url = url + name
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    data = response.read().decode()
    with open("02-encode.html", "w", encoding="utf-8") as f:
        f.write(data)


get_method_params()
