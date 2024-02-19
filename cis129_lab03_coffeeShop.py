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
LATTEPRICE      = 7.00
COOKIEPRICE     = 2.50
TAXPERCENT      = 0.06
# ------------------------

print("***************************************")             # Print bumper and welcome message
print("Welcome to Nick's Coffee & Muffin shop!")

coffeeNumber = input("How many coffees would you like?: ")   # Prompt user for how many coffees they want
muffinNumber = input("How many muffins would you like?: ")   # Prompt user for how many muffins they want
latteNumber  = input("How many lattes would you like?: ")    # Prompt user for how many lattes they want
cookieNumber = input("How many cookies would you like?: ")   # Prompt user for how many cookies they want

print("***************************************")             # Print outer bumper

# Begin conversions and price calculations -----------------------------------

coffeeNumber = int(coffeeNumber)                             # Convert totals from strings to integers
latteNumber  = int(latteNumber)
cookieNumber = int(cookieNumber)
muffinNumber = int(muffinNumber)

coffeeTotal  = coffeeNumber * COFFEEPRICE                    # Calculate total cost of the coffees, lattes, cookies and muffins, and total cost of all
latteTotal   = latteNumber * LATTEPRICE
muffinTotal  = muffinNumber * MUFFINPRICE
cookieTotal  = cookieNumber * COOKIEPRICE
totalCost    = coffeeTotal + muffinTotal + latteTotal + cookieTotal

taxTotal     = totalCost * TAXPERCENT                        # Calculate taxes (6% of total)
grandTotal   = totalCost + taxTotal                          # Calculate grand total

# End conversions and price calculations --------------------------------------

# Begin receipt printing ------------------------------------------------------

print("\n***************************************")           # Print upper bumper

print("Nick's coffee shop receipt")                          # Print receipt containing total number of each item bought,
                                                             # total cost of each type of item bought, the calculated tax,
                                                             # and the grand total including tax.

if coffeeNumber == 1:                                        # If the user only bought 1 coffee, latte, cookie or muffin, format text correctly
    print("1 Coffee at $5 each: $", coffeeTotal)             # to reflect that. Otherwise print standard message
else:
    print(coffeeNumber, "Coffees at $5 each: $", coffeeTotal)

if muffinNumber == 1:
    print("1 Muffin at $4 each: $", muffinTotal)
else:
    print(muffinNumber, "Muffins at $4 each: $", muffinTotal)

if latteNumber == 1:
    print("1 Latte at $7 each: $", latteTotal)
else:
    print(latteNumber, "Lattes at $7 each: $", latteTotal)

if cookieNumber == 1:
    print("1 Cookie at $2.50 each: $", cookieTotal)
else:
    print(cookieNumber, "Cookies at $2.50 each: $", cookieTotal)

print("6% tax: $", taxTotal)                                 # Display tax total
print("---------")                                           # Print bumper for style

print("Total: $", grandTotal)                                # Print grand total (subtotal + calculated tax)

print("\n***************************************")           # Print lower bumper

print("Thank you for shopping at Nick's coffee and muffin shop! \
    \nHave a great day!")

# End receipt printing ---------------------------------------------------------
