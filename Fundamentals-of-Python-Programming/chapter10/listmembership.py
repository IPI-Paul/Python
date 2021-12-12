# Listing 10.12
# Demonstrates Python's in operator
# Author: Rick Halterman
# Last modified: 

lst = list(range(0, 21, 2))
for i in range(-2, 23):
    if i in lst:
        print(i, 'is a member of', lst)
    if i not in lst:
        print(i, 'is a NOT member of', lst)