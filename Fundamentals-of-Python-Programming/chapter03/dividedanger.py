# Listing 3.6
# File dividedanger.py
# Demonstrates errors that cause a Run-time Exception. If the user inputs 0 to 
# as the divisor it will cause an exception.
# Author: Rick Halterman
# Last modified: 

# Get two integers from the user
print('Please enter two integers to divide.')
dividend = int(input('Please enter the dividend: '))
divisor = int(input('Please enter the divisor: '))
# Divide them and report the result
print(dividend, '/', divisor, '=', dividend / divisor)