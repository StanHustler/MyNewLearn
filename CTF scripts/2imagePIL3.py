#-*- coding:utf-8 -*-
from PIL import Image
x = 280 #x坐标  通过对txt里的行数进行整数分解
y = 280 #y坐标  x*y = 行数

im = Image.new("RGB",(x,y))#创建图片
file=open('09.txt','r') #打开rbg值文件
for i in range(0,x):
    for j in range(0,y):
        line = file.readline()#获取一行
        rgb = line.split(" ")#分离rgb
        im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
im.show()

