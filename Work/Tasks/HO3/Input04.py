#assign variables based on user's input
 
month1 = input("Enter a month: ")
month2 = input("Enter a second month: ")
month3 = input("Enter a third month: ")

# asks for users input
print()

# prints users input as displayed
print("The first month you have chosen is {0}, the second month you have chosen is {1}, the third month you have chosen is {2}".format(month1, month2, month3))

# prints 2 blank lines to seperate output
print()
print()

# prints months in entry order
print("The months you have chosen in ""entry"" order are {0}, {1}, and {2}".format(month1, month2, month3))
# prints months in reverse order
print("The months you have chosen in ""reverse"" order are {2}, {1}, and {0}".format(month1, month2, month3))
# prints months in Pulp Fiction order
print("The months you have chosen in" """ "Pulp Fiction" """ "order are {1}, {0}, and {2}".format(month1, month2, month3))