"""

5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*

"""


def r_half_pyramid():
  n = int(input("Enter the no: "))

  for i in range(n):
    print("*" * (n-i),end="")
    print()



r_half_pyramid()


"""
Enter the no: 6 
******
*****
****
***
**
*
"""