# -*- coding:utf-8 -*-
from PIL import Image
x = 45
y = 45

im = Image.new("RGB", (x, y))  # 创建图片
file = open('1.txt', 'r')  # 打开rbg值文件
for i in range(0, x):
    line = file.readline()  # 获取一行
    for j in range(0, y):
        if line[j] == '0':
            im.putpixel((i, j), (255, 255, 255))  # rgb转化为像素
        else:
            im.putpixel((i, j), (0, 0, 0))  # rgb转化为像素
im.show()
