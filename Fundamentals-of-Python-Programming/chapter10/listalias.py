# Listing 10.14
# Looks like it may behave exactly like Listing 10.13.
# Author: Rick Halterman
# Last modified: 

a = [10, 20, 30, 40]
b = a
print('a =', a)
print('b =', b)
b[2] = 35
print('a =', a)
print('b =', b)