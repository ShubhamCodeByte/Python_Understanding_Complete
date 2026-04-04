"""
5. Repeat program 4 for a list of such words to be censored.

"""

def censorBoard(content,word): 
  censoredContent = content
  while("donkey" in censoredContent):                 # i have used the content here which i was not changing so it was going into the loop
    censoredContent = censoredContent.replace(word , "######")
    print(censoredContent)
  return censoredContent

def main():
  content = ""
  with open("Donkey_list.txt","r") as f:
    content = f.read()
    print((content))
  
  word = "donkey"
  censoredContent = censorBoard(content,word)
  with open("Donkey_list.txt","w") as f:
    f.write((censoredContent))

  with open("Donkey_list.txt","r") as f:
    content = f.read()
    print((content))


main()