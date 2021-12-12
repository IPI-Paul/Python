# Listing 10.28
# Uses a list comprehension to create a list of factor pairs for a positive 
# integer supplied by the user.
# Author: Rick Halterman
# Last modified: 

n = int(input('Please enter a positive integer: '))
factors = [x for x in range(1, n + 1) if n % x == 0]
print('Factors of', n, ':', factors)