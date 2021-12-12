# Listing 12.4
# Asks user for a small integer value
# Author: Rick Halterman
# Last modified: 

try:
    val = int(input('Please enter a small positive integer: '))
    print('You entered', val)
except ValueError:
    print('Input not accepted')