# Exercise 4: Primitive Quiz


# List of European countries and their capitals
countries_and_capitals = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("United Kingdom", "London"),
    ("Spain", "Madrid"),
    ("Italy", "Rome"),
    ("Finland", "Helsinki"),
    ("Denmark", "Copenhagen"),
    ("Poland", "Warsaw"),
    ("Sweden", "Stockholm"),
    ("Norway", "Oslo"),
]

# Initialize score
score = 0

# Start the quiz
# Loop through each country and capital
for country, capital in countries_and_capitals:
    print(f"What is the capital of {country}?")
    answer = input().lower()

    # Check if the answer is correct
    if answer == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The capital of {country} is {capital}.")
    # This is for when the answer is incorrect    

# Print final score
print("--------------------------------------")
print(f"You scored {score} out of {len(countries_and_capitals)}.")
