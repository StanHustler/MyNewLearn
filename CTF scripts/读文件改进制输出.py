# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 00:07:49 2019

@author: cf260
"""

A=''
a = open('进制.txt','r').readline()
s = a.split(" ")
for i in range(len(s)):
    b=s[i]
    if b[0:1]=='d':
        A+=hex(int(b[1:]))[2:]
    elif b[0:1]=='o':
        A+=hex(int(b[1:],8))[2:]
    elif b[0:1]=='b':
        A+=hex(int(b[1:],2))[2:]
    else:
        A+=b[1:]