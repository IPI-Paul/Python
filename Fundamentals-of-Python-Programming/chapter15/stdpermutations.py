# Listing 15.16
# Demonstrates the Python standard library generator-like object named 
# permutations in the itertools module
# Author: Rick Halterman
# Last modified: 

# Use the standard permutations function to list the possible arrangements of 
# elements in a list

from itertools import permutations

def main():
    a = [0, 1, 2]
    for p in permutations(a):
        print(p, end=' ')
    print()

main()