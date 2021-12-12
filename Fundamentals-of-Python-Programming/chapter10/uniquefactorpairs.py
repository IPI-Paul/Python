# Listing 10.30
# Adds the finishing touch to avoid redundant pairs by returning all xs in the 
# range 1...sqrt(n) incliusive.
# Author: Rick Halterman
# Last modified: 

import math 
n = int(input('Please enter a positive integer: '))
factors = [(x, n // x) for x in range(1, round(math.sqrt(n)) + 1) if n % x == 0]
print('Factor pairs of', n, ':', factors)