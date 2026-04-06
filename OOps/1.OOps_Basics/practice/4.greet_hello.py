"""
4. Add a static method in problem 2, to greet the user with hello.

"""

class Calculator():
  def square(self,no):
    print(f"Suare of {no} is {no**2}.")
  
  def cube(self,no):
    print(f"Cube of {no} is {no**2}.")
  
  @staticmethod
  def squareRoot(no):
    print(f"Square Root of {no} is {no**0.5}.")

  @staticmethod
  def greet():
    print("Welcome to the calculator.")
    no = int(input("Please enter the no : "))
    return no 
  


c = Calculator()


no = c.greet()
c.square(no)
c.cube(no)
c.squareRoot(no)

