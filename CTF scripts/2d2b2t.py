# -*- coding: utf-8 -*-
"""

@author: cf260
"""
import libnum
import sys
ss=''
s=[1,27,59,11,23,7,57,1,1,76,222,1,1,50,214,6,77,50,53,214,6]
for i in s:
	ss+=bin(i)[2:]

type = sys.getfilesystemencoding()
print(libnum.b2s(ss).decode('utf-8').encode(type))
####libnum在python 3中会因为没有部分参数报错，在2中正常使用