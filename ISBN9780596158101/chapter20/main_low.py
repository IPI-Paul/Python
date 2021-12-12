#!/usr/bin/env python3

# Example 20-20
# Runs the C++ extension module diirectly without the shadow class, to demonstrate
# how the shadow class maps calls back to C++
# Author: Mark Lutz
# Last modified: 

"""
run similar tests to ch20_main.cxx and main.py
but use low-level C accessor function interface
"""

import sys 
sys.path.append('../sourceFiles/libraries')
from _number import *                   # c++ extension module wrapper

num = new_Number(1)
Number_add(num, 4)                      # pass C++ 'this' pointer explicitly
Number_display(num)                     # use accesssor functions in the C module
Number_sub(num, 2)
Number_display(num)
print(Number_square(num))

Number_data_set(num, 99)
print(Number_data_get(num))
Number_display(num)
print(num)
delete_Number(num)