# Exercise 5 Days of the Month

# This program tells the user how many days there are in a specific month.


# Dictionary mapping month numbers to the number of days
days_of_the_month = {
    1: 31,  # JAN
    2: 28,  # FEB
    3: 31,  # MAR
    4: 30,  # APR
    5: 31,  # MAY
    6: 30,  # JUN
    7: 31,  # JUL
    8: 31,  # AUG
    9: 30,  # SEP
    10: 31, # OCT 
    11: 30, # NOV
    12: 31, # DEC
}

# Ask the user for the month number
month_number = int(input("Enter the month number:"))

# Check if the input is valid
if 1 <= month_number <= 12:
    # Check if it's February and if it's a leap year
    if month_number == 2:
        is_leap_year = input("Is it a leap year? (yes/no):").lower()
        if is_leap_year == "yes":
            print("February has 28 days")
            days_of_the_month[2] = 29
        else:
            print("February has 29 days")

    # Print the number of days in the month
    print(f"There are {days_of_the_month[month_number]} days in month {month_number}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
    # This is an error message if the number isn't correct
    
   

