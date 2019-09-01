# coding:utf-8
# File Name：     get_odds_500_com
# Description :
# Author :       huxiaoyi
# Date：          2019/9/1
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
response = requests.get("http://odds.500.com/fenxi/shuju-806577.shtml",headers = headers)
print(response.request.headers)
#自动解决乱码问题
response.encoding = response.apparent_encoding
print(response.text)