""" Loops """

"""
Theory :

Types : Primarily there are two types of loops in python.
        • while loops
        • for loops


WHILE LOOP

Syntax:
while (condition): # The block keeps executing until the condition is true
#Body of the loop
what it do : In while loops, the condition is checked first. If it evaluates to true, the body of the loop
is executed otherwise not!


"""

i = 0

while(i<50):
  i=i+1
  print(i)


new_list = [2,5,5,6,73,253.55,21]

j = 0

while(j<len(new_list)):
  print(new_list[j])
  j += 1

# I have done a mistake here made the infinite loop not included j += 1 

"""   For Loop   """

""" 
Theory :

for loop : A for loop is used to iterate through a sequence like list, tuple, or string [iterables]


Syntax:
l = [1, 7, 8]
for item in l:
  print(item) # prints 1, 7 and 8

range() : This is the special function to provide the no of iteration to perform
            this will not include the last no written and also automotically include the (0,5) ex


range(start, stop, step_size)


"""

for i in range(10):
  print(i)

"""
0
1
2
3
4
5
6
7
8
9

"""
for j in range(1,11,2):
  print(j)

"""
1
3
5
7
9

"""


# list

list = [2,5,6,72,326,3,2]

for i in list:
  print(i)

# tuple

tuple = (23,35,213,"shubham")

for i in tuple:
  print(i)

# string

strings = "shubham"

for i in strings:
  print(i)



""" for else : will execute after the loop is completed or it will run one time atleast"""

for i in range(2):
  print("Shubham")
else:
  print("done printing ...")


""" break continue and pass """


"""
Theory :

break() : this is used to come out of the iteration 

continue() : this is used to skip the current itteration

pass() : this is used to skip the whole function for the execute or making the channges later

"""


for i in range(1000):
  pass


for i in range(5):
  if(i == 2):
    break
  print("break")


for i in range(5):
  if(i == 2):
    continue
  print(i+1)





