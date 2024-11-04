"""Represent the player who participates by guessing numbers"""
import random
class Player:
    def __init__(self):
        self._guess = -1
        self._name = ""

    def getGuess(self):
        return guess
    
    def play(self):
        guess = random.randit(1,10)
        return guess
    def getName(self):
        return self._name
    
    def setName(self, newname):
        self._name = newname
    
    