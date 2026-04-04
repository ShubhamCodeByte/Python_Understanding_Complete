"""
4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. 


"""

def censorBoard(content): 
  censoredContent = content
  while("donkey" in censoredContent):                 # i have used the content here which i was not changing so it was going into the loop
    censoredContent = censoredContent.replace("donkey" , "######")
    print(censoredContent)
  return censoredContent

def main():
  content = ""
  with open("Donkey.txt","r") as f:
    content = f.read()
    print(content)
  
  censoredContent = censorBoard(content)
  with open("Donkey.txt","w") as f:
    f.write(censoredContent)

  with open("Donkey.txt","r") as f:
    content = f.read()
    print(content)


main()