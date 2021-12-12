# Listing 4.11
# Uses nested if/else statements to determine if a number is between 0 and 10, 
# inclusive as it would be impossible to rewrite with only one if statment
# Author: Rick Halterman
# Last modified: 

value = int(input('Please enter and integer value in the range 0...10: '))
if value >= 0:                          # First check
    if value <= 10:                     # Second check
        print(value, 'is in range')
    else:
        print(value, 'is too large')
else:
    print(value, 'is too small')
print('Done')