# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:43:42 2019

@author: nadia
"""
#counting the number of times "bob" occurs in a string
s="ioprnabgtobobobobahy"

numBob=0
index=0
i=0
j=3
while index<len(s):
    if s[i:j]=="bob":
        numBob+=1
        index+=1
        i+=1
        j+=1
    else:
        index+=1
        i+=1
        j+=1
print('Number of times bob occurs is: '+str(numBob))
