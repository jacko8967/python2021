# asks user for 2 numbers
num1 = float(input("Enter the first decimal number: "))
num2 = float(input("Enter second decimal number: "))

# blank line
print()

# calculation to new variable
answer = num1 + num2

# output answer
print("{0:.2f} + {1:.2f} = {2:.2f}".format(num1, num2, answer))

# new calculation
num1_new = num1 + 12.53
num2_new = num2 + 12.53
answer_new = num1_new + num2_new

# blank line
print()

# output new answer
print("12.53 added to both numbers.")
print("{0:.2f} + {1:.2f} = {2:.2f}".format(num1_new, num2_new, answer_new))