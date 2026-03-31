"""
2. Write a program to input eight numbers from the user and display all the unique
numbers (once).

"""


no = set()

no.add(int(input("Enter no : ")))
no.add(int(input("Enter no : ")))
no.add(int(input("Enter no : ")))
no.add(int(input("Enter no : ")))
no.add(int(input("Enter no : ")))
no.add(int(input("Enter no : ")))
no.add(int(input("Enter no : ")))
no.add(int(input("Enter no : ")))

print(no)


"""
Output : 
Enter no : 3
Enter no : 2
Enter no : 6
Enter no : 6
Enter no : 3
Enter no : 2
Enter no : 3
Enter no : 4
{2, 3, 4, 6}

"""