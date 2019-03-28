# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:30:23 2019

@author: nadia
"""

def updateHand(hand, word):
    hand_copy= hand.copy()
    for letter in word:
        hand_copy[letter]-=1
    return hand_copy
    
