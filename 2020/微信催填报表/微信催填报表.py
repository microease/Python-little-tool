# coding:utf-8
# File Name：     微信催填报表
# Description :
# Author :       micro
# Date：          2020/4/9

# 导入模块
import itchat

itchat.auto_login()

itchat.send('今天还没有填表，快点填吧！', toUserName='文件传输助手')