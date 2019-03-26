# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:31:21 2019

@author: nadia
"""

#the third part of the "Hang Man" problem set

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters='abcdefghijklmnopqrstuvwxyz'
    allLetters=list(allLetters)
    i=0
    while i<len(lettersGuessed):
        if lettersGuessed[i] in allLetters:
            allLetters.remove(lettersGuessed[i])
            i+=1
    ans=''.join(allLetters)
    return ans
               