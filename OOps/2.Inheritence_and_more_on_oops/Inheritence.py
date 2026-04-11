



""" Practice                     """

# inheritence 

class Employee():
  a = 1  

class Devloper(Employee):
  b = 3

shubham = Employee()

print (shubham.a)
# print (shubham.b)  # this will not run as it is not in the Employee() class 

shubh = Devloper() 

print (shubh.a)    # this will run when the inheritence is done 
print (shubh.b) 



# multiple inheritence 

class Employee2():
  c = 4


class Devloper2(Employee,Employee2):
  d = 5


multiple = Devloper2()

print("Multiple Inheritance")
print(multiple.a)
print(multiple.d)
print(multiple.c)

# multilevel inheritence 

class devloper3(Devloper2):
  e = 6


multilevel = devloper3()

print("Multilevel Inheritance")

print(multilevel.a)
print(multilevel.c)
print(multilevel.d)
print(multilevel.e)


# super() 

class E1():
  def __init__(self):
    print("this is the constructor of class e1")

class E2():
  def __init__(self):
    print("this is the constructor of class e2")

class E3(E2):
  def __init__(self):
    super().__init__()
    print("this is the constructor of class e3")




a = E1()

b = E2()

c = E3()


# class methods 

class Calculation () :
  no = 2
  @classmethod
  def numberPrint(self):
    print(f"The number is {self.no}")

  # this is the normal function   
  def numberNormalPrint(self):
    print(f"The number is {self.no}")


c = Calculation()

c.no = 4
c.numberPrint()
c.numberNormalPrint()



# make the property first name and the last name and set it using the @property and then .setter thing 

class NameStore () :

  @property
  def name(self):
    return self.ename
  
  @name.setter
  def name(self,value):
    self.ename = value 


n = NameStore()

# n.name("Shubham")  # this is not the function we have made it property so we need to take it as a variable
n.name = "Shubham"
print(n.name)




class NameSplitStore () :

  @property
  def name(self):
    return f"{self.fname} {self.lname}"
  
  @name.setter
  def name(self,value):
    self.fname = value.split(" ")[0] 
    self.lname = value.split(" ")[1] 


n = NameStore()

# n.name("Shubham")  # this is not the function we have made it property so we need to take it as a variable
n.name = "Shubham Singh"
print(n.name)





# ooperator overloading 

class operatorOverloading():
  def __init__(self,n):
    self.n = n

  def __add__(self,num):
    return self.n + num.n 


a = operatorOverloading(1)
b = operatorOverloading(2)

print(a+b)
