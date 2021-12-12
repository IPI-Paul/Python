# Listing 7.5
# Provides a function that Counts to the number given bypassing in a variable
# Author: Rick Halterman
# Last modified: 

def count_to_n(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()

for i in range(1, 10):
    count_to_n(i)