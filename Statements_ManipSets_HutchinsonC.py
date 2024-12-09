# Assignment 2
# Casey Hutchinson
# ITEC 3100
# Due by 09/15/2024

def user_pay():
    # Part A
    # Asks the user to enter their name and stores it in the global variable "n" (step 1)
    global n
    n = input("Hello. Please enter your name: ")
    while True:
        try:
            hr_rate = float(input(f"{n}, please enter the hourly rate for your current job: "))     # Asks the user by the name entered previously what their hourly pay rate for their job is (step 2)
            print("Thank you.")
            break                                                                                   # breaks loop
        except ValueError:                                                                          # ValueError is used to ask the user again if they input a string value instead
            print("Please enter number values only. Thank you.")
    while True:
        try:
            hrs = float(input("And how many hours do you work in a week? "))                        # Asks the user how many hours they work in a week (step 3)
            print("Thank you.")
            break                                                                                   # breaks loop
        except ValueError:                                                                          # ValueError is used to ask the user again if they input a string value instead
            print("Please enter number values only. Thank you.")
    if hrs <= 40.0:                                                                                 # Determines the users hourly rate if they work 40 hours or less per week (step 4)
        gross_pay = hr_rate * hrs
        print(f"{n}, your total gross pay is ${gross_pay:.2f}")                                     # Displays the users gross pay with dollar sign and two decimal places - I've used .2f in previous course work (step 5)        
    else:                                                                                           # Determines the users hourly rate if they work more than 40 hours per week (step 4)
        gross_pay = hr_rate * 40.0
        ot = (hrs - 40.0) * (hr_rate * 1.5)
        new_gross_pay = gross_pay + ot
        print(f"{n}, your total gross pay is ${new_gross_pay:.2f}")                                 # Displays the users gross pay with dollar sign and two decimal places - I've used .2f in previous course work (step 5)

def user_grades():
    # Part B
    # Greets the user with the name entered for Part A (step 1)
    print("\n")
    print(f"Hello {n}, I've got a couple questions about your grades now.")
    a_points = []
    for i in range(6):                                                                                                  # Using a for loop, I ask the user how many points out of 10 they got on each of the 6 assignments and store the values in a list (step 2)
        while True:
            try:
                assign_points = float(input(f"How many points (out of 10) did you receive on Assignment {i + 1}? "))
                if assign_points <= 10.0:
                    a_points.append(assign_points)
                    break   
                else:
                    print("Invalid input. Please enter a value beetwen 0 and 10. Thank you.")               
            except ValueError:                                                                                          # ValueError is used to make sure the user inputs a value between 0-10
                print("Invalid input. Please enter a value beetwen 0 and 10. Thank you.")
    print("\n")
    q_points = []
    for i in range(12):                                                                                                 # Using a for loop I ask the user how many points out of 5 they got on each of the 12 quizzes and store the values in a list (step 3)
        while True:
            try:
                quiz_points = float(input(f"How many points (out of 5) did you receive on Quiz {i + 1}? "))
                if quiz_points <= 5.0:
                    q_points.append(quiz_points)
                    break
                else:
                    print("Invalid input. Please enter a value beetwen 0 and 5. Thank you.")
            except ValueError:                                                                                          # ValueError is used to make sure the user inputs a value between 0-5
                print("Invalid input. Please enter a value beetwen 0 and 5. Thank you.")
    print("\n")
    while True:
        midterm = (float(input("How many points (out of 30) did you earn on the midterm? ")))                           # Asks the user how many points out of 30 they earned on the midterm exam and store it in the "midterm" variable (step 4)
        if midterm <= 30.0:
            print("Thank you.")
            break
        else:
            print("Value is too high. Please enter a value between 0 and 30. Thank you.")
    print("\n")
    while True:
        final_project = (float(input("How many points (out of 50) did you earn on the final project? ")))               # Asks the user how many points out of 50 they earned on the final project and store it in the "final_project" variable (step 5)
        if final_project <= 50.0:
            print("Thank you.")
            break
        else:
            print("Value is too high. Please enter a value between 0 and 50. Thank you.")
    print("\n")

    assignments = sum(a_points)                                                                                 # I take the sum of the users points in the "a_points" assignments list and store it in a new "assignments" variable
    quizzes = sum(q_points)                                                                                     # I take the sum of the users points in the "q_points" quizzes list and store it in a new "quizzes" variable
    final_points = (assignments + quizzes + midterm + final_project)/2                                          # I add together the total number of points from all the variables and divide the total by 2 in order to grade on a 0-100 range, and store the total in the "final_points" variable (step 6)

    # Using an if, elif, else structure I use the "final_points" variable to determine the users final letter grade according to the chart in the course syllabus and displays the final answer to them (step 7)
    if final_points < 60:
        print("Failing work. Your final letter grade is an F.")
    elif final_points >=60 and final_points <=69.9:
        print("Passing work. Your final letter grade is a D.")
    elif final_points >=70 and final_points <=79.9:
        print("Satisfactory work. Your final letter grade is a C.")
    elif final_points >=80 and final_points <=89.9:
        print("Good work! Your final letter grade is a B.")
    else:
        print("Excellent work! Your final letter grade is an A!")

