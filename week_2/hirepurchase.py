#This is a program tha calculates hire purchase
#Date:21/02/2024
#Name: Tracy Kanyora

import math

# hire purchase
cash_price = float(input("Enter the cash price"))
deposit = float(input("Enter the deposit"))
time_months = float(input("Enter tme in months"))
installments = float(input("Enter number of installments"))

hire_purchase = deposit + (time_months* installments)

print("The hire purchase:" , hire_purchase)
