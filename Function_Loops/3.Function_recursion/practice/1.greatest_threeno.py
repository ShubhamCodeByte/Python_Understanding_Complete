""" 1. Write a program using functions to find greatest of three numbers """

a = int(input("Enter no:"))
b = int(input("Enter no:"))
c = int(input("Enter no:"))


def greatest(a,b,c):
  if(a>b and a>c):
    greatest = a
  elif(b>a and b>c):
    greatest = b
  else:
    greatest = c
  return greatest


print(greatest(a,b,c))


"""
Enter no:3
Enter no:8
Enter no:1
8
"""