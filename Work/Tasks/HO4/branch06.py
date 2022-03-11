start_balance = int(input("Enter starting balance: "))

#this is saying if the balance is below $1000 then
#the interest rate will be 5%
if start_balance < 1000:
    interest_rate = 5
#this is saying if the balance is below $10000 then
#the interest rate will be 5.5%
elif start_balance < 10000:
    interest_rate = 5.5
#this is saying if the balance is above 10000
#then the interest rate will be 6%
else:
    interest_rate = 6

#calculations
#calculating the interest earned per starting balance
interest_earned = start_balance * interest_rate / 100

#adding interest earned to original balance
final_balance = start_balance + interest_earned

#outputs
    #starting balance
print("Starting Balance: ${0:,.2f}".format(start_balance))
    #interest rate
print("Interest Rate: {0:,.2f}%".format(interest_rate))
    #interest earned
print("Interest Earned: ${0:,.2f}".format(interest_earned))
    #final balance
print("Final Balance is: ${0:,.2f}".format(final_balance))
