"""

4. Write a program to find whether a given username contains less than 10
characters or not.

"""

username = input("Enter the username: ")

length = len(username)

if(length < 10):
  print("Username character less than 10.")
else:
  print("No of characters not less than 10.")