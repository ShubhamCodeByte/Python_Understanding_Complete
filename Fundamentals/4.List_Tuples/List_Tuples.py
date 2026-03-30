""" List and Tuples """

"""
can store any data type at once 

list indexing start from 0

"""

newList = ["apple","akash","rohan",7,False]


print(newList[0])
print(newList[1])
print(newList[2])
print(newList[3])
print(newList[4])

# this will create the error 
# print(newList[8])

""" List Methods """

l1 = [1,8,7,2,21,15]
print(l1)

# • l1.sort(): updates the list to [1,2,7,8,15,21]
l2 = l1
l2.sort()
print(l2)

# • l1.reverse(): updates the list to [15,21,2,7,8,1]
l3 = l1
l3.reverse()
print(l3)

# • l1.append(8): adds 8 at the end of the list
l4 = l1
l4.append(8)
print(l4)

# • l1.insert(3,8): This will add 8 at 3 index
l5 = l1
l5.insert(3,26)
print(l5)

# • l1.pop(2): Will delete element at index 2 and return its value.
print(l1.pop(2))
print(l1)

# • l1.remove(21): Will remove 21 from the list. 
l6 = l1
l6.remove(21)
print(l6)



""" Tuples """

t1 = (1,45.2,"shubham singh")


# these are imutable 
# t1[1] = 34  # this will fail for tuple
l1[1] = 34 # this will pass for list

""" Methods """

# count = t1.count() this was failing as i have not specified the which thing to count 
count = t1.count(1)  
print(count)

findindex = t1.index("shubham singh")
print(findindex)








"""output:

apple
akash
rohan
7
False
[1, 8, 7, 2, 21, 15]
[1, 2, 7, 8, 15, 21]
[21, 15, 8, 7, 2, 1]
[21, 15, 8, 7, 2, 1, 8]
[21, 15, 8, 26, 7, 2, 1, 8]
8
[21, 15, 26, 7, 2, 1, 8]
[15, 26, 7, 2, 1, 8]
1
2

"""






