# coding:utf-8
# File Name：     fast_modify_special
# Description :
# Author :       micro
# Date：          2019/9/3
import os


# 批量修改文件夹中的index.shtml
def run():
    # 第一步，读取所有的子文件夹，形成地址列表
    all_child_dir = get_all_child_dir("C:\\Users\micro\Desktop\闭馆")
    # 第二步,判断路径下的index.shtml是否存在，如果存在加入新的index.shtml列表
    index_shtml = get_all_index_shtml(all_child_dir)
    # 第四步 转换gb2312的文件列表为utf-8
    index_shtml = modify_file(index_shtml)


def get_all_child_dir(path):
    dir_list = []
    # 判断路径是否存在
    if (os.path.exists(path)):
        print("该母路径存在")
        # 获取该目录下的所有文件或文件夹目录
        files = os.listdir(path)
        for file in files:
            # 得到该文件夹下所有子目录的路径
            m = os.path.join(path, file)
            # 判断是否为文件夹
            if (os.path.isdir(m)):
                dir_list.append(m)
    print("所有列表如下")
    print(dir_list)
    return dir_list


def get_all_index_shtml(all_child_dir):
    index_shtml = []
    for i in all_child_dir:
        i = i + "\index.html"
        # 判断文件是否存在
        if os.path.exists(i):
            index_shtml.append(i)
    print("index.shtml列表如下")
    print(index_shtml)
    return index_shtml


def modify_file(index_shtml):
    old_str_1 = '''/zt/'''
    new_str_1 = '''/mzt/'''
    for i in index_shtml:
        file_data = ""
        with open(i, "r", encoding="utf-8") as f:
            for line in f:
                if old_str_1 in line:
                    print("发现file,修改ing")
                    line = line.replace(old_str_1, new_str_1)
                file_data += line
        with open(i, "w", encoding="utf-8") as f:
            f.write(file_data)
    return index_shtml


if __name__ == '__main__':
    run()
