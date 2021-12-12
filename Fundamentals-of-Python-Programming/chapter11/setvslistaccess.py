# Listing 11.16
# Creates both a set and a list, each containing the first 1,000 perfect squares.
# It then searches both data structures for, and does nothing with, all the 
# integers from 0 to 999,999. It reports the time required for the efforts.
# Author: Rick Halterman
# Last modified: 

# Data Structure size
size = 1000

# Make a big set 
S = {x ** 2 for x in range(size)}
# Make a big list
L = [x ** 2 for x in range(size)]

# Verify the type of S and L
print('Set:', type(S), ' List:', type(L))

from time import clock

# Search size
search_size = 1000000

# Time list access
start_time = clock()
for i in range(search_size):
    if i in L:
        pass
stop_time = clock()
print('List elapsed:', stop_time - start_time)

# Time set access
start_time = clock()
for i in range(search_size):
    if i in S:
        pass
stop_time = clock()
print('Set elapsed:', stop_time - start_time)