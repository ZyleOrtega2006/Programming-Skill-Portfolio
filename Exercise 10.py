# Exercise 10 Is it Even

# This is the function of the code
def main():
# This is to prompt the user input a number
    odd_or_even=int(input("Input a number: "))

# This code makes it so it runs a odd or even code when you input a number
    if odd_or_even % 2 == 0:
        result = "The number is even."
    else:
        result = "The number is odd."
# The if and else are so to identify the user if the code is an odd or an even number 
       
        print (result) # This is so to print the result
if __name__ == "__main__":
    main()
# This is so that the code can run      