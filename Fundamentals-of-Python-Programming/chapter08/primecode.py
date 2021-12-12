# Listing 8.6
# Illustrates that a Python source file constitutes a module
# Author: Rick Halterman
# Last modified: 

""" Contains the definition of the is_prime function """
from math import sqrt

def is_prime(n):
    """ 
    Returns True if nonnegative integer n is prime; otherwise, returns False 
    """
    trial_factor = 2
    root = sqrt(n)
    
    while trial_factor <= root:
        if n % trial_factor == 0:  # Is trial factor a factor?
            return False            # Yes, return right away
        trial_factor += 1           # Consider next potential factor
        
    return True                     # Tried them all, must be prime