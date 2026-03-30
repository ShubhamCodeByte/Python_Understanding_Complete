# 5. Label the program written in problem 4 with comments. 

# importing the os built in module 
import os

# defining the path in for listing the content 
path = '.'

# get the list and store in a variable to list it later 
files_and_folders = os.listdir(path)

# listing all the files in this using the for loop.
for item in files_and_folders:
    print(item) # printing the items in the list or array
    