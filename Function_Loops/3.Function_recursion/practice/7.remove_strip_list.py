"""
7. Write a python function to remove a given word from a list ad strip it at the same
time.

"""


def removeStrip(list, toRemove):
  list.remove(toRemove)
  newlist = []
  for i in list:
    j = i.strip()               # previously i made it with the i = i.strip() but as the strings are immutabel so it didnt worked
    newlist.append(j)
  else:
    print(newlist)


list = [" shubham ","add"," the","23  ","34","65"]

removeStrip(list,"34")


