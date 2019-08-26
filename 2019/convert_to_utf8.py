# coding=utf-8
import os
import chardet
import codecs


# 批量转换文件夹中的index.shtml为utf-8编码
def run():
    # 第一步，读取所有的子文件夹，形成地址列表
    all_child_dir = get_all_child_dir("D:\\2")
    # 第二步,判断路径下的index.shtml是否存在，如果存在加入新的index.shtml列表
    index_shtml = get_all_index_shtml(all_child_dir)
    # 第三步 自动判断index.shtml文件的编码，如果为gb2312，加入新列表
    gb2312_list = get_all_gb2312(index_shtml)
    # 第四步 转换gb2312的文件列表为utf-8
    convert_to_utf8(gb2312_list)


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
        i = i + "\index.shtml"
        # 判断文件是否存在
        if os.path.exists(i):
            index_shtml.append(i)
    print("index.shtml列表如下")
    print(index_shtml)
    return index_shtml


def get_all_gb2312(index_shtml):
    gb2312_list = []
    for i in index_shtml:
        # with open(i, 'rb') as f:
        #     if chardet.detect(f.read())['encoding'] == "GB2312":
        #         gb2312_list.append(f)
        f = open(i, "rb")
        data = f.read()
        print(chardet.detect(data)["encoding"])
        # 如果文件为Gb2312加入新列表
        if (chardet.detect(data)["encoding"] == "GB2312"):
            gb2312_list.append(i)
    print("GB2312列表如下")
    print(gb2312_list)
    return gb2312_list


def convert_to_utf8(gb2312_list):
    to_coding_type = "utf-8"
    from_coding_type = "ansi"
    jishuqi = 0
    for i in gb2312_list:
        try:
            f = codecs.open(i, "rb", from_coding_type)
            new_content = f.read()
            codecs.open(i, "wb", to_coding_type).write(new_content)
            jishuqi += 1
        except IOError as err:
            print("IO ERROR:".format(err))
    print("本次转换%d个文件" % jishuqi)


if __name__ == '__main__':
    run()
