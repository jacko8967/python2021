# asks user for 2 numbers
num1 = float(input("Enter the first decimal number: "))
num2 = float(input("Enter second decimal number: "))

# blank line
print()

# calculation to new variable
answer = num1 - num2

# output answer
print("{0:.3f} - {1:.3f} = {2:.3f}".format(num1, num2, answer))

# new calculation
num1_new = num1 * 3
num2_new = num2 * 3
answer_new = num1_new - num2_new
# blank line
print()

# output new answer
print("Each number multiplied by 3 and the difference between them.")
print("{0:.3f} - {1:.3f} = {2:.3f}".format(num1_new, num2_new, answer_new))