# coding:utf-8
# File Name：     fast_modify_and_create_website_page
# Description : 快速修改网站页面和生成相同的其他站页面
# Author :       microease
# Date：          2019/8/26
import os
import re
import codecs


def run():
    # 第一步：找到要修改的文件并判断文件是否存在
    file_path = find_file("C:\\Users\micro\Desktop\酷朔\\")  # 此处填写文件夹路径
    # 第二步：修改文件1：在body前加调用JS代码
    # 第三步：所有的商务通链接加nofollow
    # 第四步 删除headfoot.css
    # 第四步：读取TDK和设置的文件夹名，替换原本的title以前的字符
    title = "非凡酷塑冷冻减脂_瘦身塑形_深圳非凡医疗美容医院"
    keywords = "非凡瘦身塑形,酷塑,酷塑冷冻减脂,减肥"
    description = "非凡酷塑冷冻减脂是非入侵入不需要手术的一种减肥塑形方式，特有的冷冻疗法，不用再担心加肥瘦身困难，轻松瘦下来，达到身体曲线完美，皮肤紧致弹润，并且能达到稳定效果，不会再增脂。"
    new_dir_name = "2019kusuo"
    file_path = modify_file(file_path, new_dir_name, title, keywords, description)
    # 第五步：更换编码为GB2312
    file_path = convert_to_gb2312(file_path)
    # 第六步:生成其他站的文件，并对应好
    # create_new_file(file_path)


def find_file(dir_path):
    if (os.path.exists(dir_path + "index.html")):
        print("文件存在，可以修改！")
        return dir_path + "index.html"


def modify_file(file_path, new_dir_name, title, keywords, description):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:file_path
    """
    old_str_1 = "</body>"
    new_str_1 = '''<script src="http://m.szffmr.com/newjs/jquery-1.9.1.min.js"></script>\n<script type="text/javascript" src="http://m.szffmr.com/newjs/kf.js"></script>\n</body>'''
    old_str_2 = '''target="_blank"'''
    new_str_2 = '''target="_blank" rel="nofollow"'''
    old_str_3 = '''<link rel="stylesheet" type="text/css" href="http://m.szffmr.com/style/headfoot.css?201906102">'''
    new_str_3 = ""
    old_str_4 = '''<html lang="en">'''
    new_str_4 = '''<html lang="zh-cmn-Hans">'''
    old_str_5 = '''<meta charset="UTF-8">'''
    new_str_5 = '''<meta charset="gb2312">\n<base href="http://m.szffmr.com/zhuanti/%s/">''' % new_dir_name
    old_str_6 = '''<meta http-equiv="X-UA-Compatible" content="ie=edge">'''
    new_str_6 = '''<meta http-equiv="X-UA-Compatible" content="ie=edge">\n<meta name="format-detection" content="telephone=no" />\n<meta content="yes" name="apple-mobile-web-app-capable" />\n<meta content="black" name="apple-mobile-web-app-status-bar-style" />'''
    old_str_7 = '''<title>酷朔</title>'''
    new_str_7 = '''<title>%s</title>\n<meta name="keywords" content="%s">\n<meta name="description" content="%s">''' % (
        title, keywords, description)
    file_data = ""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if old_str_1 in line:
                print("发现body,修改ing")
                line = line.replace(old_str_1, new_str_1)
            if old_str_2 in line:
                print("发现target=_blank,修改ing")
                line = line.replace(old_str_2, new_str_2)
            if old_str_3 in line:
                print("发现headfoot.css,修改ing")
                line = line.replace(old_str_3, new_str_3)
            if old_str_4 in line:
                print("发现<html lang=\"en\">,修改ing")
                line = line.replace(old_str_4, new_str_4)
            if old_str_5 in line:
                print("发现<meta charset=\"UTF-8\">,修改ing")
                line = line.replace(old_str_5, new_str_5)
            if old_str_6 in line:
                print("发现meta标头,修改ing")
                line = line.replace(old_str_6, new_str_6)
            if old_str_7 in line:
                print("修改TDK ing")
                line = line.replace(old_str_7, new_str_7)
            file_data += line
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_data)
    return file_path


def convert_to_gb2312(file_path):
    to_coding_type = "GB18030"
    from_coding_type = "utf-8"
    try:
        f = codecs.open(file_path, "rb", from_coding_type)
        new_content = f.read()
        codecs.open(file_path, "wb", to_coding_type).write(new_content)
    except IOError as err:
        print("IO ERROR:".format(err))
    print("转换编码成功！")
    return file_path


# def create_new_file(file_path):
#     desktop = "C:\Users\micro\Desktop\\"
#     if os.path.exists(desktop):
#         print("桌面文件夹存在")

if __name__ == '__main__':
    run()
