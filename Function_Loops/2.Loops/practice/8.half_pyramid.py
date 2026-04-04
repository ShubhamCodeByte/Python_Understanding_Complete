"""
8. Write a program to print the following star pattern:
*
**
*** for n = 3

"""

n = int(input("Enter no: "))

for i in range(n):
  for j in range(i+1):
    print("*",end = " ")
  else:
    print(" ")
else:
  print("Half Pyramid ...")

"""
*  
* *
* * *
Half Pyramid ...

"""


no = int(input("Enter no: "))

for i in range(1,no+1):
  print("*" * i,end="")
  print()




"""
Enter no: 6
*  
* *
* * *
* * * *
* * * * *
* * * * * *
Half Pyramid ...
Enter no: 6
*
**
***
****
*****
******

"""