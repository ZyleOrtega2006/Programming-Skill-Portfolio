# Exercise 7 Some Counting 

def main():
# Print a count from 0 to 50   
    print("Count from 1 to 50:")
    for number in range (0, 50,):
        print(number) # Display it into the user
        
# Count 50 to 0 in increments of -1 so it displays at 0       
    print("\nCounting down from 50 to 0:")
    for number in range (50, -1 -1,):
        print(number)
 
# Count from 30 to 50   
    print("\nCounting down from 30 to 50:")
    for number in range (30, 51): 
        print(number)     
      
# Count down from 50 to 10 in -2 it goes down by 2 and displays a 10 by the end of it.       
    print("\nCounting down from 50 to 10 in decrements of 2:")
    for number in range (50, 9, -2):
        print(number) 

# Count from 100 to 200 in increments of 5        
    print("\nCounting down from 50 to 10 in decrements of 2:")
    for number in range (100, 200, 5):
        print(number)     
        
if __name__ == "__main__":
     main()