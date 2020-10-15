# -*- coding: utf-8 -*-
import hashlib
c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
miwen='e9032???da???08????911513?0???a2'
flag=0
def f(mds):
    for i in range(0,len(miwen)):
        if miwen[i]=='?':
            continue
        elif miwen[i]!=mds[i]:
            return 0
    return 1
for i in range(0,len(c)):
    if flag==1:
        break
    for j in range(0,len(c)):
        for k in range(0,len(c)):
            b='TASC'+c[i]+'O3RJMV'+c[j]+'WDJKX'+c[k]+'ZM' #mingwen
            md=hashlib.md5(b.encode('utf8'))
            mds=md.hexdigest()
            flag=f(mds)
            if flag==1:
                print(mds)