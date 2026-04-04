# 8. Write a python function to print multiplication table of a given number.



def table():
  no = int(input("Enter the no table to print: "))
  m = 10
  for i in range(10):
    print(f"{no} x {i+1} = {(i+1)*no}")
    m -= 1


table()



"""

Enter the no table to print: 4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

"""