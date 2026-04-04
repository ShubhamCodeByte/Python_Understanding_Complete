""" Function and Recursion  """

"""   
Theory :

Functions : A function is a group of statements performing a specific task.

Syntax : 

Function Defination : 

def FunctionName():
  print("welcome to python")


Function Call :

FunctionName()

Types : 
  1. Built in functions : ex:- len(), print(), range().
  2. User defined functions : ex:- func1() etc.

Arguments : A function can accept some value it can work with. We can put these values in the
parentheses.

ex:-

def add(a,b):
  print(a*b)

add(3,6)

Default Parameter Value : We can have a value as default as default argument in a function


ex:-

def greet(name="Shubham"):
  print(name)

greet("Harsh")

greet()


'''    RECURSION    '''

RECURSION : Recursion is a function which calls itself.
            It is used to directly use a mathematical formula as function.

Ex:-

def factorial(n):
  if(n == 0 or n == 1):
    return 1
  else:
    fact = n*factorial(n-1)
  return fact

  

 """


def FunctionName():
  print("welcome to python")

FunctionName()



def add(a,b):
  print(a*b)

add(3,6)


def greet(name="Shubham"):
  print(name)

greet("Harsh")

greet()




def factorial(n):
  if(n == 0 or n == 1):
    return 1
  else:
    fact = n*factorial(n-1)
  return fact


print(factorial(4))