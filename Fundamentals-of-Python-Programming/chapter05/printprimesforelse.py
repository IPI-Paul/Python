# Listing 5.38
# Uses a for/else loop to display all prime numbers up to a value entered by the 
# user
# Author: Rick Halterman
# Last modified: 

max_value = int(input('Display primes up to what value? '))
# Try values from 2 (smallest prime number) to max_value
for value in range(2, max_value + 1):
    # See if value is prime: try all possible factors from 2 to value -1
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            break                   # No need to continue; it is not prime
    else:
        print(value, end = ' ')     # Display the prime number
print()                             # Move to the next line