# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 02:35:04 2019

@author: cf260
"""

import requests
import base64
url='http://123.206.87.240:8002/web6/'

s=requests.Session()
source=s.get(url)
mingwen=base64.b64decode(source.headers['flag'])
mingwen=str(mingwen)
result= mingwen.split(": ")[1]
payload= {'margin':result}
a=s.post(url,data=payload)
print (a.text)


url = 'http://120.24.86.145:8002/web6/'
session = requests.Session()
req = session.get(url)
header_flag = req.headers['flag']
header_flag_decode = base64.decodestring(header_flag)
margin_value = header_flag_decode.split(": ")[1]
print(margin_value)
post_page = session.post(url,{"margin":base64.decodestring(margin_value)})
print(post_page.text)