"""

7. Write a program to find out whether a given post is talking about “Shubham” or not.

"""

Post = input("Enter the post content : ")

Letter = input("Enter the person name : ")

if(Letter in Post):
  print(f"{Post} is talking about {Letter}")
else:
  print(f"{Post} is not talking about {Letter}")

"""
Output :


Enter the post content : shubham is a very good python devloper
Enter the person name : naman
shubham is a very good python devloper is not talking about naman

Enter the post content : shubham is a very good python devloper
Enter the person name : shubham
shubham is a very good python devloper is talking about shubham

"""