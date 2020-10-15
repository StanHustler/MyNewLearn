# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 00:04:39 2019

@author: cf260
"""

import re
str1=input('input the text :')
str1 = re.sub(r"(?<=\w)(?=(?:\w\w)+$)"," ",str1)
list1 = str1.split()
list1 = list(reversed(list1))
str1 = " ".join(list1)
print(str1)
