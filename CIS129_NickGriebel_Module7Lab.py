# This program was written for CIS 129 Module 7 lab
# Written by Nick Griebel
# On 04/02/2024
#
# Purpose:
# 

def main():
    # Define constants
    aCost = 20
    bCost = 15
    cCost = 10

    aSeats = 300
    bSeats = 500
    cSeats = 200

    aSubtotal = 0
    bSubtotal = 0
    cSubtotal = 0

    # Print welcome messages and display section totals and details
    print("Welcome to Nick's dramatic theatre!")
    print("The A section has", aSeats, "total seats, cost for 1 is $" + str(aCost) +
          "\nThe B section has", bSeats, "total seats, cost for 1 is $" + str(bCost) +
          "\nThe C section has", cSeats, "total seats, cost for 1 is $" + str(cCost))


    # Get total amount of tickets sold for each row. Check to make sure that total ticket count
    # does not exceed total available seats for each row. If it does, request re-entry. 
    while(True):
        sectionATickets = get_integer("How many tickets were sold for section A?: ")
        if (sectionATickets > aSeats):
            print("There weren't that many seats available! Re-enter. ")
        else:
            aSubtotal = sectionATickets * aCost
            print("Subtotal for all tickets sold so far: $" + str(aSubtotal) + ".00")
            sectionBTickets = get_integer("How many tickets were sold for section B?: ")
            if (sectionBTickets > bSeats):
                print("There weren't that many seats available! Re-enter. ")
            else:
                bSubtotal = sectionBTickets * bCost
                print("Subtotal for all tickets sold so far: $" + str(aSubtotal + bSubtotal) + ".00")
                sectionCTickets = get_integer("How many tickets were sold for section C?: ")
                if (sectionCTickets > cSeats):
                    print("There weren't that many seats available! Re-enter. ")
                else:
                    cSubtotal = sectionCTickets * cCost
                    print("Subtotal for all tickets sold so far: $" + str(aSubtotal + bSubtotal + cSubtotal) + ".00")
                    break

    print("")
    print("Row A  -->   Total seats available:", aSeats, 
        "\n                Total tickets sold:", sectionATickets,
        "\n         Subtotal for tickets sold: $" + str(aSubtotal) + ".00")
    
    print("Row B  -->   Total seats available:", bSeats,
        "\n                Total tickets sold:", sectionBTickets,
        "\n         Subtotal for tickets sold: $" + str(bSubtotal) + ".00")
    
    print("Row C  -->   Total seats available:", cSeats,
        "\n                Total tickets sold:", sectionCTickets,
        "\n         Subtotal for tickets sold: $" + str(cSubtotal) + ".00")
    print("")

    print("Grand total from all ticket sales: $" + str(aSubtotal + bSubtotal + cSubtotal) + ".00\n")
    
    # End main

def get_integer(message):
    while True:

        try:
            user_input = int(input(message))
            if (user_input >= 0):
                return user_input
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid data entered. Please re-enter.")


__main__ = main()