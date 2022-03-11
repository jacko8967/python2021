gross_balance = int(input("Enter your gross income: "))

#this is saying if the balance is below $7999.99
#the tax rate will be 0%
if gross_balance <= 7999.99:
    tax_rate = 0
#this is saying if the balance is below $14999.99
#the tax rate will be 25%
elif gross_balance <= 14999.99:
    tax_rate = 25
#this is saying if the balance is below $24999.99
#the tax rate will be 35%
elif gross_balance <= 24999.99:
    tax_rate = 35
#this is saying if the balance is below $49999.99
#the tax rate will be 42%
elif gross_balance <= 49999.99:
    tax_rate = 42
#this is saying if the balance is above $50000
#then the tax rate will be 48%
else:
    tax_rate = 48

#calculations
#calculating the tax paid per starting balance
tax_payable = gross_balance * tax_rate / 100


#adding interest paid to original balance
net_balance = gross_balance - tax_payable

#outputs
    #starting balance
print("Gross Balance: ${0:,.2f}".format(gross_balance))
    #tax rate
print("Tax Rate: {0:,.2f}%".format(tax_rate))
    #tax paid
print("Tax Payable: ${0:,.2f}".format(tax_payable))
    #nett income
print("Nett Income: ${0:,.2f}".format(net_balance))
