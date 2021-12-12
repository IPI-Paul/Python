#!/usr/bin/env python3

# Example 18-6
# The built-in time module provides a clock function that we can use to get the 
# current CPU time in floating-point seconds, and the function timer.test simply
# calls a function reps times and returns the number of elapsed seconds by 
# subtracting stop from start times
# Author: Mark Lutz
# Last modified: 

"generic code timer tool"

def test(reps, func, *args):            # or best of N? see Learning Pythpn
    import time
    start = time.clock()                # current CPU time in float seconds
    for i in range(reps):               # call function reps times
        func(*args)                     # discard any return value
    return time.clock() - start         # stop time - start time