# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:35:32 2019

@author: nadia
"""
#counting vowels in a string

s='anhtarehs'
numVowels=0    
for char in s: 
    if char == 'o' or char == 'u' or char == 'e' or char == 'a' or char == 'i':
        numVowels+=1
print ('Number of vowels is: ' + str(numVowels))
