sum = 0

count = 0

while count < 5:
    score=int(input("Enter test score: "))
    sum = sum + score
    count = count + 1
avg = sum / 5
print("Average result = {0}%".format(avg))
