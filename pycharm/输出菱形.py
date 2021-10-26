#!/usr/bin/env python
# coding:utf-8
"""
Name    : 输出菱形.py
Author  : Stan Hustler
Contact : cf118799765@gmail.com
Time    : 2021/10/26 8:41
Desc    :
"""


n = eval(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
m=2*n-1
for i in range(1,n):
    for j in range(i):
        print(' ',end='')
    m-=2
    for j in range(m):
        print('*',end ='')
    print()