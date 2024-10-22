# Exercise 3 Biography        

# I make a variable in order for the user to input their data into the code
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

while True: # I assign a loop once an integer has been entered
    age_input = input("Enter your age: ")
    try: 
        age = int(age_input)
        break
    except ValueError:
        
# I then displayed it to the user of the pyhton dictionary 
        print("Please enter valid integers")