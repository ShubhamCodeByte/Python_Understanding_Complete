# Defining a string 

name = 'Shubham'
name2 = "Singh"
name3 = '''Rajput'''

print ("Name :",name,name2,name3)

# Operation on the string 
# Strings are immutable

# Slicing

sliced_name = name[2:5]
sliced_name_start = name[:5]
sliced_name_end = name[2:]


print("The sliced string name is",sliced_name)
print("The sliced string from start is",sliced_name_start)
print("The sliced string from the end is",sliced_name_end)

# Slicing with the skip values

slice_name_skip = name[1:6:2]
print("skip slice name is",slice_name_skip)




"""
String Methods --> create the new string or object

"""


length = len(name)
count = name.count("h")

print("The name is ending with am or not:", name.endswith("am"))

print(f"The length is {length}, the count of h is {count}.")

Capitalized_name = name.capitalize()
print(f"The capital form of the name is {Capitalized_name}")

find_index = name.find("ub")

replaced_string = name.replace("h","u")

print(f"The index of ub is {find_index}, The replaced new sting is {replaced_string}.")


""" 
escape sequence characters
"""

print("This is for the use of the sequence characters \n new line \t tab \' single quote \\ backslash ")

"""
Output
Name : Shubham Singh Rajput
The sliced string name is ubh
The sliced string from start is Shubh
The sliced string from the end is ubham
skip slice name is hba
The name is ending with am or not: True
The length is 7, the count of h is 2.
The capital form of the name is Shubham
The index of ub is 2, The replaced new sting is Suubuam.
This is for the use of the sequence characters
 new line        tab ' single quate \ backslash
"""