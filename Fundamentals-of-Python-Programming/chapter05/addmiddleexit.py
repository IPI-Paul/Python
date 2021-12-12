# Listing 5.23
# Uses a while loop to add all nonnegatives entered by the user and then uses a 
# break statement to implement middle-exiting loop control logic
# Author: Rick Halterman
# Last modified: 

# Allow the user to enter a sequence of nonnegative numbers. The user ends the 
# list with a negative number. At the end the sum of the nonegative numbers 
# entered is displayed. the program prints zero if the user provides no 
# nonnegative numbers.

entry = 0           # Ensure the loop is entered
sum = 0             # Inintialize sum

# Request input from the user
print("Enter numbers to sum, negative number ends list: ")

while True:                                         # Loop forever? Not really
    entry = int(input('Please enter an integer: ')) # Get value
    if entry < 0:                                   # Is number negative?
        break                                       # If so, exit the loop
    sum += entry                                    # Add entry to running sum
print("Sum =", sum)