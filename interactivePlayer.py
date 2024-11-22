"""Defines the interactivePlayer class"""
import player 
import guessingGame as game #NOTE: this import syntax is needed to avoid circular import

class InteractivePlayer(player.Player): # interactivePlayer IS-A Player
    def __init__(self, name, game):
        player.Player.__init__(self, name)

    def playGame(self, answer):
        InRange = True
        # todo: add error handling to ensure user types a number in range
        # todo: provide hints to tell user if guess is too low or too high
        self._guess = int(input(f"Please enter a number from {game.GuessingGame.getMinGuess()} to {game.GuessingGame.getMaxGuess()}: "))
        while InRange == True:
            if (self._guess < answer) and (self._guess >= game.GuessingGame.getMinGuess()) and (self._guess <= game.GuessingGame.getMaxGuess()):
                print("Your guess is too low")
            elif (self._guess > answer) and (self._guess >= game.GuessingGame.getMinGuess()) and (self._guess <= game.GuessingGame.getMaxGuess()):
                print("Your guess is too high")            
            if self._guess < game.GuessingGame.getMinGuess() or self._guess > game.GuessingGame.getMaxGuess():
                self._guess = int(input(f"\033[91m***ERROR***\n***OUT OF BOUNDS INPUT***\033[0m\nPlease enter a number from {game.GuessingGame.getMinGuess()} to {game.GuessingGame.getMaxGuess()}: "))
                InRange = True
            else:
                InRange = False
        return self._guess
            
            
            
            
            
            
            
            