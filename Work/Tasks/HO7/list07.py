#initalizes empty list
names = []

#sets length of list to 5
length = 5

#populates the list via user input
for x in range(length):
    name = str(input("Enter name: "))
    names.append(name)

#print the range of the list over lines
for i in range(len(names)):
    print (names[i])

print()


print(names[0])
print(names[2])
print(names[4])