weather = input("Is the weather good? ('y' or 'n': ")
if weather == "y":
    restaurant = input("Is there a nice restuarant? ('y' or 'no'): ")
    if restaurant == "y":
        print("Have lunch at the restaurant")
    else:
        print("Stay home and have a sandwich")
else:
    cinema = input("is there a cinema around? ('y' or 'n'): ")
    if cinema == "y":
        tickets = input("Are there movie tickets available? ('y' or 'n'): ")
        if tickets == "y":
            print("Go and see a movie")
        else:
            print("Go shopping")
    else:
        print("Go shopping")
    