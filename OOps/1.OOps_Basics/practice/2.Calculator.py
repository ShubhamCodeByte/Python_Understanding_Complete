"""
2. Write a class “Calculator” capable of finding square, cube and square root of a
number.
"""

class Calculator():
  def square(self,no):
    print(f"Suare of {no} is {no**2}.")
  
  def cube(self,no):
    print(f"Cube of {no} is {no**2}.")
  
  @staticmethod
  def squareRoot(no):
    print(f"Square Root of {no} is {no**0.5}.")
  


c = Calculator()

c.square(3)
c.cube(2)
c.squareRoot(4)