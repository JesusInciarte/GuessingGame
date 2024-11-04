"""Represent the player who participates by guessing numbers"""
import random
class Player:
    def __init__(self, name):
        self._guess = -1
        self._name = name

    def getGuess(self):
        return guess
    
    def play(self):
        self._guess = random.randit(0,9)
        return self._guess
    
    def getName(self):
        return self._name
    
    def setName(self, newname):
        self._name = newname
    
    