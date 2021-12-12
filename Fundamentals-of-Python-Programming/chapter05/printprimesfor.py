# Listing 5.37
# Uses a for loop to display all prime numbers up to a value entered by the 
# user
# Author: Rick Halterman
# Last modified: 

max_value = int(input('Display primes up to what value? '))
# Try values from 2 (smallest prime number) to max_value
for value in range(2, max_value + 1):
    # See if value is prime
    is_prime = True # Provisionally, value is prime
    # Try all possible factors from 2 to value -1
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False        # Found a factor
            break                   # No need to continue; it is not prime
    if is_prime:
        print(value, end = ' ')     # Display the prime number
print()                             # Move to the next line