#!/usr/bin/env python3

# Example 18-10
# Implements a set object that can hold any type of object
# Author: Mark Lutz
# Last modified: 

"multi-instance, customizable, encapsulated set class"

class Set:
    def __init__(self, value=[]):       # on obje t creation
        self.data = []                  # manages a local list
        self.concat(value)
    
    def intersect(self, other):         # other is any sequence type
        res = []                        # self is the instance subject
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)                 # return a new Set
    
    def union(self, other):
        res = self.data[:]              # make a copy of my list
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)
    
    def concat(self, value):            # value: a list, string, Set...
        for x in value:                 # filters out duplicates
            if not x in self.data:
                self.data.append(x)
    
    def __len__(self):          return len(self.data)
    def __getitem__(self, key): return self.data[key]
    def __and__(self, other):   return self.intersect(other)
    def __or__(self, other):    return self.union(other)
    def __repr__(self):         return '<Set: ' + repr(self.data) + '>'