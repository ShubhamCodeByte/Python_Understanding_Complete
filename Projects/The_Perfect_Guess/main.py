"""
PROJECT 2 – THE PERFECT GUESS


We are going to write a program that generates a random number and asks the user to
guess it.


If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module.

"""

import random 


# this will create the random no 
class createRandom:
  randomNo = random.randint(0,100)


class GameUI:
  gameName = "The Perfect Guess"

  def __init__(self):
    print(f"--------------------Welcome to the {self.gameName}---------------------")
    print()
    print("-------------------Plese guess the no between 0 to 100-------------------")
    print()
    




class takingInput :
  def userInput(self):
    return int(input("Please guess the no : "))  
  
""" Mistake : i have taken the input but it will give the str right but we need int """


class MainLogic :
  def __init__(self):
    self.noOfGuessNo = 1

  @property
  def noOfGuess(self):
    return self.noOfGuessNo
  
  @noOfGuess.setter
  def noOfGuess(self,no):
    self.noOfGuessNo = no

  # noOfGuess = 1

  def compareResult(self,computer,user):
    if(computer < user):
      print("Guess Lesser No.")
      self.noOfGuess += 1
    elif(computer > user):
      print("Guess Higher No.")
      self.noOfGuess += 1
    elif(computer == user):
      print(f"Computer No : {computer} \nYour No : {user}\nTotal Gueesses : {self.noOfGuess}")


class GameLogic(GameUI,createRandom,takingInput,MainLogic):
  def __init__(self):
    # super().__init__()  # this will call only the first parent class init to get specific or other class we need to call it individually 
    GameUI.__init__(self)  # self is required in this 
    MainLogic.__init__(self)

game = GameLogic()
computer = game.randomNo
user = game.userInput()
if(computer == user):
  game.compareResult(computer,user)
else:
  while(computer != user):
    game.compareResult(computer,user)
    user = game.userInput()
  else:
    game.compareResult(computer,user)







