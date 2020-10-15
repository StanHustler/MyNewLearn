# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:42:04 2018

@author: cf260
"""

import requests
import re
url='http://123.206.31.85:10002/'

s=requests.Session()
source=s.get(url)

text=re.search('<br/>\\n(.*)</p>',source.text, re.M | re.S)#re.M匹配多行，re.S匹配一行

#print(text.group(1))

result=eval(text.group(1))
payload= {'result':result}
a=s.post(url,data=payload)
print (a.text)