# Listing 6.13
# Uses the sys.exit function to end the program's execution after it prints 10 
# numbers
# Author: Rick Halterman
# Last modified: 

import sys

sum = 0
while True:
    x = int(input('Enter a number (999 ends): '))
    if x == 999:
        sys.exit(0)
    sum += x
    print('Sum is', sum)