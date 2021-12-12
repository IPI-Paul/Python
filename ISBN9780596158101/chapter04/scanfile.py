#!/usr/bin/env python3

# Example 4-1
# Defines a general file-scanning routine, which simply applies a passed-in Python
# function to each line in an external file
# Author: Mark Lutz
# Last modified: 

def scanner(name, function):    
    file = open(name, 'r')                      # create a file object
    while True:
        line = file.readline()                  # call file methods
        if not line: break                      # until end-of-file
        function(line)                          # call a function obkject
    file.close()