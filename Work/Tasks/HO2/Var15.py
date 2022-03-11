# initialise numeric values as strings
pounds = 2
shillings = 4
pennies = 6
totalPennies = 0

# calculate working out total pennies
               # 4 times 12    2 times 20  then add 6
totalPennies = shillings * 12 + pounds * 20 + pennies

# print the function after calculations
      #writes out the message inside the print function using formatting of {} brackets 
print ("{0} Pounds + {1} shillings + {2} pennies = {3} Pennies".format(pounds, shillings, pennies, totalPennies))