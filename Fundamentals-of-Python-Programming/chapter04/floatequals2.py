# Listing 4.8
# Checks floating-point numbers to see if the values are close enough to zero
# Author: Rick Halterman
# Last modified: 

d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1 =',d1, ' d2 =', d2)
if -0.0000001 < d1 - d2 < 0.0000001:    
    print('Same')
else:
    print('Different')