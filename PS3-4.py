# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:31:56 2019

@author: nadia
"""

#the last part of the "Hang Man" problem set

def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+ str(len(secretWord)) +' letters long.')
    lettersGuessed = []
    lettersGuessed1= []
    j=8
    space='_'
    print("-----------") 
    while j>0 and space in getGuessedWord(secretWord, lettersGuessed):
        print('You have ' + str(j) + ' guesses left.')
        print('Available letters: '+ getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ') 
        guessInLowerCase = guess.lower()
        lettersGuessed += guessInLowerCase
        if guessInLowerCase in lettersGuessed1:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed1))
        elif guessInLowerCase in secretWord:
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            j-=1
        lettersGuessed1+=guessInLowerCase 
        print("-----------") 
    space='_'
    if j==0:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)
    elif space not in getGuessedWord(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    