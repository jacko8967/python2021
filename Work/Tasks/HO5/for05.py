num = int(input("Enter a positive integer: "))

print("Odd integers between 1 and {0}".format(num))
for num in range (1, num, 2):
    print(num)