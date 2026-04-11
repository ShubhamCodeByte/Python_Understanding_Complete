"""
3. Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
which changes the value of increment based on the salary.

"""


class Employee :
  salary = 15000
  increment = 20

  @property
  def salaryAfterIncrement(self):
    return (self.salary + (self.salary * (self.increment / 100)))
  
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self,salary):
    self.increment = ((salary/self.salary) -1) * 100 



a = Employee()

print(f"Salary : {a.salary}")

print(a.salaryAfterIncrement)

a.salaryAfterIncrement = 25000

print(f"Increment : {a.increment}")



"""
Salary : 15000
18000.0
Increment : 66.66666666666667


"""