# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:31:36 2019

@author: nadia
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand.copy()
    hand_copy=hand.copy()
    if word in wordList:
        try:
            for letter in word: 
                hand_copy[letter]-=1
                if hand_copy[letter]<0: 
                    return False 
            return True
        except KeyError: return False
         
    else:
        return False