# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:29:50 2019

@author: nadia
"""
#the second part of the "Hang Man" problem set

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    i=0
    l=[]
    while i<len(secretWord):
        if secretWord[i] in lettersGuessed:
            l += secretWord[i]
        else:
            l += '_'
        i+=1
    ans=str(' '.join(l))
    return ans
    


