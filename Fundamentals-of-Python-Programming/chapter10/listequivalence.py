# Listing 10.15
# Demonstrates the difference between two operators
# Author: Rick Halterman
# Last modified: 

# a and b are distinct lists that contain the same elements
a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
print('Is ', a, ' equal to ', b, '?', sep='', end=' ')
print(a == b)

print('Are ', a, ' and ', b, ' aliases?', sep='', end=' ')
print(a is b)

# c and d alias are distinct lists that contain the same elements
c = [100, 200, 300, 400]
d = c       # makes d an alias od c
print('Is ', c, ' eqaul to ', d, '?', sep='', end=' ')
print(c == d)

print('Are ', c, ' and ', d, ' aliases?', sep='', end=' ')
print(c is d)