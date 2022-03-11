# asks user for 2 numbers
num1 = int(input("Enter the first number: ")) #input 12
num2 = int(input("Enter second number: ")) #input 5

# blank line
print()

# calculation to new variable
answer = num1 / num2 #expected answer = 2
answer2 = num1 % num2 #xepected answer = 2

# output answer
print("{0} / {1} = {2:.0f}".format(num1, num2, answer))
print("{0} % {1} = {2}".format(num1, num2, answer2))