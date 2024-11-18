"""Represent the player who participates by guessing numbers"""
import random
import guessingGame as game #NOTE: this import syntax is needed to avoid circular import

class Player:
    def __init__(self, name):
        self._guess = -1
        self._name = name

    def getGuess(self):
        return self._guess
    
    def play(self):
        self._guess = random.randint(game.s_minGuess, game.s_maxGuess)
        return self._guess
    
    def getName(self):
        return self._name
    
    def setName(self, newname):
        self._name = newname
        
    
    
    