#!/usr/bin/env python3

# Example 18-5
# Shows one way to implement a stack with in-place changes
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-4-14

"optimize with in-place list operations"

class error(Exception): pass                    # when imported: local exception

class Stack:
    def __init__(self, start=[]):               # self is the instance object
        self.stack = []                         # start is any sequence: stack...
        for x in start: self.push(x)
    
    def push(self, obj):                        # methods: like module + self
        self.stack.append(obj)                  # top is end of list
    
    def pop(self):
        if not self.stack: raise error('underflow')
        return self.stack.pop()                 # like fetch and delete stack[-1]
    
    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[-1]
    
    def empty(self):
        return not self.stack                   # instance.empty()
    
    def __len__(self):
        return len(self.stack)                  # len(instance), not instance
    
    def __getitem__(self, offset):
        return self.stack[offset]               # instance[offset], in, for
    
    def __repr__(self):
        return '[Stack: %s]' % self.stack
    
    # overloads
    def __eq__(self, other):
        return self.stack == other.stack        # '==', '!='?
    
    def __add__(self, other):
        return Stack(self.stack + other.stack)  # instance1 + instance2
    
    def __mul__(self, reps):
        return Stack(self.stack * reps)         # instance * reps

    def __sub__(self, other):
        try:
            len(other.stack)
        except:
            val = other
            other = Stack()
            try:
                for itm in val: other.push(itm)
                other.stack.reverse()
            except:
                other.push(val)
        for i in range(len(other.stack), len(self.stack) + 1):
            if self.stack[-i:len(self.stack)-(i-len(other.stack))] == other.stack:
                return self.stack[:-i] + self.stack[len(self.stack)-(i-len(other.stack)):]    