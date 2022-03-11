# assigns users input into current bank balance
old_balance = float(input("Enter opening balance: "))
interest_rate = float(input("Enter interest rate: "))

# calculations and assign to new variables
interest = interest_rate / 100
new_balance = old_balance + old_balance * interest


# new line
print()

# print old balance
print("Old Balance: {0:,.2f}".format(old_balance))
print("Interest Rate: {0}%".format(interest_rate))
print("Interest: ${0:.2f}".format(interest))

# print blank line
print()

# print new bank balance
print("New Balance: ${0:,.2f}".format(new_balance))
