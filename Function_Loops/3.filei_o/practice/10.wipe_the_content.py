"""
10. Write a program to wipe out the content of a file using python.

"""

filepath  = "wipe.txt"

with open(filepath,"w") as f:
  f.write("")

print(f"{filepath} content is deleted.")