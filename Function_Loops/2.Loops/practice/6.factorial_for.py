"""

6. Write a program to calculate the factorial of a given number using for loop.

"""

n = int(input("Enter the no : "))

m = 1     # i have made it 0 mistakely which was giving the output 0 

if(n == 0):
  print(1)
else:
  for i in range(n):
    m = m * (i + 1)
  else:
    print(m)



