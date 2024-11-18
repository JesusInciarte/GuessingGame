"""Defines the interactivePlayer class"""
from player import Player
from guessingGame import GuessingGame

class InteractivePlayer(Player): # interactivePlayer IS-A Player
    def __init__(self, name):
        Player.__init__(self, name)

        def play(self):
            self._guess = int(input(f"Please enter a number from {GuessingGame.s_minGuess} to {GuessingGame.s_maxGuess}: "))







