# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:36:40 2019

@author: cf260
"""

x=''
import re
a = open('ascaaa.log','r').readlines()
for i in range(int(len(a))):
    try:
        text=re.search('%29%3\D(.*)--%20',a[i], re.M | re.S)
        x+=text.group(1)+','
    except:
        continue
    