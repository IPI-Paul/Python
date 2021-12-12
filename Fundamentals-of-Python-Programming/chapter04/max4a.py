# Listing 4.28
# Uses an if/elif/else statement to check for the maximum number entered
# Author: Rick Halterman
# Last modified: 

# Get input from user
print("Please enter four integer values.")
num1 = int(input("Enter integer 1: "))
num2 = int(input("Enter integer 2: "))
num3 = int(input("Enter integer 3: "))
num4 = int(input("Enter integer 4: "))

# Compute the maximum value 
if num1 >= num2 and num1 >= num3 and num1>= num4:
    max = num1
elif num2 >= num1 and num2 >= num3 and num2>= num4:
    max = num2
elif num3 >= num1 and num3 >= num2 and num3>= num4:
    max = num3
else:   # The maximum must benum4 at this point
    max = num4
    
# Report result
print("The maximum number entered was:", max)