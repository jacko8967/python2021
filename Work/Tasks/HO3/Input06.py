# assigns users input into float number
balance1 = float(input("Enter the first bank balance: "))
balance2 = float(input("Enter the second bank balance: "))
balance3 = float(input("Enter the third bank balance: "))
balance4 = float(input("Enter the fourth bank balance: "))

# assigns a variable to the four balances added together to get the total
total = balance1 + balance2 + balance3 + balance4
# uses the total balance to assign a average variable
average = total / 4

# prints users output as single numbers
print(balance1)
print(balance2)
print(balance3)
print(balance4)

# prints blank line
print()

# prints total answer to user
print("Your total bank balance is: ${0:.2f}".format(total))
print("Your average bank balance is: ${0:.2f}".format(average))
