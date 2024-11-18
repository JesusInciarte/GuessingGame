"""Defines the interactivePlayer class"""
from player import Player
import guessingGame as game #NOTE: this import syntax is needed to avoid circular import

class InteractivePlayer(Player): # interactivePlayer IS-A Player
    def __init__(self, name):
        Player.__init__(self, name)

        def play(self):
            self._guess = int(input(f"Please enter a number from {game.s_minGuess} to {game.s_maxGuess}: "))
            
            
            
            
            
            
            
            