# Listing 6.1
# Uses the Math library function sqrt, eliminating the complex logic of the 
# original code
# Author: Rick Halterman
# Last modified: 

from math import sqrt

# Get value from the user
num = float(input('Enter a number: '))

# Compute the square root
root = sqrt(num)

# Report the result
print("Square root of", num, "=", root)