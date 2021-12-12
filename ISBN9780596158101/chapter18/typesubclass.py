#!/usr/bin/env python3

# Example 18-13
# Shows the main parts of a module containing variants of our stack and set 
# objects coded in the prior sections, revised as customized lists
# Author: Mark Lutz
# Last modified: 

"customize built0in types to extend, instead of starting from scratch"

class Stack(list):
    "a list with extra methods"
    def top(self):
        return self[-1]
    
    def push(self, item):
        list.append(self, item)
    
    def pop(self):
        if not self:
            return None                 # avoid exception
        else:
            return list.pop(self)

class Set(list):
    "a list with extra methods and operators"
    def __init__(self, value=[]):       # an object creation
        list.__init__(self)
        self.concat(value)
    
    def intersect(self, other):         # other is any sequence type
        res = []                        # self is the instance subject
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)                 # return a new Set
    
    def union(self, other):
        res = Set(self)                 # new set with a copy of my list
        res.concat(other)               # insert uniques from other
        return res
    
    def concat(self, value):            # value: a list, string, Set...
        for x in value:                 # filters out duplicates
            if not x in self:
                self.append(x)
    
    # len, getitem, iter inherited, use list repr
    def __and__(self, other):   return self.intersect(other)
    def __or__(self, other):    return self.union(other)
    def __str__(self):          return '<Set: ' + repr(self) + '>'

class FastSet(dict):
    pass        # this doesn;t simplify much