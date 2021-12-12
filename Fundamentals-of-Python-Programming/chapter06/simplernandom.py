# Listing 6.10
# Prints 100 pseudorandom integers in the range 1...100
# Author: Rick Halterman
# Last modified: 

from random import randrange, seed

seed(23)                                # Set random number seed
for i in range(0, 100):                 # Print 100 random numbers
    print(randrange(1, 1001), end=' ')  # Range 1...1,000, inclusive
print()                                 # Print new line