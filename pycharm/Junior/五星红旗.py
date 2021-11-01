#!/usr/bin/env python
# coding:utf-8
"""
Name    : 五星红旗.py
Author  : 李贇奇(Stan Hustler)
Contact : cf118799765@gmail.com
Time    : 2021/9/29 21:19
Desc    :
"""

import turtle as t
import math


def draw_rectangle(start_x, start_y, x, y):  # 画矩形
    t.penup()
    t.pencolor('black')
    t.goto(start_x, start_y)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    for i in range(2):
        t.forward(x)
        t.rt(90)
        t.forward(y)
        t.rt(90)
    t.end_fill()


def draw_star(x, y, r, angle=0.0):  # 画星星
    t.penup()
    t.setheading(90)
    t.lt(angle)
    t.goto(x, y)
    t.forward(r)
    t.rt(180-36/2)
    t.pendown()
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(2 * r * math.cos(math.pi/10))
        t.rt(144)
    t.end_fill()


if __name__ == '__main__':
    t.speed('fast')
    draw_rectangle(-300, 200, 600, 400)  # 画国旗框
    draw_star(-200, 100, 60)  # 画大星
    draw_star(-100, 160, 20, 180 - math.tan(5/3)*180)  # 画第一颗小星
    draw_star(-60, 120, 20, 180 - math.tan(7)*180)  # 画第二颗小星
    draw_star(-60, 60, 20)  # 画第三颗小星
    draw_star(-100, 20, 20, math.tan(5/4)*180)  # 画第四颗小星
    input()
