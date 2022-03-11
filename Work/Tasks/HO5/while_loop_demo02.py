total = 0
num = 0

num = (int(input("Enter a whole number between 1 and 100: ")))

total += num

while total < 100:
    num = (int(input("Enter a whole number between 1 and 100: ")))
    total += num

print("Total is {0}".format (total))