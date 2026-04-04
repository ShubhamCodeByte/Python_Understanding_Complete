"""
11. Write a python program to rename a file to “renamed_by_ python.txt.
"""
import os

filePath = ".\\textfiles\\new.txt"    #**Mistake** : i have not made the directory so the error was comming 

content = ""
renamed = ".\\textfiles\\renamed_by_python.txt"
if (os.path.exists(filePath)):
  print("file already created")
else:
  with open(filePath,"w") as f:
    f.write("this is the new file which will be renamed")
    print("file created")
  
with open(filePath) as f:
  content = f.read()
  print("content stored")


if(os.path.exists(renamed)):
  print("already renamed file exitsts in the destination.")
else:
  with open(renamed,"w") as f:
    f.write(content)
    print(f"{filePath} is renamed to {renamed}")
  if(os.path.exists(filePath)):
    os.remove(filePath)
    print("old file is removed")
