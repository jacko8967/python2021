#Program: Lightbulb Troubleshooter
#Author: Jack Robins
#Date Created: 1.4.21

#specifies wanted answers to the questions
print("Please answer all of the following questions in 'yes' or 'no'")

#asks if light is on
lightON = input("Is the light on?: ")
#if light is NOT on, asks if electricity is on
if lightON.lower != "yes":
    elecON = input("Is the electricity turned off?: ")
    #if electricity is NOT on, asks if lightglobe has blown
    if elecON.lower != "yes":
        globeBlown = input("Has the lightglobe blown?: ")
        #if globe has NOT blown, asks if fuse is blown
        if globeBlown.lower != "yes":
            fuseBlown = input("Has the fuse blown?: ")
            #if fuse has NOT blown, calls electrician
            if fuseBlown.lower != "yes":
                print("Call an electrician.")
            #if fuse HAS blown, ends program
            else:
                print("Replace the fuse.")
        #if globe HAS blown, ends program
        else:
            print("Replace the light globe.")
    #if electricity IS on, ends program
    else:
        print("Turn on electricity at the switch.")
#if light IS on, ends program
else:
    print("Good, all is okay.")
print("Thank you for using the troubleshooter.")