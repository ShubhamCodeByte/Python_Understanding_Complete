"""
6. Write a program to mine a log file and find out whether it contains ‘python’.

"""
with open("log_python.txt","r") as f:
  content = f.read()
  if ("python" in content):
    print("Python is present")
  else:
    print("Python is not present")


with open("log_no_python.txt","r") as f:
  content = f.read()
  if ("python" in content):
    print("Python is present")
  else:
    print("Python is not present")