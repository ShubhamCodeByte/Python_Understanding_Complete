"""
***** Files input and output *****

Theory :

**Volatile** : memory ram when we run the program it will go into the memory and then run and then data is erased

**Non Volatile** : hdd stored into the memory and remain in that for long time.

** Types of files ** : 2
 1. Text File : .txt .c etc
 2. Binary File : .jpg .dat etc

** OPENING A FILE ** : Python has an open() function for opening files. It takes 2 parameters: filename and
mode.

open("this.txt", "r")

** READING A FILE IN PYTHON **

# Open the file in read mode
f = open("this.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
# Close the file
f.close()


** OTHER METHODS TO READ THE FILE. **
We can also use f.readline() function to read one full line at a time.

f.readline() # Read one line from the file.

** MODES OF OPENING A FILE **

r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode

** WRITE FILES IN PYTHON ** 

# Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is nice")
# Close the file
f.close()


** WITH STATEMENT **

The best way to open and close the file automatically is the with statement.

# Open the file in read mode using 'with', which automatically closes the
file
with open("this.txt", "r") as f:
# Read the contents of the file
text = f.read()
# Print the contents
print(text)

"""
# open and read only by default it is in the read mode
# f = open("demo.txt","r")  # we need to open the file in something so that we will be able to use it to read or read line

# text = f.read()

# print(text)

# f.close()


# i am running this in the different folder in the terminal so it is creating the issue so nat able to run as it was not able to get the location of the demo.txt file location 

# writing in the file 
# w = open("demo.txt", "w")
# text = '''
# this is the new things
# which i need to add 
# for the verification of the new
# line by lie reading 
# then we will be exit from here 
# so i need the thing in proper 
# manner
# '''
# w.write(text)  # when i am doing write it erase the previous things and added the new only 
# w.close()

# reading again
# f = open("demo.txt","r") 
# text = f.read()
# print(text)
# f.close()

# reading the line by line

# f = open("demo.txt")
# l1 = f.readline()
# l2 = f.readline()
# l3 = f.readline()
# l4 = f.readline()
# l5 = f.readline()
# l6 = f.readline()
# l7 = f.readline()

# print(l2)
# print(l3)
# print(l5)


# f.close()


def appendText(text,filePath):
  f = open(filePath,"a")
  # f.append(text)   # mistake : there is no attribute called append to write the things we need to make that .write only but the mode is only changed to "a".
  f.write(text)
  f.close()

def readText(filePath):         # Mistake : i have defined the name of the function as the real methods which we cannot take for the user defined function.
  f = open(filePath)
  text = f.read()
  f.close()
  return text

def readline(lineNo,filePath):
  f = open(filePath)

  for i in range(lineNo):
    text = f.readline()
  
  f.close()
  return text

"""
"r+" (Read and Write): Opens the file for both reading and writing, placing the pointer at the beginning of the file.

"a+" (Append and Read): Opens the file for reading and writing, placing the pointer at the end of the file.

"""


def update(text, filePath):
  f = open(filePath,"r+")
  f.write(text)
  f.close


# defination of the text and the file path
text = "This is the append check\n"
filePath = "demo.txt"


r = readText(filePath)
print(r)
appendText(text,filePath)
r = readText(filePath)
print(r)

line2 = readline(2,filePath)
print(line2)

# update
up = "This is to check the update"
update(up,filePath)

r = readText(filePath)
print(r)


with open(filePath) as f:  # i have not written the open in this so cousing the attribute error
  text = f.read()
  print(text)