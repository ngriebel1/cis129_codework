# In-class code-along for CIS 129
# Written on 03-11-2024
# By Nick Griebel
#
# This program is practice with loops in python

def main():
    doAgain = 'y'
    while (doAgain == 'y'):
        number = int(input("Please enter a number: "))

        if (number % 2 == 0):
            print("This number is even")
        else:
            print("This number is odd")

        doAgain = input("Would you like to enter another number? (Y/N): ")
        while (doAgain != 'y' and doAgain != 'n'):
            doAgain = input("What? Respond with y or n: ")

__main__ = main()
