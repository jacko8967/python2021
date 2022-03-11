number = int(input("Enter the number 1, 2, 3, or 4: "))

if number == 1:
    print("ONE")
if number == 2:
    print("TWO")
if number == 3:
    print("THREE")
if number == 4:
    print("FOUR")
else:
    print("ERROR - You must enter a number between 1 and 4")
print("You entered {0}".format(number))
print("Please run the program again!")