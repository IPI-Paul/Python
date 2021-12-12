# Listing 4.2
# File betterdivision.py
# Shows how to take steps to ensure that a user input does not cause an error
# Author: Rick Halterman
# Last modified: 

# Get two integers from the user 
print('Please enter two integers to divide.')
dividend = int(input('Please enter the first integer to divide: '))
divisor = int(input('Please enter the second integer to divide: '))
# If possible, divide them and report the result
if divisor != 0:
    print(dividend, '/', divisor, '=', dividend / divisor)