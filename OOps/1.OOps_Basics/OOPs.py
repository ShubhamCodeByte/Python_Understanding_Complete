""" Object Oriented Programming """

"""
OBJECT ORIENTED PROGRAMMING :

	• oops : Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented programming. 
	• reusability : This concept focuses on using reusable code (DRY Principle).

 CLASS 

	•  blueprint : A class is a blueprint for creating object.
	• ex:- 
	• 
	• Syntax : 
	class Employee: # Class name is written in pascal case
	# Methods & Variables 
	

OBJECT
	• instantiation : An object is an instantiation of a class.
	• memory allocation : Memory is allocated only after object instantiation.
	• abstraction and incapsulation : Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. – Abstractions & Encapsulation!

MODELLING A PROBLEM IN OOPS
	• Class : Noun → Class → Employee 
	• Attributes : Adjective → Attributes → name, age, salary 
	• Methods : Verbs → Methods → getSalary(), increment() 

CLASS ATTRIBUTES
	• only class : An attribute that belongs to the class rather than a particular object.
	• ex: - 

	class Employee:
	company = "Google" # Specific to Each Class
	harry = Employee() # Object Instatiation
	harry.company
	Employee.company = "YouTube" # Changing Class Attribute
	
INSTANCE ATTRIBUTES
	• instance : An attribute that belongs to the Instance (object).
	• ex:- 
	harry.name = "harry"
	harry.salary = "30k" # Adding instance attribute
	• preference :  Instance attributes, take preference over class attributes during assignment & retrieval. 

SELF PARAMETER
	• instance_class : self refers to the instance of the class. It is automatically passed with a function call from an object.
	• ex:- 
	harry.getSalary() # here self is harry
	# equivalent to Employee.getSalary(harry)
	The function getSalary() is defined as:
	class Employee:
	company = "Google"
	def getSalary(self):
	print("Salary is not there")
	
STATIC METHOD 
	• no self parameter  : Sometimes we need a function that does not use the self-parameter. We can define a static method like this:
	• ex:-
	@staticmethod # decorator to mark greet as a static method
	def greet():
	print("Hello user")
	
__INIT__() CONSTRUCTOR 
	• creation of obj : __init__() is a special method which is first run as soon as the object is created.
	• constructor : __init__() method is also known as constructor.
	• arguments : It takes ‘self’ argument and can also take further arguments
	• ex:-
	class Employee:
	def __init__(self, name):
	self.name=name
	def getSalary(self):
	...
	harry = Employee("Harry")
	


"""

class CarManufacturer:
  name = "tata"
  type = "suv"
  # def start(self):                        # if we are not giving the self then it will not run as an instance function from object
  @staticmethod
  def start():                        # if we are not giving the self then it will not run as an instance function from object
    print("car is started.")
  
  def specs(self):
    print(f"Manufacturer Name: {self.name} \nCar type: {self.type} \nStart Status: {self.start()}\n")

# CarManufacturer punch   # this is the mistake i have instatiated ir wrong.
punch = CarManufacturer()

print(punch.name)
print(punch.type)

# punch.start()     # as we are passing nothing but 1 argument is automaticlly sent that is the name of the obj.
# CarManufacturer.start()   # this will work directly not pass any argument automatically

# use the self
punch.start()


# use the @staticmethod without self also it will work.
# punch.start()


# instantiation the variables of the object 
punch.name = "toyota"
print(punch.name)

punch.mode = "electric"
print(f"{punch.name} mode is {punch.mode}")

punch.specs()


# the __init__ constructore() to use.

class Teacher():
  school = "Christ Church"
  salary = "1500"
  classsection = "5 a"
  
  # using init

  # def __init__(self,name = "default",manager):        # this is the wrong way of writing the default
  def __init__(self,manager,name = "default"):         # to make the argument default value we need to keep that in the last 
    print("this is the constructor run on every intatation of the obj")
    print(self.school)
    print(self.salary)
    print(self.classsection)
    print(name)
    print(manager)

  
teach1 = Teacher("Shubham","Radha")
# teach1 = Teacher()       # this will give an error we need to give the arguments of the constructor 




