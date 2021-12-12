# Listing 12.5
# Includes a statement that attempts to assign a value at index 2 of an empty 
# list.
# Author: Rick Halterman
# Last modified: 

try:
    val = int(input('Please enter a small positive integer: '))
    print('You entered', val)
    [][2] = val # Try to assign to a nonexistent index of the empty list
except ValueError:
    print('Input not accepted')    