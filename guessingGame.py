"""defines the game logic for the guessing game"""

from player import Player

class GuessingGame:
    def __init__(self):
        self._answer = -1
        self._roundCount = 0

        #create the 3 players OBJs
        self._larry = Player("Larry")
        self._curly = Player("Curly")
        self._moe = Player("Moe")

        #ElaraStats = Character("Elara", 20, 15, 30, 100)


    def start(self):
        pass

    def determineWinner(self):
        pass