# Contact: jacko8967@gmail.com
# Date Written: 21.02.2021
# Version: 1.0

# initialise numeric and string variables
name = "Jack Robins"
wageRate = 10
hoursWorked = 34

# calculate output
wage = wageRate * hoursWorked

# display output on seperate prints
print("Wages for", name)
print("Hourly Rate:", "${0:.2f}".format(wageRate))
print("Hours Worked:", hoursWorked)
print("Weekly Wage:", "${0:.2f}".format(wage))

# print blank space
print()

# display seperate lines output on same print
print(" Wages for", name, "\n", "Hourly Rate:", "${0:.2f}".format(wageRate), "\n", "Hours Worked:", hoursWorked, "\n", "Weekly Wage:", "${0:.2f}".format(wage))