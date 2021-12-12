# Listing 10.13
# Demonstrates that lists are no immutable and can be reassigned
# Author: Rick Halterman
# Last modified: 

a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
print('a =', a)
print('b =', b)
b[2] = 35
print('a =', a)
print('b =', b)