# ask users for input
state = input("Enter a state: ")
town1 = input("Enter a town in that state: ")
town2 = input("Enter another town from that state: ")
town3 = input("Last time, enter yet another town: ")

# asks users for their input to assign values
print()

# assigns new line variable
line = "\n"

# prints users variables over multiple lines
print("Your state: ",state)
print("Your first town: ",town1)
print("Your second town: ",town2)
print("Your third town: ",town3)

# prints the output over a single line
print("{2}, {1}, and {3} are all towns in {0}".format(state, town2, town3, town1))