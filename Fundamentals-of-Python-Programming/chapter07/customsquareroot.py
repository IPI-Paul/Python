# Listing 7.24
# Contains the definition of a custom square_root function
# Author: Rick Halterman
# Last modified: 

# File customsquareroot.py

def square_root(val):
    """ Copute an approximation of the square root of x """
    # Compute a provisional sqquare root
    root = 0.1
    
    # How far off is our provisional root?
    diff = root * root - val
    
    # Loop until the provisional root is close enough to the actual root
    while diff > 0.00000001 or diff < -0.00000001:
        root = (root + val / root) / 2  # Compute new provisional root
        diff = root * root - val        # How bad is our current approximation
    return root

# Use the standard square root function to compare with our custom function
from math import sqrt

d = 1.0
while d <= 10.0:
    print('{0:6.1f}: {1:16.8f} {2:16.8f}'.format(d, square_root(d), sqrt(d)))
    d += 0.5    # Net d