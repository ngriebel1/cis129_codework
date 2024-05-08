# --------------------------------------------------------------------------------------------------
# Written by Nick Griebel for Module 11 Lab, CIS129
# On 05-07-2024
#
# Purpose:      9.1 -->    This function allows the user to enter valid grades 
#                          into the program, and saves the grades to a file.
#
#               9.2 -->    This function reads the grades from the file created
#                          in the previous function, and also displays their total,
#                          number of grades in the file, and the average grade based
#                          on all the grades present in the file.
#
#               9.3 -->    This function retrieves first and last student names from the
#                          user, and the grade they achieved for 3 exams. This information
#                          is then formatted, and written to a .CSV formatted file. Each new
#                          record added is on its own line.
# --------------------------------------------------------------------------------------------------

# library imports
import csv

# Main driver routine. Executes each exercise driver (9.1, 9.2 & 9.3) in order.
def main():
    print("Module 11 Lab written by Nick Griebel on 05-07-2024\n")
    print("\n    --> Executing Exercise 9.1")
    Exercise_9_1()

    print("\n    --> Executing Exercise 9.2")
    Exercise_9_2()

    print("\n    --> Executing Exercise 9.3")
    Exercise_9_3()

    print("\nExecution of exercises complete. ")
    
    
# Exercise main routines ---------------------------

# This exercise allows the user to enter valid grades, and write those
# valid grades into a text file. These grades are delimeted by spaces, ' '.
#  NOTE: grades.txt file being accessed in a(ppend)+ mode. Please take care
#  to not overwrite any contents of the existing file! Thank you :)
def Exercise_9_1():
    while (True):
        validGrade = getValidGrade("Please enter a valid grade (Q to quit): ",
                            "That is not a valid grade. Please enter again. ")
        if validGrade == -1:
            print("Thank you! Grades were added to file 'grades.txt' in the current directory.")
            print("Have a nice day!")
            return

        with open("grades.txt", mode="a+") as gradeFile:
            gradeFile.write(str(validGrade) + " ")

# This exercise displays the contents of the grades file that was created/modified in the
# previous exercise. It formats the printed outputs, displays grades, their respective number
# in the file entries, the total of all the grades and the overall grade average. 
def Exercise_9_2():
    # unrelated newline to space between "executing exercise" msg and
    # this functions output
    print('')

    # Define some variables we will need
    fileName = "grades.txt"
    fileContent = str()
    
    gradeList = []
    gradeTotal = 0
    gradeAverage = 0

    # Open the file in read-only mode.
    with open(fileName, "r") as gradeFile:
        fileContent = gradeFile.read()      # Read in raw file data to split apart into a list
        gradeList = fileContent.split()     # Split apart the file contents with the space delimeter.

        for i in range(len(gradeList)):
            gradeList[i] = int(gradeList[i])    # Convert all grades into integers to be calculated with
            print(f" Grade {str(i+1):>2}:  {gradeList[i] : >17}")

        print("="*30) # *print a separator of '='s

        # We need to get the total of all the grades in the file
        for i in range(len(gradeList)):
            gradeTotal = gradeTotal + gradeList[i]
        print(f"{' Grade total:  ' : >12} {gradeTotal:>13}")

        # Then we need to get the average of all the grades in the file
        gradeAverage = gradeTotal / len(gradeList)
        print(f" Grade average: {gradeAverage:>13.2f}")

def Exercise_9_3():
    badExamGradeMsg = "Please enter a valid exam grade."

    while (True):
        # We need the first and last name of the student that the user is storing grades for.
        firstName = getValidName("First name: ", "Please enter a valid first name. ")
        lastName = getValidName("Last name: ", "Please enter a valid last name. ")

        # Now we need to get the actual grades.  
        exam1Grade = getValidGrade("First exam grade: ", badExamGradeMsg)
        exam2Grade = getValidGrade("Second exam grade: ", badExamGradeMsg)
        exam3Grade = getValidGrade("Third exam grade: ", badExamGradeMsg)

        with open("grades.csv", mode="a+") as gradesFile:
            fileWriter = csv.writer(gradesFile)
            fileWriter.writerow([lastName] + [firstName] + [exam1Grade] + [exam2Grade] + [exam3Grade])

        # And finally, we ask if the user would like to enter another grade. Return if not.
        sentinel = input("Would you like to enter another grade?(Y/N): ").lower()

        if sentinel == 'n':
            return
    

    # Debug code block
    print(firstName + " " + lastName)
    print("Grade 1: " + str(exam1Grade))
    print("Grade 2: " + str(exam2Grade))
    print("Grade 3: " + str(exam3Grade))
    # End debug code block

# --------------------------------------------------

# This routine retrieves a valid name from the user. A valid name
# is any string that does not contain anything other than alphabetical
# characters. Names that contains numbers or symbols are invalid names.
def getValidName(promptMsg, errorMsg):
    while(True):
        try:
            validName = input(promptMsg)
            if not validName.isalpha():
                print(errorMsg)
            else:
                return validName
        except(ValueError):
            print(errorMsg)

# This routine retrieves a valid grade from the user. Valid grades
# are any positive integer between 0 and 100. Anything greater than,
# less than, or not equal to an integer are not valid input.
def getValidGrade(promptMsg, errorMsg):
    while(True):
        try:
            validGrade = input(promptMsg)
            if validGrade.lower() == 'q':
                return -1
            elif int(validGrade) > 100 or int(validGrade) < 0:
                print(errorMsg)
            else:
                return int(validGrade)
        except(ValueError):
            print(errorMsg)

main()
