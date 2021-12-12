#!/usr/bin/env python3

# Example 20-22
# A Python program to be run by various C programs.
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
C code runs Python code in this module in embedded mode. 
Such a file can be changed without changing the C layer.
This is just standard Python code (C handles conversions).
must be on the Python module search path if imported by C.
C can also run code in standard library modules like string.
################################################################################
"""

message = 'The meaning of life...'

def transform(input):
    input = input.replace('life', 'Python')
    return input.upper()