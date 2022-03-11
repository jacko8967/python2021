# asks user for 2 numbers
num1 = int(input("Enter first whole number: "))
num2 = int(input("Enter second whole number: "))

# blank line
print()

# calculation to new variable
answer = num1 + num2

# output answer
print("{0} + {1} = {2}".format(num1, num2, answer))

# new calculation
num1_new = num1 + 10
num2_new = num2 + 20
answer_new = num1_new + num2_new

# blank line
print()

# output new answer
print("10 added to the first\nand 20 the the second number.")
print("{0} + {1} = {2}".format(num1_new, num2_new, answer_new))