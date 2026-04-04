"""
7. Write a program to print the following star pattern.
 *
***
***** for n = 3

"""
# for odd no this is working and for even no this is not working and creating " " in between
n = int(input("Enter no: "))

for i in range(n):
  for j in range(i+n):           # this i have written --> for j in range(i+3): --> non dynamic
    if(j < (n-(i+1))):
      print(" ",end = "")        # end = " " --> create the space in between
    else:  
      print("*",end = "")
  else:
    print("")
else:
  print("Figure Pyramid Created...")

"""
    *  
  * * *
* * * * *
Figure Pyramid Created...

Enter no: 4
   
  **
 ****
******
Figure Pyramid Created...

"""

""" More simpler solution """


no = int(input("Enter no : "))

for i in range(1,no+1):
  print(" "*(no - i),end="")
  print("*"*(2*(i-1)+1),end="")
  print("")




"""
Enter no: 6
     *
    ***
   *****
  *******
 *********
***********
Figure Pyramid Created...
Enter no : 6
     *
    ***
   *****
  *******
 *********
***********

"""