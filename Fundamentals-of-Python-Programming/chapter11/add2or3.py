# Listing 11.3
# Illustrates the ability to have a function with a variable number of parameters
# Author: Rick Halterman
# Last modified: 

def sum(a, b, c = 0):
    return a + b + c        # Adding zero will not affect a + b

print(sum(3, 4))
print(sum(3, 4, 5))