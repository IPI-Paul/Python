# Listing 4.24
# Uses an if/else statement to check for division by zero
# Author: Rick Halterman
# Last modified: 

# Get dividend and divisor from the user
dividend = int(input('Enter dividend integer: '))
divisor = int(input('Enter divisor integer: '))
# We want to divide only if divisor is not zero; otherwise, we will print an 
# error message
if divisor != 0:
    print(dividend / divisor)
else:
    print("Error, cannot divide by zero")