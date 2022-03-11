# Contact: jacko8967@gmail.com
# Date Written: 21.02.2021
# Version: 1.0

# initialise numeric and string variables
unitPrice= 2.95
itemsPurchased = 7
totalPrice = unitPrice * itemsPurchased

# combine and print on seperate lines
print(" Unit Price: $", unitPrice, "\n", "Number bought: ", itemsPurchased, "\n", "Total Price: ""${0:.2f}".format(totalPrice))