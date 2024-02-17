""" ---------------------------------------------------------------------------------

File: coffeeShop.py
 Written by Nicholas J. Griebel
 On 02-16-2023 for CIS 129

Purpose: This program asks user what they would like to buy from the coffee shop,
 calculates subtotals, taxes, and grand totals, and displays the users
 receipt to the terminal.

-------------------------------------------------------------------------------------- """

# Static variables -------
COFFEEPRICE     = 5.00
MUFFINPRICE     = 4.00
TAXPERCENT      = 0.06
# ------------------------

print("***************************************")             # Print welcome message and bumper
print("Welcome to Nick's Coffee & Muffin shop!")
coffeeNumber = input("How many coffees would you like?: ")   # Prompt user for how many coffees they want
muffinNumber = input("How many muffins would you like?: ")   # Prompt user for how many muffins they want
print("***************************************")             # Print outer bumper
# Convert totals from strings to integers
coffeeNumber = int(coffeeNumber)
muffinNumber = int(muffinNumber)

# Calculate total cost of both the coffee and the muffins, and total cost of both
coffeeTotal  = coffeeNumber * COFFEEPRICE
muffinTotal  = muffinNumber * MUFFINPRICE
totalCost    = coffeeTotal + muffinTotal

# Calculate taxes (6% of total)
taxTotal     = totalCost * TAXPERCENT

# Calculate grand total
grandTotal   = totalCost + taxTotal

# Print upper bumper
print("\n***************************************")

# Print receipt containing total number of each item bought,
# total cost of each type of item bought, the calculated tax,
# and the grand total including tax. 
print("Nick's coffee shop receipt")

# If the user only bought 1 coffee or muffin, format text correctly
# to reflect that. Otherwise print standard message
if coffeeNumber == 1:
    print("1 Coffee at $5 each: $", coffeeTotal)
else:
    print(coffeeNumber, "Coffees at $5 each: $", coffeeTotal)

if muffinNumber == 1:
    print("1 Muffin at $4 each: $", muffinTotal)
else:
    print(muffinNumber, "Muffins at $4 each: $", muffinTotal)

print("6% tax: $", taxTotal) # Display tax total
print("---------") # Print bumper for style

print("Total: $", grandTotal) # Print grand total (subtotal + calculated tax)

print("\n***************************************") # Print lower bumper
