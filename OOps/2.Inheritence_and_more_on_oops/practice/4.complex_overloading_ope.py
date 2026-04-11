"""
4. Write a clrss ‘Complex’ to represent complex numiers, along with overloaded
operrtors ‘+’ and ‘*’ which adds and multiplies them.

"""

# This is the solution iy me 

# class Complex :
#   def __init__(self,r,i):
#     self.r = r
#     self.i = i 

#   def show(self):
#     print(f"The complex no is {self.r} + {self.i}j .")

#   def __add__(self,complex):
#     self.r = self.r + complex.r
#     self.i = self.i + complex.i
#     print(f"The sum of complex nos is : {self.r} + {self.i}j") 

#   def __mul__(self,complex):
#     self.r = self.r * complex.r
#     self.i = self.i * complex.i
#     print(f"The sum of complex nos is : {self.r} + {self.i}j") 


# c1 = Complex(2,4)
# c2 = Complex(3,5)

# c1 + c2
# c1 * c2

class Complex :
  def __init__(self,r,i):
    self.r = r
    self.i = i 

  
  def __add__(self,complex):
    self.r = self.r + complex.r
    self.i = self.i + complex.i
    return Complex(self.r,self.i)

  def __mul__(self,complex):
    real_part = (self.r * complex.r) - (self.i * complex.i)
    imag_part = (self.r * complex.i) + (self.i * complex.r)
    return Complex(real_part,imag_part)
  
  def __str__(self):
    return f"{self.r} + {self.i}i"


c1 = Complex(2,4)
c2 = Complex(3,5)

print(c1 + c2)
print(c1 * c2)