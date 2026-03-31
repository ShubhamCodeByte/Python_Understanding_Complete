"""3. Check that a tuple type cannot be changed in python."""

tuple1 = (34,"shubham")

# trying to change the type of the tuple 

list1 = list(tuple1)

print(type(tuple1))
print(type(list1))

# check immutability this will cause the error

# tuple[1] = "singh"



