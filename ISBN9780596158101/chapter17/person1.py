#!/usr/bin/env python3

# Example 17-3
# The Person class from previous section changed 
# Author: Mark Lutz
# Last modified: 

"""
a person object: fileds + behaviour
change: tax method is now a computed attribute
"""

class Person:
    
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job = job
        self.pay = pay                          # real instance data
    
    def __getattr__(self, attr):                # on person.attr
        if attr == 'tax':
            return self.pay * 0.30              # computed on access
        else:
            raise AttributeError()              # other unknown names
    
    def info(self):
        return self.name, self.job, self.pay, self.tax