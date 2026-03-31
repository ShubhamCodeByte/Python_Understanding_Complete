"""

5. Write a program which finds out whether a given name is present in a list or not.

"""

list = ["shubham","gautam","naman","abhinav",]

check = input("Please enter the name to search: ")

if(check in list):
  print(f"{check} is present in the list")
else:
  print(f"{check} is not present in the list.")




"""
Output :

Please enter the name to search: nikhil
nikhil is not present in the list.

Please enter the name to search: shubham
shubham is present in the list

"""