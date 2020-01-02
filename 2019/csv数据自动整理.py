# coding:utf-8
# File Name：     csv_data_sort
# Description :
# Author :       micro
# Date：          2019/9/17
import glob, os
import csv
import xlrd, xlwt
from xlutils.copy import copy


def run():
    #  第一步 遍历读取文件夹，获取每个csv的路径
    path = r'C:\Users\micro\Desktop\新建文件夹'
    files = glob.glob(os.path.join(path, "*.csv"))
    print(files)
    # 第二步 分别遍历每个文件,并获取所需要网站的UV
    all_result = []
    for file in files:
        csvFile = open(file, "r", encoding='gb18030', errors='ignore')
        reader = csv.reader(csvFile)
        m_ffyy_cc_uv = 0
        www_ffyy_cc_uv = 0
        for item in reader:
            if (len(item) > 1):
                if (item[0] == "www.szffmr.com"):
                    www_szffmr_com_uv = item[2]
                if (item[0] == "m.szffmr.com"):
                    m_szffmr_com_uv = item[2]
                if (item[0] == 'mm.szffmr.com'):
                    mm_szffmr_com_uv = item[2]
                if (item[0] == "m.88833222.com"):
                    m_88833222_com_uv = item[2]
                if (item[0] == "m.ffyy.cc"):
                    m_ffyy_cc_uv = item[2]
                if (item[0] == "www.ffyy.cc"):
                    www_ffyy_cc_uv = item[2]
        result = [www_szffmr_com_uv, m_szffmr_com_uv, mm_szffmr_com_uv, m_88833222_com_uv, m_ffyy_cc_uv, www_ffyy_cc_uv]
        all_result.append(result)
    write_excel_xls_append(r"C:\Users\micro\Desktop\2019.xlsx", all_result)


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


if __name__ == '__main__':
    run()
