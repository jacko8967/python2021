age = int(input("Enter age:"))
if age > 65:
    print("Elderly")
elif age > 35:
    print("Middle Aged")
elif age > 17:
    print("Adult")
elif age > 12:
    print("Teenager")
else:
    print("Child")