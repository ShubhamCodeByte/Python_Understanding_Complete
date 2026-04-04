# 2. Write a python program using function to convert Celsius to Fahrenheit.


def ConvertionC_F(c):
  f = (c * 1.8) + 32
  print(f"The coresponding Ferenhite is {f}")



celsius = float(input("Enter Celsius: "))

ConvertionC_F(celsius)



"""
Enter Celsius: 20.45
The coresponding Ferenhite is 68.81
"""
