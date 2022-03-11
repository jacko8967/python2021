# Name: Jack Robins
# Contact: jacko8967@gmail.com
# Version: 1.0


# assings the user's input to strings
name = input("Enter your name: ")
reg = input("Enter your car's registration number: ")
color = input("Enter the color of your car: ")

# prints the message to ask users for input
print()

# the function to print each statement on new line
line = "\n"

# currently quoted out: print the users input to statements in an output
"""
print("Your name is: ", name, line, "Your car's registration number is: ", reg, line, "The color of your car is: ", color, sep="")
"""

#currently quoted out: modified code from 01 to print different output
"""
print("{0}", line, "Registration number is {1}", line, "You have a {2} car".format(name, reg, color))
"""

# display users input as output on 3 seperate lines
print("{0}".format(name))
print("You have a {0} car".format(color))
print("Registration number is {0}".format(reg))

# print blank line to seperate output
print()

# combine users input as 1 line
print("{0} has a {1} car, whose registration is {2}".format(name, color, reg))