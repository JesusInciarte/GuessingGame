"""Represents the guessing game application responsible for user interaction and for creating
and running the guessin game.
"""
from guessingGame import GuessingGame
from execptions import OperationCancelled
from execptions import InvalidRange

class Application:
   def run(self):
      #create the game
      game = GuessingGame()
      
      #ask user to determine the guess range
      userMinGuess, userMaxGuess = self.askUserForGuessRange()
      GuessingGame.setGuessRange(userMinGuess, userMaxGuess)

      #repeat playing the game for as long as the user wants to play
      playAgain = True
      while playAgain:      
         #start the game 
         game.start()

         #check if the user wants to play again
         playAgain = self.checkPlayAgain()

   def askUserForGuessRange(self):
      while True:
         try:
            userMinGuessInput = input("Please enter the minimum guess for players: [Press ENTER to cancel]")
            if len(userMinGuessInput) == 0:
               raise OperationCancelled("Setting the minimum guess was canceled by the user")
            
            userMaxGuessInput = input("Please enter the maximum guess for players: [Press ENTER to cancel]")
            if len(userMaxGuessInput) == 0:
               raise OperationCancelled("Setting the maximum guess was canceled by the user")
            
            userMinGuess = int(userMinGuessInput)
            userMaxGuess = int(userMaxGuessInput)
            
            if userMinGuess > userMaxGuess:
               raise InvalidRange("The minimum guess is greater than the maximum guess")
                        
            return (userMinGuess, userMaxGuess)
         except OperationCancelled as ex:
            print(f"\033[91m{ex}\033[\n\033[93mThe game will continue with the default range of 0 to 9\033[0m")
            return (0, 9)
         
         except InvalidRange as ex:
            print(f"\033[91m{ex}\033[93m\nYour initial values have been inverse.\033[0m")
            tempGuess = userMinGuess
            userMinGuess = userMaxGuess
            userMaxGuess = tempGuess      
            # return correct range to caller      
            return (userMinGuess, userMaxGuess)
         
         except ValueError as ex:
            print(f"\033[91mAn unexpected error has occurred. Please enter valid numbers only.\nError Message: {ex}\033[0m")

   def checkPlayAgain(self):
      """Asks the user if they want to play again and returns true/false depending on the answer"""
      #ask the user if the want to play the game
      playAgainInput = input("Would you like to play again? [y/n]: ")

      #determine if they do or not and return True/False accordingly
      return playAgainInput.upper() == "Y"
      # if playAgainInput.upper() == "Y":
      #    return True
      # else:
      #    return False

       