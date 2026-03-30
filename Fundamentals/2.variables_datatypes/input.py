# This is used to input the thing from the user 


a = input("input no ")
print ("type of a:",type(a))
print ("a = ",a)

b = int(input("Please input the no or float it will be automatically converted")) #we cannot convert the float to the int 
print ("type of b:",type(b))
print ("b = ",b)


"""
Output :

input no 37.6 
type of a: <class 'str'>
a =  37.6
Please input the no or float it will be automatically converted43
type of b: <class 'int'>
b =  43

"""