def get_sets():
    # Part C
    # Greets the user with the name entered for Part A (step 1)
    print("\n")
    print(f"Alright {n}, now I'd like to ask your to enter some data for me!")
    while True:
        future_set1 = input("Please enter a string of text that's at least 10 characters long containing letters, numbers, and/or symbols. Example - 'Mi$$iss!ppi': ")                      # Asks the user to input a set of text as a string containing at least 10 characters (step 2)
        if len(future_set1) >= 10:                                                                                                                                                          # Tests to make sure the input is at least 10 characters (step 3)
            print(f"Thank you. You entered '{future_set1}'")
            break
        else:
            print("Error. Please try again and enter at least 10 characters. Thank you.")                                                                                                   # Error message asking the user to try again (step 3)
    while True:
        future_set2 = input("Please enter a second string of text that's at least 10 characters long containing letters, numbers, and/or symbols: ")                                        # Asks the user to input a set of text containing at least 10 characters (step 4)
        if len(future_set2) >= 10:                                                                                                                                                          # Tests to make sure the input is at least 10 characters (step 5)
            print(f"Thank you. You entered '{future_set2}'")
            break
        else:
            print("Error. Please try again and enter at least 10 characters. Thank you.")                                                                                                   # Error message asking the user to try again (step 5)
    S1 = set(future_set1)                                                                                                                                                                   # Converts the user input into a set
    S2 = set(future_set2)                                                                                                                                                                   # Converts the user input into a set
    
    # First I display the sets to the user. Then I display a menu to ask the user what they would like to do with their sets. When they've made a selection, I use an if, elif, else statement to run the test they selected (step 6)
    print(f"Now that we have your input, we're going to look at our two 'sets.' These are the 2 sets we'll work with based on what you entered: Set one: {S1} and Set two: {S2}")
    print("\n")
    print("Use the list below to choose which test you'd like to perform on our new sets.")
    while True:
        print("1. Determine if the sets are disjointed.")
        print("2. Determine if one set is the subset of the other set.")
        print("3. Determine if one set is a proper subset of the other set.")
        print("4. Determine if one set is the superset of the other set.")
        print("5. Determine if one set is a proper superset of the other set.")
        print("6. Determine the union of the sets.")
        print("7. Determine the intersection of the sets.")
        print("8. Determine the difference of the sets.")
        print("9. Replace one set with different values.")
        print("0. Exit.")                                                                                                                                                                   # The user can input "0" to end the program (step 8)
        choice = input("Please enter the test you'd like to perform by entering the appropriate number: ")
        print("\n")

        # This is the if, elif, else statement constructed for step 6 that the user selection calls based on their input 
        if choice == "1":
            result = S1.isdisjoint(S2)
            print(f"Set one and Set two are disjoined: {result}!")                                                                                                                          # Displays the result from part 6 if the user chose input #1 (step 7)
            print("\n")

        elif choice == "2":
            selection = input("Which set would you like to test to see if it is a subset of the other? Enter 1 or 2: ")
            if selection == "1":
                result = S1.issubset(S2)
                print(f"Set one is a subset of Set two: {result}!")                                                                                                                         # Displays the result from part 6 if the user chose input #2 and Set one (step 7)
                print("\n")
            elif selection == "2":
                result = S2.issubset(S1)
                print(f"Set two is a subet of Set one: {result}!")                                                                                                                          # Displays the result from part 6 if the user chose input #2 and Set two (step 7)
                print("\n")
            else:
                print("Error. Please enter a 1 or 2.")

        elif choice == "3":
            selection = input("Which set would you like to test to see if it is a proper subset of the other? Enter 1 or 2: ")
            if selection == "1":
                result = S1 < S2
                print(f"Set one is a proper subset of Set two: {result}!")                                                                                                                  # Displays the result from part 6 if the user chose input #3 and Set one (step 7)
                print("\n")
            elif selection == "2":
                result = S2 < S1
                print(f"Set two is a proper subset of Set one: {result}!")                                                                                                                  # Displays the result from part 6 if the user chose input #3 and Set two (step 7)
                print("\n")
            else:
                print("Error. Please enter a 1 or 2.")

        elif choice == "4":
            selection = input("Which set would you like to test to see if it is a superset of the other? Enter 1 or 2: ")
            if selection == "1":
                result = S1.issuperset(S2)
                print(f"Set one is a superset of Set two: {result}!")                                                                                                                       # Displays the result from part 6 if the user chose input #4 and Set one (step 7)
                print("\n")
            elif selection == "2":
                result = S2.issuperset(S1)
                print(f"Set two is a superset of Set one: {result}!")                                                                                                                       # Displays the result from part 6 if the user chose input #4 and Set two (step 7)
                print("\n")
            else:
                print("Error. Please enter a 1 or 2.")

        elif choice == "5":
            selection = input("Which set would you like to test to see if is a proper superset of the other? Enter 1 or 2: ")
            if selection == "1":
                result = S1 > S2
                print(f"Set one is a proper superset of Set two: {result}!")                                                                                                                # Displays the result from part 6 if the user chose input #5 and Set one (step 7)
                print("\n")
            elif selection == "2":
                result = S2 > S1
                print(f"Set two is a proper superset of Set one: {result}!")                                                                                                                # Displays the result from part 6 if the user chose input #5 and Set two (step 7)
                print("\n")
            else:
                print("Error. Please enter a 1 or 2.")

        elif choice == "6":
            result = S1.union(S2)
            print(f"The union of Set one and Set two is: {result}")                                                                                                                         # Displays the result from part 6 if the user chose input #6 (step 7)
            print("\n")

        elif choice == "7":
            result = S1.intersection(S2)
            print(f"The intersection of Set one and Set two is: {result}")                                                                                                                  # Displays the result from part 6 if the user chose input #7 (step 7)
            print("\n")

        elif choice == "8":
            selection = input("Which set would you like to find the difference for first? Enter 1 or 2: ")
            if selection == "1":
                result = S1.difference(S2)
                print(f"The difference of Set one and Set two is: {result}")                                                                                                                # Displays the result from part 6 if the user chose input #8 and Set one (step 7)
                print("\n")
            elif selection == "2":
                result = S2.difference(S1)
                print(f"The difference of Set two and Set one is: {result}")                                                                                                                # Displays the result from part 6 if the user chose input #8 and Set two (step 7)
                print("\n")
            else:
                print("Error. Please enter a 1 or 2.")

        elif choice == "9":
            selection = input("Which set would you like to update? Enter 1 or 2: ")
            if selection == "1":
                new_set = input("Enter any text containing letters, numbers, and/or symbols to update Set one: ")
                S1 = set(new_set)
                print(f"The updated Set one is now: {S1}")                                                                                                                                  # Displays the new set that the user entered if the user chose input #9 and Set one (step 7)
                print("\n")
            elif selection == "2":
                new_set = input("Enter any text containing letters, numbers, and/or symbols to update Set two: ")
                S2 = set(new_set)
                print(f"The updated Set two is now: {S2}")                                                                                                                                  # Displays the new set that the user entered if the user chose input #9 and Set two (step 7)
                print("\n")

        elif choice == "0":
            print("Thanks for looking at Sets with me today. Have a great day!")                                                                                                            # Displays a thank you message if the user chose input #0 to exit the program (step 8)
            break

        else:
            print("Error. Invalid choice. Please select from the available options and try again.")                                                                                         # Error message that displays the user input isn't a valid choice and asks them to try again (step 8)


def main():
    user_pay()
    user_grades()
    get_sets()

if __name__ == "__main__":
    main()