#!/usr/bin/env python
# coding:utf-8
"""
Name    : turtle输出sn图.py
Author  : 李贇奇
Contact : cf118799765@gmail.com
Time    : 2021/10/19 15:45
Desc    :
"""
import turtle as t
import math


def draw_diagonals(magnify):
    t.penup()
    t.goto(-100 * magnify, 150 * magnify)
    t.pendown()
    draw_diagonal(magnify)

    t.penup()
    t.goto(-100 * magnify, 50 * magnify)
    t.pendown()
    draw_diagonal(magnify)

    t.penup()
    t.goto(-100 * magnify, -50 * magnify)
    t.pendown()
    draw_diagonal(magnify)


def draw_diagonal(magnify):
    t.seth(360 - math.degrees(math.atan(50 / 100)))
    t.fd(math.sqrt((100 * magnify) ** 2 + (50 * magnify) ** 2))
    t.seth(270)
    t.fd(25*magnify)
    t.back(25*magnify)
    t.seth(math.degrees(math.atan(50 / 100)))
    t.fd(math.sqrt((100 * magnify) ** 2 + (50 * magnify) ** 2))
    t.seth(0)


def draw_rectangle(magnify):
    t.penup()
    t.goto(100 * magnify, 175 * magnify)
    t.pendown()
    for i in range(2):
        t.rt(90)
        t.fd(325 * magnify)
        t.rt(90)
        t.fd(200 * magnify)
    t.penup()
    t.goto(-100 * magnify, 150 * magnify)
    t.pendown()
    for i in range(12):
        if (i == 1 or i == 5 or i == 9):
            t.seth(270)
            t.fd(25 * magnify)
            t.seth(0)
            t.pendown()
        else:
            t.fd(200 * magnify)
            t.penup()
            t.back(200 * magnify)
            t.seth(270)
            t.fd(25 * magnify)
            t.seth(0)
            t.pendown()
    draw_diagonals(magnify)
    mid(magnify)


def write(x, y, text, magnify):
    t.penup()
    t.goto(x * magnify, y * magnify)
    t.pendown()
    t.write(text, align='center', font=('宋体', math.ceil(10 * magnify), 'normal'))


def mid(magnify):
    write(0, 150, "输入abc", magnify)
    write(0, 125, "a大于b", magnify)
    write(-50, 100, "T", magnify)
    write(50, 100, "F", magnify)
    write(-50, 75, "交换a和b", magnify)
    write(0, 50, "输入abc", magnify)
    write(0, 25, "a大于c", magnify)
    write(-50, 0, "T", magnify)
    write(50, 0, "F", magnify)
    write(-50, -25, "交换a和c", magnify)
    write(0, -50, "输入abc", magnify)
    write(0, -75, "b大于c", magnify)
    write(-50, -100, "T", magnify)
    write(50, -100, "F", magnify)
    write(-50, -125, "交换b和c", magnify)
    write(0, -150, "输出abc", magnify)


if __name__ == '__main__':
    t.speed("fastest")
    draw_rectangle(2)
    input()
