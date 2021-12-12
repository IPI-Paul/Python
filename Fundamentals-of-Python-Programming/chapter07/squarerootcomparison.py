# Listing 7.25
# Tests a custom square root function over a range of 10,000,000 floating-point
# values
# Author: Rick Halterman
# Last modified: 

from math import fabs, sqrt

def equals(a, b, tolerance):
    """
    Consider two floating-point numbers equal when the difference between them 
    is very small.
    Retruns true if a = b or |a - b| < tolerance.
    If a and b diffe by only a small amount (specified by tolerance), a and b 
    are considered "equal". Useful to account for floating-point round-off error.
    The == operator is checked first since some special floating-point values 
    such as floating-point infinity require an exact check.
    """
    return a == b or fabs(a - b) < tolerance

def square_root(val):
    """
    Computes the approximate square root of val.
    val is a number
    """
    # Compute a provisional square root?
    root = 1.0
    
    # How far off is our provisional root?
    diff = root * root - val
    
    # Loop until the provisional root is close enough to the actual root
    while diff > 0.00000001 or diff < -0.00000001:
        root = (root + val / root) / 2  # Compute new provisional root
        diff = root * root - val        # How bad is our current approximation
    return root

def main():
    d = 0.0
    err = 0
    while d < 10000.0:
        if not equals(square_root(d), sqrt(d), 0.001):
            print('*** Diffenrence detected for', d)
            print(' Expected', sqrt(d))
            print(' Computed', square_root(d))
            err += 1
        d += 0.0001 # Consider next value
    if err == 0:
        print('Both functions produced the same results')
        
main()  # Run program