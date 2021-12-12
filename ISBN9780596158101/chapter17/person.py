#!/usr/bin/env python3

# Example 17-2
# A class, which is used to model people in a hypothetical work scenario
# Author: Mark Lutz
# Last modified: 

'a person object: fields + behaviour'

class Person:
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job = job
        self.pay = pay                      # real instance data
    
    def tax(self):
        return self.pay * 0.25              # computed on call
    
    def info(self):
        return self.name, self.job, self.pay, self.tax()