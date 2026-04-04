"""
2. Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

"""

l = ["Harry", "Soham", "Sachin", "Rahul"]

# m = l                 # not required
# m.startswith("S")     # this i have done mistake this is not the method of list 

for i in l:
  if(i.startswith("S")):
    print(f"Hello {i}.")
    
"""

Hello Soham.
Hello Sachin.

"""
