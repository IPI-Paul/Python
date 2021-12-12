# Listing 4.29
# Uses sequential if statements to check for the maximum number entered
# Author: Rick Halterman
# Last modified: 

# Get input from user
print("Please enter four integer values.")
num1 = int(input("Enter integer 1: "))
num2 = int(input("Enter integer 2: "))
num3 = int(input("Enter integer 3: "))
num4 = int(input("Enter integer 4: "))

# Compute the maximum value 
max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
if num4 > max:
    max = num4
    
# Report result
print("The maximum number entered was:", max)