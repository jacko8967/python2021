#initialise the list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#initialize the sum variable
sum = 0

#print the range of the list over lines
for x in range(len(number)):
    print (number[x])

#calculates the sum of the list
for i in range(len(number)):
    sum += number[i]

#blank line
print()

#prints the sum of the list
print("The sum of the numbers is:", sum)

#blank line
print()

#prints the range of the list over lines in reverse
for y in range(len(number)):
    number.sort(reverse=True)
    print (number[y])