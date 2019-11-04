# coding:utf-8
# File Name：     pdf_to_jpg
# Description :
# Author :       micro
# Date：          2019/11/4
# -*- coding: utf-8 -*-
from wand.image import Image
# Converting first page into JPG
with Image(filename="D:\\1.pdf[0]") as img:
     img.save(filename="/temp.jpg")