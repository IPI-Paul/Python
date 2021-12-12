#!/usr/bin/env python3

# Example 20-19
# Repeats the ch20_main.cxx file's class tests. The C++ class is being utiolized 
# from the Python programming language
# Author: Mark Lutz
# Last modified: 

"""
use C++ class in Python code (c++ module + py shadow class)
this script runs the same tests as the ch20_main.cxx C++ file
"""

from number import Number       # imports .py C++ shadow class module

num = Number(1)                 # make a C++ class object in Python
num.add(4)                      # call its methods from Python
num.display()                   # num saves the C++ 'this' pointer
num.sub(2)
num.display()

res = num.square()              # converted C++ int return value
print('square: ', res)

num.data = 99                   # set C++ data member, generated __setattr__
val = num.data                  # get C++ data member, generated __getattr__
print('data: ', val)            # returns a normal Python integer object
print('data+1: ', val + 1)

num.display()
print(num)                      # runs repr in shadow/proxy class
del num                         # runs C++ destructor automatically