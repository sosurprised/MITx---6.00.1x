# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:49:19 2019

@author: nadia
"""

#s is a string of lower case characters
# the program that prints the longest substring of s 
#in which the letters occur in alphabetical order
#in the case of ties, print the first substring

s = 'krfiajwbbxknrdiurec'

count=0
maxCount=0
endStrIndex=0
for i in range(len(s)-1):
    if s[i]<=s[i+1]:
        count+=1
        if count>maxCount:
            maxCount=count
            endStrIndex=i+1
    else:
        count=0
startStrIndex=endStrIndex-maxCount
print('Longest string in the alphabetical order is: ' + s[startStrIndex:endStrIndex+1])