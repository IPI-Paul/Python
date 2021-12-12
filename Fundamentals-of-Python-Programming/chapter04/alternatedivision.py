# Listing 4.3
# This program optionally executes two statements depending on the input values 
# provided by the user.
# Author: Rick Halterman
# Last modified: 

# Get two integers from the user
dividend = int(input('Please enter the integer to divide: '))
divisor = int(input('Please enter the integer to divide by: '))
# If possible, divide them and report the result
if divisor != 0:
    quotient = dividend / divisor
    print(dividend, '/', divisor, '=', quotient)
print('Program finished')