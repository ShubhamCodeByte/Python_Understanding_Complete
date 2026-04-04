"""
10. Write a program to print multiplication table of n using for loops in reversed
order.

"""

n = 10 

no = int(input("Please enter the no to print : "))

for i in range(10):
  print(n * no)
  n -= 1
else:
  print("completed")


"""
Please enter the no to print :2
20
18
16
14
12
10
8
6
4
2
completed

"""

