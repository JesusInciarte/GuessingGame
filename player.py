"""Represent the player who participates by guessing numbers"""
import random
from guessingGame import GuessingGame

class Player:
    def __init__(self, name):
        self._guess = -1
        self._name = name

    def getGuess(self):
        return self._guess
    
    def play(self):
        self._guess = random.randit(GuessingGame.s_minGuess, GuessingGame.s_maxGuess)
        return self._guess
    
    def getName(self):
        return self._name
    
    def setName(self, newname):
        self._name = newname
        
    
    
    