#!/usr/bin/env python
# coding:utf-8
"""
Name    : 金字塔.py
Author  : Stan Hustler
Contact : cf118799765@gmail.com
Time    : 2021/10/26 0:12
Desc    :
"""


# n=int(input())+1
# for i in range(1,n):
#
#     for j in range(n-i):
#         print(" ",end='')
#     for j in range(2*i - 1):
#         print('*',end='')
#
#     print()

n = eval(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# 倒序
# x = eval(input())
# i = 1
# while i <= x:
#     j = x # j=每行的*数
#     while j >= i:
#         print("*",end = "")
#         j -= 1
#     print()
#     i += 1
