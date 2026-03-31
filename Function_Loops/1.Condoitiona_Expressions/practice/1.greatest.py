"""

1. Write a program to find the greatest of four numbers entered by the user.

"""


a = int(input("Enter no: "))
b = int(input("Enter no: "))
c = int(input("Enter no: "))
d = int(input("Enter no: "))


if(a>b and a>c and a>d):
  greatest = a
elif(b>a and b>c and b>d):
  greatest = b
elif(c>a and c>b and c>d):
  greatest = c
else:
  greatest = d

print(greatest)

"""
Output :

Enter no: 45
Enter no: 345
Enter no: 4
Enter no: 2
345
"""