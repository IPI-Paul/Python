# Listing 11.6
# Demonstrates the power of the * unpacking operator for flexible list printing
# Author: Rick Halterman
# Last modified: 

lst = [ 2 * i for i in range(6)]

# Typical list printing
print(lst)

# Print just the list elements
print(*lst)

# Print the list in a special way
print(*lst, sep=' and ', end="--that's all folks!\n")