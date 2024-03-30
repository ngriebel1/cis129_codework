# This program was written by Nick Griebel
# For CIS 129 Module 7 assignment.
# Purpose:  This is a simple dice game written in python, converted from the
#           module 7 assignment pseudo-code.
# Written on 03-29-2024
#

# Add libraries needed
import random

def main():
    print()

    # Initialize variables
    endProgram = "no"
    playerOne = playerTwo = "NONE"
    
    # Call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':

        # Populate variables
        winnersName = "NO NAME"
        p1number = p2number = 0

        # Call to rollDice
        winnersName = rollDice(p1number, p2number, playerOne, playerTwo,
                              winnersName)
        
        # Call to displayInfo
        displayInfo(winnersName)
        endProgram = input("Do you want to end program? (Yes/No): ").lower()

# This function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Please enter the name of player one: ")
    playerTwo = input("Please enter the name of player two: ")
    return playerOne, playerTwo

# This function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnersName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number == p2number:
        winnersName = "TIE"
    elif p1number > p2number:
        winnersName = playerOne
    elif p2number > p1number:
        winnersName = playerTwo
    else:
        winnersName = "ERROR"

    return winnersName

# This function displays the winner
def displayInfo(winnersName):
    print("The winner is " + winnersName + "! Congratulations! ")
    return

# calls main
__main__ = main()
