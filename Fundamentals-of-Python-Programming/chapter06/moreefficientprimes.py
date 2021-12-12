# Listing 6.4
# Uses the math library sqrt function to reduce the number of potential factors
# a program needs to consider when checking for prime numbers
# original code
# Author: Rick Halterman
# Last modified: 

from math import sqrt

max_value = int(input('Display primes up to what value? '))
value = 2 # Samllest prime
while value <= max_value:
    # See if value is prime
    is_prime = True # Provisionally, value is prime
    # Try all possible factors from 2 to value - 1
    trial_factor = 2
    root = sqrt(value)  # Compute the square root of the value
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False        # Found a factor
            break                   # No need to continue; it is not prime
        trial_factor += 1           # Try the next potential factor
    if is_prime:
        print(value, end = ' ')     # Display the prime number
    value += 1                      # Try next portential prime number
    
print()         # Move cursor down to next line
        