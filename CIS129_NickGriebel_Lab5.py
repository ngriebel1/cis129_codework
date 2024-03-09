# Initial definition of variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = "y"

while keepGoing == "y":

    # Reset variables for new loop
    totalBottles = 0
    counter = 1
    todayBottles = 0
    totalPayout = 0
    keepGoing = "y"

    # Cycle through and collect bottle data for each day of the week
    while counter <= 7:
        print("Enter number of bottles for day #", counter, ":")
        todayBottles = int(input())     # Get total bottles for day
        totalBottles += todayBottles    # Add it to totalBottles
        counter += 1                    # Move to the next day

    totalPayout = totalBottles * 0.10   # Calculate total payout from all bottles collected

    # Display total number of bottles collected and total payout calculation to screen
    print("The total number of bottles collected is ", totalBottles)
    print("The total paid out is $ ", totalPayout)

    # More data to input? y=yes, n=no
    print("Do you want to enter another week's worth of data?")
    print("(Enter y or n): ")
    keepGoing = input()

