# Listing 15.17
# Uses the list constructor function to perform the conversion of the tuples 
# produced by the itertools permutations function to lists
# Author: Rick Halterman
# Last modified: 

# Use the standard permutations function to list the possible arrangements of 
# elements in a list

from itertools import permutations

def main():
    a = [0, 1, 2]
    for p in permutations(a):
        print(list(p), end=' ')
    print()

main()