sum = 0

for num in range (5):
    num = int(input("Enter test score: "))
    sum = sum + num
avg = sum / 5
print("Average result {0:.1f}".format(avg))