# Listing 6.7
# Measures how long it takes a for a Python program to caount all prime numbers 
# up to 10,000 using the same algorithm as Listing 5.37
# Author: Rick Halterman
# Last modified: 

from time import clock

max_value = 10000
count = 0
start_time = clock()        # Start timer
# Try values from 2 (smallest prime number) to max_value
for value in range(2, max_value + 1):
    # See if value is prime
    is_prime = True     # Provisionally, value is prime
    # Try all possible factors from 2 to value - 1
    for trail_factor in range(2, value):
        if value % trail_factor == 0:
            is_prime = False    # Found a factor
            break               # No need to continue; it is not prime
    if is_prime:
        count += 1              # Count the prime number
print()     # Move cursor down to next line
elapsed = clock() - start_time  # Stop the timer
print('Count:', count, ' Elapsed time:', elapsed, 'sec')