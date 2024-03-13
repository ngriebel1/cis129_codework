# This program explores looping and input checking in python
# Written by Nick Griebel
# On 03-13-2024
# For CIS 129
#

def main():
    restartInput = "y"
    userNumber = ""

    # Call get_integer to retrieve number from the user
    while (restartInput == "y"):
        userNumber = get_integer("Please enter a number: ")

        # Check whether users inputted number is even or odd
        if (userNumber % 2 == 0):
            print("Your number", userNumber, "is even!")
        else:
            print("Your number", userNumber, "is odd!")

        # Ask user if they would like to enter another number
        restartInput = input("Would you like to enter another number? (Y/N): ")

        # Check for correct (y/n) input from user. repeat input if incorrect input
        if (restartInput != "y" and restartInput != "n"):
           while (restartInput != "y" and restartInput != "n"):
               restartInput = input("Would you like to enter another number? (Y/N): ")

        # If user entered no(n), return from main to caller.
        if (restartInput.lower() == "n"):
            return 0

# This routine retrieves a number from the user and verifies
#   that input was an integer. If it was not, an error is thrown
#   and user is prompted to re-enter input
def get_integer(message):
    while True:

        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Incorrect data entered. Please re-attempt")


__main__ = main()       # Set our main routine as main()
