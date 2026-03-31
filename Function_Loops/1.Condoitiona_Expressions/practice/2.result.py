"""
2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.

"""

maths = int(input("Enter maths marks: "))
english = int(input("Enter english marks: "))
science = int(input("Enter science marks: "))

total = maths + english + science

Percentage = total / 300 * 100

print(total)
print(Percentage)

if(Percentage < 40):
  print("Fail Overall Percent Less than 40%.")
elif((maths or english or science) < 33):
  print("Individual subject marks less than 33 so Fail.")
else:
  print(f"Pass with {Percentage} % .")


"""
Output :

Enter maths marks: 56
Enter english marks: 78
Enter science marks: 98
232
77.33333333333333
Pass with 77.33333333333333 % .

Enter maths marks: 23
Enter english marks: 45
Enter science marks: 78
146
48.66666666666667
Individual subject marks less than 33 so Fail.

"""
