days = int(input("Enter the number of days in a month: "))

if days == 28:
    print("Febuary")
elif days == 29:
    print("Febuary on a Leap Year")
elif days == 30:
    print("April, June, September, November")
elif days == 31:
    print("January, March, May, July, August, October, December")
else:
    print("There is no month with the number of days you have chosen")