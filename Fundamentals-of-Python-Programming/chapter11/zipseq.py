# Listing 11.2
# Constructs a sequence of tuples with their first elements derived from a list 
# and their second elements obtained from a generator.
# Author: Rick Halterman
# Last modified: 

def gen(n):
    """
    Generates the first n perfect squares, starting with zero:
    0, 1, 4, 9, 16,..., (n - 1)^2.
    """
    for i in range(n):
        yield i ** 2

for p in zip([10, 20, 30, 40, 50, 60], gen(4)):
    print(p, end=' ')
print()