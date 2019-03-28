# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:32:57 2019

@author: nadia
"""

#playing a hand

def playHand(hand, wordList, n):
    new_score=0
    while calculateHandlen(hand)>0:
        print("Current Hand: ", end="")
        displayHand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        if word=='.':
            break
            print('Goodbye! Total score: '+ str(new_score) + ' points.')
        else:
            if isValidWord(word, hand, wordList)==False:
                    print('Invalid word, please try again.')
                    print()

            else:
                new_score+=int(getWordScore(word, n))
                print('"' + str(word) + '"' + ' earned ' + str(getWordScore(word, n)) + ' points. Total: ' + str(new_score) + ' points')
                print()
                hand=updateHand(hand, word)

    print('Run out of letters. Total score:' + str(new_score) + ' points')