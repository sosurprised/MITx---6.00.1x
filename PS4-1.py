# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:27:27 2019

@author: nadia
"""
#writing methods for the Scrabble program 
#implement some code that allows us to calculate
#the score for a single word


def getWordScore(word, n):
    score=0
    word_low=word.lower()
    i=0
    while i<len(word_low):
        if word_low[i] in SCRABBLE_LETTER_VALUES:
            score+=SCRABBLE_LETTER_VALUES[word_low[i]]
            i+=1
    score=score*len(word)
    if len(word_low)==n:
        score=score+50
        
    return score