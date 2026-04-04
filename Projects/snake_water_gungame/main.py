"""

PROJECT 1: SNAKE, WATER, GUN GAME
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.



"""

"""
# Game Rules: Snake, Water, Gun

* **Snake** : The **Snake** drinks the **Water**, securing a win.
* **Water** : The **Water** douses the **Gun**, claiming the victory.
* **Gun** : The **Gun** shoots the **Snake**, emerging victorious.
* **Draw** : If both **players** make the same **choice**, the round is a tie.
* **Gameplay** : Both **participants** make their **selection** simultaneously.
* **Victory** : The **player** with the most **wins** takes the overall match.
"""

def inputRes():
  No = (input("Its your turn :- \n" \
  "Select your option:- \n" \
  "1.Snake \n" \
  "2.Water \n" \
  "3.Gun \n" \
  "Please select your option: "))

  if(No == "1" or No == "2" or No == "3"):
    RespNo = int(No)
  else:
    print("Error : Please select the option as 1,2,3")
    No = None
    # inputRes()        # **Mistake**: i have used this as a recursion so this is executing from here only 
    return inputRes()

  options = ["Snake","Water","Gun"]
  if(RespNo >= 1 or RespNo <= 3):
    response = options[RespNo - 1]
  else: 
    print("Error : Please select the option as 1,2,3")
    inputRes()
  return response


def computer():
  import random
  
  options = ["Snake","Water","Gun"]
  print("Thinking ....")
  comp_choice = random.choice(options)   # **Mistake** : i have taken the function as the choose .

  return comp_choice


# for this we can use the dictionary also to make it simpler 
# def winnerSelect(response,comp_choice):
#   print("Comparing .....")

#   if(response == comp_choice):
#     print(f"Computer : {comp_choice} \nYour option : {response} \nDraw Match......")
#   elif(response == "Snake" and comp_choice == "Water"):
#     print(f"Computer : {comp_choice} \nYour option : {response} \nThe **Snake** drinks the **Water**, You win ....")
#   elif(response == "Water" and comp_choice == "Gun"):
#     print(f"Computer : {comp_choice} \nYour option : {response} \nThe **Water** douses the **Gun**, You win ....")
#   elif(response == "Gun" and comp_choice == "Snake"):
#     print(f"Computer : {comp_choice} \nYour option : {response} \nThe **Gun** shoots the **Snake**, You win ....")
#   elif(comp_choice == "Snake" and response == "Water"):
#     print(f"Computer : {comp_choice} \nYour option : {response} \nThe **Snake** drinks the **Water**, You loses ....")
#   elif(comp_choice == "Water" and response == "Gun"):
#     print(f"Computer : {comp_choice} \nYour option : {response} \nThe **Water** douses the **Gun**, You loses ....")
#   elif(comp_choice == "Gun" and response == "Snake"):
#     print(f"Computer : {comp_choice} \nYour option : {response} \nThe **Gun** shoots the **Snake**, You loses ....")
#   else:
#     print("Not able to compute ERROR Occured")


# Alternative function using the dictionary
def winnerSelect(userResp,compResp):
  print("Comparing ....")
  winTable = {
    "Snake": "Water",
    "Water": "Gun",
    "Gun": "Snake",
  }
 
  if(winTable[userResp] == compResp):      # mistake i was calling the dictionary with . and () which is wrong.
    print(f"Computer : {compResp} \nYour option : {userResp} \nYou won {userResp} beats {compResp}.")
  elif(winTable[compResp] == userResp):
    print(f"Computer : {compResp} \nYour option : {userResp} \nYou looses {compResp} beats {userResp}.")
  else:
    print(f"Computer : {compResp} \nYour option : {userResp} \nDraw Match......")
# Display the dashboard

def dashboard():
  print(">>> Welcome to Snake Water Game <<<")

def main():
  # Starting the main fumction 
  dashboard()

  # Input the response   # ** Mistake ** : I have not added the variable to store the output of the function ..
  response = inputRes()     

  # Commputer Response generation:
  comp_response = computer()    # ** Mistake ** : I have not added the where the output will be stored ...

  # winner selection and dispaying the result
  winnerSelect(response,comp_response)    # **Mistake ** : I have not selected the arguments for this ..

while(1):
  main()
  exit = input("Press Enter to continue and exit to close the game: ")
  if(exit == "exit"):                          # this i introduced to make the function more dynamic
    break




