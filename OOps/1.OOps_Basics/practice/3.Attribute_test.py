"""
3. Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?

"""


class No():
  a: int = 2


a = No()

a.a = 0
print(a.a)

# this will not change the class attribute