"""
Following are some common operators in python:
1. Arithmetic operators: +, -, *, / etc.
2. Assignment operators: =, +=, -= etc.
3. Comparison operators: ==, >, >=, <, != etc.
4. Logical operators: and, or, not.
"""


a = 2
b = 4
c = 1

print("Arithmetic operators")
print(a+b,a-b,a*b,a/b,a//b,a**b,b%a)

print("Assignment Operators")
# print(c=b,c += b,c *= b,c /= b,c //= b,c **= b,c %= a)   this caused the error in the code as these are cmpound
# statement must be placed on the seperate line 
# print(c=b) ---> we cannot assign like this and print we need to do it individually
c += b
print(c)


print("Comparision Operators")
print(a > b,a < b,a >= b,a / b,a <= b,a == b,b != a)


print("Logical Operators")
print(a and b,a or b, not b)




"""
Output :
Arithmetic operators
6 -2 8 0.5 0 16 0
Assignment Operators
5
Comparision Operators
False True False 0.5 True False True
Logical Operators
4 2 False

"""