# Listing 4.9
# Uses nested if/else statements to determine if a number is between 0 and 10, 
# inclusive
# Author: Rick Halterman
# Last modified: 

value = int(input('Please enter and integer value in the range 0...10: '))
if value >= 0:              # First check
    if value <= 10:         # Second check
        print('In range')
print('Done')