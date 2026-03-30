# Primarily these are the following data types in Python:

# 1. Integers
a = 22
# 2. Floating point numbers
b = 32.43
# 3. Strings
name = "shubham"
# 4. Booleans
status = True
# 5. None
content = None

print(a,b,name,status,content)
print(type(a),type(b),type(name),type(status),type(content))


# now performing the type casting

c = int(b)
d = str(a)
new_status = float(status)

print("printing the typecasted things")
print(c,d,new_status)

"""
output:

22 32.43 shubham True None
<class 'int'> <class 'float'> <class 'str'> <class 'bool'> <class 'NoneType'>
printing the typecasted things
32 22 1.0

"""