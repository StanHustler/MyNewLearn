# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 00:57:42 2019

@author: cf260
"""

import requests
import re
#import random

url='http://123.206.31.85:10020/'
s=requests.Session()
source=s.get(url)
text=re.search('¼\x9a(.*)<br/>GET',source.text, re.M | re.S)
a=text.group(1)

#a=a[:32]+str(random.randint(0,9))

data = {'key':a}
response = requests.get(url,data)
print (response.text)
