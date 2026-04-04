# 4. Write a recursive function to calculate the sum of first n natural numbers


def sum(n):
  if(n == 1):
    return 1
  else:
    return sum(n-1) + n

no = int(input("Enter No: "))

print(sum(no))

