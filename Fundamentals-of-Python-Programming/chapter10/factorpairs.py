# Listing 10.29
# Shows the resulting program which produces a list of factor pairs.
# Author: Rick Halterman
# Last modified: 

n = int(input('Please enter a postive integer: '))
factors = [(x, n // x) for x in range(1, n + 1) if n % x == 0]
print('Factor pairs of', n, ':', factors)