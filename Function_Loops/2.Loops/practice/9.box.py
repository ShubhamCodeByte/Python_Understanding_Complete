"""
9. Write a program to print the following star pattern.
* * *
*   * for n = 3
* * * 

"""

n = int(input("Enter no: "))

# this will fail for the no other than 3

for i in range(n-1):
  for j in range(n):
    if(j == (2**(n-(i+1))-1)):
      print(" ",end=" ")
    else:
      print("*",end=" ")
  else:
    print("")
else:
  for i in range(n):
    print("*",end=" ")
  else:
    print("\nBox Made ...")



"""
* * * 
*   *
* * *
Box Made ...

"""

"""  Other good solution  """

no = int(input("Enter no: "))

for i in range(1,no+1):
  if(i == 1 or i == no):
    print("*" * no,end="")
    print()
  else:
    print("*",end="")
    print(" " * (no-2),end="")
    print("*",end="")
    print()
    
