# Listing 5.31
# Demonstrates that accidental infinite loops are not easy to diagnose and repair
# This program attempt to print all integers with their associated factors from 
# 1 to 20
# Author: Rick Halterman
# Last modified: 

# List the factors of the integers 1...MAX
MAX = 20                            # MAX is 20
n = 1                               # Start with 1
while n <= MAX:                     # Do not go past MAX
    factor = 1                      # 1 is a factor of any intger
    print(end = str(n) + ": ")      # Which integer are we examining?
    while factor <= n:              # Factors are <= the number
        if n% factor == 0:          # Test to see if factor is a factor of n
            print(factor, end=' ')  # If so, display it
            factor += 1             # Try the next number
    print()     # Move to the next line for next n
    n += 1