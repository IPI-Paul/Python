# Listing 4.5
# This program uses the if/else statement to provide better feedback to the user
# Author: Rick Halterman
# Last modified: 

# Get two integers from the user 
dividend = int(input('Please enter the integer to divide: '))
divisor = int(input('Please enter the integer to divide by: '))
# If possible, divide them and report the result
if divisor != 0:
    print(dividend, '/', divisor, '=', dividend / divisor)
else:
    print('Division by zero is not allowed')