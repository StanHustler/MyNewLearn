# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:47:18 2020

@author: cf260
"""

a='0000101000000011000101110000001001010110000000010001010100010001000010100001010000001110000010100001111000110000000011100000101000011110001100000000111000001010000111100011000000010100000011000001100100001101000111110001000000001110000001100000001100011000'
b='0110110001101111011101100110010101101100011011110111011001100101011011000110111101110110011001010110110001101111011101100110010101101100011011110111011001100101011011000110111101110110011001010110110001101111011101100110010101101100011011110111011001100101'
d='';
for i in range(len(a)):
	d+=str(int(a[i])^int(b[i]))

print(d);