"""Represent the guessing game application responsible for user interaction and for creating 
and running the guessing game"""
from guessingGame import GuessingGame

class Application:
    def run(self):
        #create game
        game = GuessingGame()

        #start the game
        game.start()
