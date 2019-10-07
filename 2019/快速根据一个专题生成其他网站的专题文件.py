# coding:utf-8
# File Name：     fast_copy
# Description : 快速根据一个专题生成其他网站的专题文件
# Author :       huxiaoyi
# Date：          2019/9/1
import os
import shutil


def run():
    # 第一步 根据桌面地址创建好对应的文件夹
    # 在这里输入桌面文件夹地址
    desktop = "C:\\Users\micro\Desktop\\"
    # 在这里输入你想要的文件夹名称
    new_dir_name = "2019quba"
    mszffmrcom, mmszffmrcom, m88833222com, mffyycc = mkdir(desktop, new_dir_name)
    # 第二步 根据读取的文件夹文件复制所有文件到每个网站对应的文件夹中 返回四个index.html地址
    # 在这里输入需要复制的专题地址
    wait_copy_dir = r"C:\Users\micro\Desktop\祛疤专题"
    mszffmrcomindex, mmszffmrcomindex, m88833222comindex, mffyyccindex = \
        copy(wait_copy_dir, mszffmrcom, mmszffmrcom, m88833222com, mffyycc)
    # 第三步 分别修改四个网站的文件夹中index.html中的链接。
    modify_link(mszffmrcomindex, mmszffmrcomindex, m88833222comindex, mffyyccindex)


def mkdir(desktop, new_dir_name):
    mszffmrcom = desktop + "/网站文件/szffmr/wap/zhuanti/" + new_dir_name
    mmszffmrcom = desktop + "/网站文件/szffmr/mm/zhuanti/" + new_dir_name
    m88833222com = desktop + "/网站文件/www.88833222.com/wap/zhuanti/" + new_dir_name
    mffyycc = desktop + "/网站文件/www.ffyy.cc/wap/zhuanti/" + new_dir_name
    return mszffmrcom, mmszffmrcom, m88833222com, mffyycc


def copy(wait_copy_dir, mszffmrcom, mmszffmrcom, m88833222com, mffyycc):
    if (not os.path.exists(mszffmrcom)):
        shutil.copytree(wait_copy_dir, mszffmrcom)
        shutil.copytree(wait_copy_dir, mmszffmrcom)
        shutil.copytree(wait_copy_dir, m88833222com)
        shutil.copytree(wait_copy_dir, mffyycc)
    else:
        print("地址存在，删除文件夹后重试")
    mszffmrcomindex = mszffmrcom + "/index.html"
    mmszffmrcomindex = mmszffmrcom + "/index.html"
    m88833222comindex = m88833222com + "/index.html"
    mffyyccindex = mffyycc + "/index.html"
    return mszffmrcomindex, mmszffmrcomindex, m88833222comindex, mffyyccindex


def modify_link(mszffmrcomindex, mmszffmrcomindex, m88833222comindex, mffyyccindex):
    if (os.path.exists(mszffmrcomindex)):
        print(mmszffmrcomindex + "文件存在，可以修改！")
        old_str_1 = '''m.szffmr.com'''
        new_str_1 = '''mm.szffmr.com'''
        new_str_2 = '''m.88833222.com'''
        new_str_3 = '''m.ffyy.cc'''
        mmszffmrcom_file_data = ""
        m88833222com_file_data = ""
        mffyycc_file_data = ""
        # 修改mmszffmrcom
        with open(mmszffmrcomindex, "r", encoding="GB18030") as f:
            for line in f:
                if old_str_1 in line:
                    print("发现m.szffmr.com,修改ing")
                    line = line.replace(old_str_1, new_str_1)
                mmszffmrcom_file_data += line
        with open(mmszffmrcomindex, "w", encoding="GB18030") as f:
            f.write(mmszffmrcom_file_data)
        # 修改m.88833222.com
        with open(m88833222comindex, "r", encoding="GB18030") as f:
            for line in f:
                if old_str_1 in line:
                    print("发现m.szffmr.com,修改ing")
                    line = line.replace(old_str_1, new_str_2)
                m88833222com_file_data += line
        with open(m88833222comindex, "w", encoding="GB18030") as f:
            f.write(m88833222com_file_data)
        # 修改mffyyccindex
        with open(mffyyccindex, "r", encoding="GB18030") as f:
            for line in f:
                if old_str_1 in line:
                    print("发现m.szffmr.com,修改ing")
                    line = line.replace(old_str_1, new_str_3)
                mffyycc_file_data += line
        with open(mffyyccindex, "w", encoding="GB18030") as f:
            f.write(mffyycc_file_data)


if __name__ == '__main__':
    run()
