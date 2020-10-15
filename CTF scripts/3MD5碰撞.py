# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:06:25 2019

@author: cf260
"""

import hashlib

def get_token(txt):
    m1 = hashlib.md5()
    m1.update(txt.encode("utf-8"))
    token = m1.hexdigest()
    return token
for i in range(0,99999999999):
    if get_token(str(i))[0:6] == 'bfa6d6':
        print(i)
        break
