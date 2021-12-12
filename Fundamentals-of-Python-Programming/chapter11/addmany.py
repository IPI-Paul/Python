# Listing 11.4
# Illustrates to write a function that can accept an arbitary number of parameters
# Author: Rick Halterman
# Last modified: 

def sum(*nums):
    s = 0               # Intialise sum to zero
    for num in nums:    # Consider each argument passed to the function
        s += num        # Accumulate their values
    return s

print(sum(3, 4))
print(sum(3, 4, 5))
print(sum(3, 3, 3, 3, 4, 1, 9, 44, -2, 8, 8))