"""  CONDITIONAL EXPRESSION  """

"""
Theory : 

IF ELSE AND ELIF IN PYTHON

RELATIONAL OPERATORS
Relational Operators are used to evaluate conditions inside the if statements. Some
examples of relational operators are:
==: equals.
> =: greater than/ equal to.
< =: lesser than/ equal to

LOGICAL OPERATORS
In python logical operators operate on conditional statements. For Example:
• and – true if both operands are true else false.
• or – true if at least one operand is true or else false.
• not – inverts true to false & false to true.


ELIF CLAUSE

IMPORTANT NOTES:
1. There can be any number of elif statements.
2. Last else is executed only if all the conditions inside elifs fail


in : this is use item is present in 
not in : this is used to check the the prescence is not there in the object

"""

""" Practical """

# Write a program to print yes when the age entered by the user is greater
# than or equal to 18.

age = int(input("Enter age : "))

if(age >= 18):
  print("Can Vote")

elif(age < 0):
  print("The no is negative")

elif(age < 18):
  print("Not eligible for vote.")

else:
  print("Enter a valid no")