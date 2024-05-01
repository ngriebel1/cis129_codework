#
# CIS 129
# Nick Griebel
# 04-30-2024
# Module 10 Lab (Exercise 8.1)
# 
#  This program creates a check value that is protected from alterations 
# by using leading asterisks in the printout. This makes it harder to make
# alterations to the checks value. 
#

import decimal

# Purpose: Main function. Retrieves a valid payable amount, and
#           formats it to be printed to the screen.
def main():
    # Retrieve desired payable amount for check printout
    # Include both the inquiry message and an error message
    payableAmount = getFloat("Please enter a payable amount: ", \
                             " !! That is not a valid payable amount !!")

    # Format the payable amount, and print to the screen with
    # anti-theft formatting (asterisk place-holders)
    print(f"Total check amount: \n${payableAmount:*>10,.2f}")


# Purpose: Retrieve a valid float value from the user, and
#           reject all others until a valid value is retrieved.
def getFloat(inquiryMsg, errorMsg):
    while (True):
        try:
            floatVal = input(inquiryMsg)

            # Check if we have a negative number on our hands before
            # converting to a floating point variable.
            if '-' in floatVal:
                print(errorMsg)
                # continue looping at this point. no break provided to this branch

            else:
                return float(floatVal) # Good input was retrieved. convert & return it
            

        # An incorrect value was entered. Ask for input again
        except(ValueError):   
            print(errorMsg)

main()
