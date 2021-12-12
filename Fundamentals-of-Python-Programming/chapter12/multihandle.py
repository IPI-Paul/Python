# Listing 12.7
# Illustrates an exact code that handles more than one exception type. It 
# associates multiple types with a single except block by listing each exception
# type within a tuple.
# Author: Rick Halterman
# Last modified: 

import random

for i in range(10):     # Loop 10 times
    print('Beginning of loop iteration', i)
    try:
        r = random.randint(1, 3)    # r is pseudorandomly 1, 2, or 3
        if r == 1:
            print(int('Fred'))  # Try to convert a non-integer
        elif r == 2:
            [][2] = 5   # Try to assign to a nonexistent index of the empty list
        else:
            print(3 / 0)    # Try to devide by zero
    except (ValueError, ZeroDivisionError):
        print('Problem with integer detected')
    except IndexError:
        print('List index is out of range')
    
    print('End of lop iteration', i)        