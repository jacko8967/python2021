# Name: Jack Robins
# Contact: jacko8967@gmail.com
# Version: 1.0


# assings the user's input to strings
name = input("Enter your name: ")
reg = input("Enter your car's registration number: ")
carColor = input("Enter the color of your car: ")

# prints the message to ask users for input
print()

# the function to print each statement on new line
line = "\n"

# print the users input to statements in an output
print("Your name is: ", name, line, "Your car's registration number is: ", reg, line, "The color of your car is: ", carColor, sep="")