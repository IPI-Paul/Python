# Listing 5.20
# Uses a triply nested loop to print all the differrent arrangements of the 
# letters A, B, and C. Each string is a permutation of ABC
# Author: Rick Halterman
# Last modified: 
# File permuteabc.py

# The first letter varies from A to C
for first in 'ABC':
    for second in 'ABC':    # The second varies from A to C
        if second != first:     # No duplicate letters allowed
            for third in 'ABC':     # The third letter varies from A to C
                # Don't duplicate first or second letter
                if third != first and third != second:
                    print(first + second + third)