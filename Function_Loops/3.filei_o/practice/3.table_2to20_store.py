"""
3. Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.


"""


def tableCreate(no):
  table = ''''''
  for i in range(10):
    table = table + (f"{no} x {i+1} = {no*(i+1)}\n")
  return table

def main():

  for i in range(2,21):
    table = tableCreate(i)
    fileName = f"Table_of_{i}"
    with open(f"./alltables/{fileName}","x") as f:
      f.write(table)
    
main()
