"""
__str__() method to print the vector as follows:
 7i + 8j +10k
Assume vector of dimension 3 for this problem.

"""


class ThreeDVector:
  def __init__(self,i,j,k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

b = ThreeDVector(1,2,3)

print(f"b vectore is : {b}")

