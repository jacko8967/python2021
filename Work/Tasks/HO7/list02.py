days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
months = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31]
balance = [106.82, 56.82, 87.67, 104.56, 57.82, 256.76]

print("First and last days:", days[0], "and", days[6])
print("First, fifth, and last months: ", months[0], ",", months[4], ",", months[11])
print("First, third, and last balance: ", balance[0], ",", balance[2], ",", balance[5])

print()

print("days has", len(days), "elements")
print("months has", len(months), "elements")
print("balance has", len(balance), "elements")