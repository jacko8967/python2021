# Sample06.py
# Programmer: Phil O'Neill
# E-mail: poneill@gordontafe.edu.au
# Date: 20/2/2018

height = 0.0

age = int(input("Enter your age: "))
year = int(input("Enter the current year: "))

yearBorn = year - age
print(age)
print(year)
print(yearBorn)
print()
height = float(input("Enter your height in metres: "))
print()
print("You were born in {0}".format(yearBorn))
print("You are {0} metres tall".format(height))


