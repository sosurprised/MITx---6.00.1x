# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:35:29 2019

@author: gecap
"""

def playGame(wordList):
    hand={}
    while True:
        choice=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        try:
            if choice=='n':
                hand=dealHand(HAND_SIZE)
                copy_hand=hand.copy()
                playHand(copy_hand, wordList, HAND_SIZE)
            elif choice=='r':
                    if hand=={}:
                        print('You have not played a hand yet. Please play a new hand first!')
                    else:
                        playHand(copy_hand, wordList, HAND_SIZE)
            elif choice=='e':
                break 
            else:
                print('Invalid command.')
        except:
                print('Invalid command.')
            