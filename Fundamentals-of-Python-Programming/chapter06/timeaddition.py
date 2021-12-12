# Listing 6.6
# Measures how long it takes a for a Python program to add up all integers from 
# 1 to 100,000,000
# Author: Rick Halterman
# Last modified: 

from time import clock

sum = 0             # Initialize sum accumulator
start = clock()     # Start the stopwatch
for n in range(1, 100000001):   # Sum the numbers
    sum += n
elapsed = clock() - start   # Stop the stopwatch
print('Sum:', sum, 'time:', elapsed)    # Report results