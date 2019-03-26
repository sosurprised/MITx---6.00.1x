# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:28:45 2019

@author: nadia
"""
#the first part of the "Hang Man" problem set

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i=0
    while secretWord[i] in lettersGuessed:
        i+=1
        if i==len(secretWord):
            return True
    if i<len(secretWord):
        return False
