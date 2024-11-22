"""Defines the game logic for the guessing game"""

import random
import player
from interactivePlayer import InteractivePlayer
class GuessingGame:
    
    #define static/shared field variables
    s_minGuess = 0
    s_maxGuess = 9
    
    def __init__(self):
        self._answer = -1
        self._roundCount = 0

        #create the three player objects
        self._larry = player.Player("Larry")
        self._curly = player.Player("Curly")
        self._moe = InteractivePlayer("Moe", self)

    @staticmethod
    def getMinGuess():
        return GuessingGame.s_minGuess

    @staticmethod
    def getMaxGuess():
        return GuessingGame.s_maxGuess

    @staticmethod
    def setGuessRange(minGuess, maxGuess):
        GuessingGame.s_minGuess = minGuess
        GuessingGame.s_maxGuess = maxGuess

    def start(self):
        #pick a number to be guessed between the game's range
        self._answer = random.randint(GuessingGame.getMinGuess(), GuessingGame.getMaxGuess())

        #repeat asking the user to play for each round of the game until someone wins
        winner = None
        while winner == None:
            #increment the round
            self._roundCount += 1

            #ask each player to play and show their guess
            self._larry.play()
            print(f"{self._larry.getName()} guessed {self._larry.getGuess()}")

            self._curly.play()
            print(f"{self._curly.getName()} guessed {self._curly.getGuess()}")
            
            #print(f"The answer is {self._answer}")
            self._moe.playGame(self._answer)
            print(f"{self._moe.getName()} guessed {self._moe.getGuess()}")

            #determine if anybody won
            winner = self.determineWinner()

        #let the user know who won
        print(f"{winner.getName()} won the game in {self._roundCount} rounds with the guess {winner.getGuess()}")

    def determineWinner(self):
        #check each player to see if their guess matched the answer
        if self._larry.getGuess() == self._answer:
            #Larry guessed correctly
            return self._larry        
        elif self._curly.getGuess() == self._answer:
            #Curly guessed correctly
            return self._curly
        elif self._moe.getGuess() == self._answer:
            #Moe guessed correctly
            return self._moe
        else:
            return None