# Exercise 6: Brute Force Attack 

# Define the correct password for it
correct_password = "12345"

max_attempts = 5 # This is the maximum amount of attempts the user can do 
attempts = 0 # But this is the max for the user

# Use a while loop to repeatedly ask for the password until it's correct or attempts are exhausted
while attempts < 5:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Password correct. Access granted.")
        break # This is for the code to stop doing it again after having the correct password
    else:
        print("Incorrect password. You have", 5 - attempts - 1, "attempts remaining.")
        attempts += 1

# If the maximum number of attempts is reached, inform the user
if attempts == 5:
    print("Maximum attempts reached. The Authorities has been alerted.")

