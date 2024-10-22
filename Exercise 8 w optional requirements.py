# Exercise 8 Simple Search 

# Write the names in the given
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#Allow user to input the search term

# Get the search term for the user
search_for = input("Enter your name here:")

# This is to search the name
if search_for in names:
    print(f" {search_for} is in the list.")
else: 
    print (f" {search_for} is not in the list.")
# If the user doesn't provide input, use "Sam" as the default search term