# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:43:01 2019

@author: cf260
"""
from PIL import Image
import os

s=''
x=1
path=os.listdir(r"C:\Users\cf260\Desktop\c6d4e637b62049dba3a3744c68a0cb7e\gif")


################            RENAME                    
a=0
for a in range (len(path)):   
    if len(path[a]) <7:
         oldname=r"C:\Users\cf260\Desktop\c6d4e637b62049dba3a3744c68a0cb7e\gif\\"+path[a]  #设置旧文件名（就是路径+文件名） 
         if len(path[a]) ==5:
             newname=r"C:\Users\cf260\Desktop\c6d4e637b62049dba3a3744c68a0cb7e\gif\\"+'00'+path[a]   #设置新文件名 
         else:
             newname=r"C:\Users\cf260\Desktop\c6d4e637b62049dba3a3744c68a0cb7e\gif\\"+'0'+path[a]
         os.rename(oldname,newname) #用os模块中的rename方法对文件改名
################            RENAME




################            LOADPIX          【取色对比】
path=os.listdir(r"C:\Users\cf260\Desktop\c6d4e637b62049dba3a3744c68a0cb7e\gif")
for i in path:

    im = Image.open(r"C:\Users\cf260\Desktop\c6d4e637b62049dba3a3744c68a0cb7e\gif\\"+i,'r')
    pix=im.load()#导入像素
#    im.show()
    

    

    if pix[0,0] == (12, 12, 0):
        s+='1'
    else:
        s+='0'
################            LOADPIX        
#    if x % 8 == 0:
#        s+=" "
#    x+=1
        
################            LOADPIX          【size对比】  
path=os.listdir(r"C:\Users\cf260\Desktop\wenjian")
for i in path:

    a=os.path.getsize(r"C:\Users\cf260\Desktop\wenjian\\"+i)
    if a == 443:
        x+='0'
    else:
        x+='1'        