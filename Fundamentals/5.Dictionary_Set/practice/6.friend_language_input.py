"""
6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.

"""

newDict = {}

newDict.update({input("Enter friend name : "): input("Enter favorite language : ")})
newDict.update({input("Enter friend name : "): input("Enter favorite language : ")})
newDict.update({input("Enter friend name : "): input("Enter favorite language : ")})
newDict.update({input("Enter friend name : "): input("Enter favorite language : ")})
newDict.update({input("Enter friend name : "): input("Enter favorite language : ")})

print(newDict)


"""
Output :

Enter friend name : shubham
Enter favorite language : hindi
Enter friend name : harsh
Enter favorite language : english
Enter friend name : abhinava
Enter favorite language : kanada
Enter friend name : naman
Enter favorite language : malyalam
Enter friend name : gautam
Enter favorite language : bhojpuri
{'shubham': 'hindi', 'harsh': 'english', 'abhinava': 'kanada', 'naman': 'malyalam', 'gautam': 'bhojpuri'}


"""