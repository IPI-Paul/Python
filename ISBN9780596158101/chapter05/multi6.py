#!/usr/bin/env python3

# Example 5-34
# Demonstrates multiprocessing support for pools- spawned shildren that work in 
# concert on a given task
# Author: Mark Lutz
# Last modified: 

import os
from multiprocessing import Pool

def powers(x):
    # print(os.getpid())                        # enable to watch children
    return 2 ** x

if __name__ == '__main__':
    workers = Pool(processes=5)
    
    results = workers.map(powers, [2] * 100)
    print(results[:16])
    print(results[-2:])
    
    results = workers.map(powers, range(100))
    print(results[:16])
    print(results[-2:])