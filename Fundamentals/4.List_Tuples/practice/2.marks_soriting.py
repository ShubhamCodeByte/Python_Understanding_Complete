""" 2. Write a program to accept marks of 6 students and display them in a sorted
manner.

"""

marks = []

marks.append(int(input("enter the marks : ")))
marks.append(int(input("enter the marks : ")))
marks.append(int(input("enter the marks : ")))
marks.append(int(input("enter the marks : ")))
marks.append(int(input("enter the marks : ")))


marks.sort()
print(marks)


"""
Output:

enter the marks : 54
enter the marks : 3
enter the marks : 645
enter the marks : 75
enter the marks : 78976
[3, 54, 75, 645, 78976]

"""