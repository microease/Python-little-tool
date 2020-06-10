# coding:utf-8
# File Name：     fast_copy
# Description : 快速根据一个专题生成其他网站的专题文件
# Author :       huxiaoyi
# Date：          2019/9/1
import os
import shutil


def run():
    #域名列表
    domains = ["m.szffmr.com", "mm.szffmr.com", "m.88833222.com", "m.ffyy.cc", "wap.mr91.com",
               "baidu.mr91.com"]
    #桌面地址
    desktop = "C:\\Users\micro\Desktop\\"
    #新专题文件夹名称
    new_dir_name = "202005tmj"
    #各专题文件夹地址
    dirs = ["/网站文件/szffmr/wap/zhuanti/", "/网站文件/szffmr/mm/zhuanti/", "/网站文件/www.88833222.com/wap/zhuanti/",
            "/网站文件/www.ffyy.cc/wap/zhuanti/", "/网站文件/wap.mr91.com/zhuanti/", "/网站文件/baidu.mr91.com/zhuanti/"]
    #新专题文件夹地址
    new_dirs = [desktop + i + new_dir_name + "/" for i in dirs]
    new_index_htmls = [i + "index.html" for i in new_dirs]
    wait_copy_dir = r"C:\Users\micro\Desktop\jgquban"
    copy(wait_copy_dir, new_dirs)
    modify_link(domains, new_index_htmls)


def copy(wait_copy_dir, new_dirs):
    for i in new_dirs:
        if (not os.path.exists(i)):
            shutil.copytree(wait_copy_dir, i)
        else:
            print("地址存在，删除文件夹后重试")

def modify_link(domains, new_index_htmls):
    for i in new_index_htmls:
        print(i)
        # 修改mmszffmrcom
        file_data = ""
        with open(i, "r", encoding="GB18030") as f:
            for line in f:
                if domains[0] in line:
                    print("发现m.szffmr.com,修改ing")
                    line = line.replace(domains[0], domains[new_index_htmls.index(i)])
                file_data += line
        with open(i, "w", encoding="GB18030") as f:
            f.write(file_data)


if __name__ == '__main__':
    run()
