"""
8. Write a program to make a copy of a text file “this. txt”

"""


source = "this.txt"
destination = "copy_this.txt"
sourceContent = ""
with open(source,"r") as f:
  sourceContent = f.read()

with open(destination,"x") as f:
  f.write(sourceContent)

print(f"copy of {source} is generated as {destination}")