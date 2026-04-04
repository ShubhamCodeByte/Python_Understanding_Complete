"""
2. The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

"""


def game():
  highscore = int(input("Enter the score in integer format: "))
  return highscore

def main():
  
  # game
  userHigh = game()

  # read

  # with open("highscore.txt","w+") as f:    # Read-Write Access : Change the mode to r+. This allows the script to read existing data without deleting it immediately.
  with open("highscore.txt","r") as f:    # mistake : this i have opened in the mode of u which is not there + is used for the updation
    check = "0"
    # highscore               # i have not defined it outside the while scope so it was failing. we cannot write like this .
    highscore = 0
    while (check != ""):
      highscore = int(check)
      check = f.readline().strip()
    if(highscore < userHigh):
      with open("highscore.txt","a") as f:
        f.write("\n")           # this will create the new line for that 
        f.write(str(userHigh))         # this is returning integer and we cannot write the thing in the integer format
      print(f"{userHigh} is the new high score.")
    else:
      print(f"{highscore} is the highest score\nYour score: {userHigh}")
    
while(1):
  
  main()
  input("Press enter to continue.")


