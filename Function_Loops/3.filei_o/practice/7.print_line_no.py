"""
7. Write a program to find out the line number where python is present from ques 6.

"""
filePath = "log_python.txt"
# filePath = "log_no_python.txt"


with open(filePath,"r") as f:
  content = f.readline()
  lineNo = 0
  while(content != ""):
    if ("python" in content):
      lineNo +=1
      print(f"Python is present in line: {lineNo}")
      content = f.readline()
    else:
      # print("Python is not present")
      lineNo += 1
      content = f.readline()
  else:
    with open(filePath,"r") as f:
      content = f.read()
      if ("python" in content):
        print("Python is present")
      else:
        print("Python is not present")



# with open("log_python.txt","r") as f:
#   content = f.readline()
#   lineNo = 0
#   while(content == ""):
#     if ("python" in content):
#       lineNo +=1
#       print(f"Python is present in line: {lineNo}")
#       content = f.readline()
#     else:
#       # print("Python is not present")
#       lineNo += 1
#       content = f.readline()