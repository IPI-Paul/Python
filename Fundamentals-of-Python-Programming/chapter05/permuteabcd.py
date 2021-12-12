# Listing 5.21
# Uses a four deep nested loop to print all the differrent arrangements of the 
# letters A, B, C, and D. Each string is a permutation of ABCD
# Author: Rick Halterman
# Last modified: 
# File permuteabcd.py

# The first letter varies from A to D
for first in 'ABCD':
    for second in 'ABCD':    # The second varies from A to D
        if second != first:     # No duplicate letters allowed
            for third in 'ABCD':     # The third letter varies from A to D
                # Don't duplicate first or second letter
                if third != first and third != second:
                    for fourth in 'ABCD': # The fourth letter varies from A to D
                        if fourth != first and fourth != second and fourth != third:
                            print(first + second + third + fourth)