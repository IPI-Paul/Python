#!/usr/bin/env python3

# Example 20-33
# Defines a simple Python class in a module that can be utilized from C
# Author: Mark Lutz
# Last modified: 

# call this class from C to make objects

class klass:
    def method(self, x, y):
        return "brave %s %s" % (x, y)           # run me from C