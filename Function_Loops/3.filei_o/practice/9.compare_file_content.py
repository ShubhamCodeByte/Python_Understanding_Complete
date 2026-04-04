"""
9. Write a program to find out whether a file is identical & matches the content of
another file.

"""

source1 = "copy_this.txt"
# source2 = "this.txt"
source2 = "Donkey.txt"
content_source1 = ""
content_source2 = ""

# reading source 1
with open(source1,"r") as f:
  content_source1 = f.read()

# reading source 2
with open(source2,"r") as f:
  content_source2 = f.read()

if (content_source1 == content_source2):
  print(f"{source1} and {source2} are identical")
else:
  print(f"{source1} and {source2} are not identical")
