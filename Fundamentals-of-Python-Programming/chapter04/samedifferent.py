# Listing 4.6
# Demonstrates the perils of using the equality operator with floating-point 
# numbers
# Author: Rick Halterman
# Last modified: 

d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1 =',d1, ' d2 =', d2)
if d1 == d2:
    print('Same')
else:
    print('Different')