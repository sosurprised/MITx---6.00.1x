# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:32:26 2019

@author: nadia
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())
