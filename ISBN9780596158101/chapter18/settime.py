#!/usr/bin/env python3

# Example 18-12
# Codes a script to compare set class performance. It reuses the timer module of 
# Example 18-6 used to compare stacks 
# Author: Mark Lutz
# Last modified: 

"compare set alternatives performance"
import timer, sys
import set, fastset

def setops(Class):                              # 3.x: range okay
    a = Class(range(50))                        # a 50-interger set
    b = Class(range(20))                        # a 20-interger set
    c = Class(range(10))
    d = Class(range(5))
    for i in range(5):
        t = a & b & c & d                       # 3 intersections
        t = a | b | c | d                       # 3 unions

if __name__ == '__main__':
    rept = int(sys.argv[1])
    print('set     => ', timer.test(rept, setops, set.Set))
    print('fastset => ', timer.test(rept, setops, fastset.Set))