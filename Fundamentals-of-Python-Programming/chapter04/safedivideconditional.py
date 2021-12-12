# Listing 4.25
# Uses a conditional expression to check for division by zero
# Author: Rick Halterman
# Last modified: 

# Get dividend and divisor from the user
dividend = int(input('Enter dividend integer: '))
divisor = int(input('Enter divisor integer: '))
# We want to divide only if divisor is not zero; otherwise, we will print an 
# error message
msg = dividend / divisor if divisor != 0 else 'Error, cannot divide by zero'
print(msg)