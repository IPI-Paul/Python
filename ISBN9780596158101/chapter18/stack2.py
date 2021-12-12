#!/usr/bin/env python3

# Example 18-2
# Defines a full-featured stack class which defines a new datatype with a variety 
# of behaviours
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-04-14

"a multi-instance stack class"

class error(Exception): pass                    # when imported: local exception

class Stack:
    def __init__(self, start=[]):               # self is the instance object
        self.stack = []                         # start is any sequence: stack...
        for x in start: self.push(x)
        self.reverse()                          # undo push's order reversal
    
    def push(self, obj):                        # methods: like module + self
        self. stack = [obj] + self.stack        # top is front of list
    
    def pop(self):
        if not self.stack: raise error('underflow')
        top, *self.stack = self.stack
        return top
    
    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[0]
    
    def empty(self):
        return not self.stack                   # instance.empty()
    
    # overloads
    def __repr__(self):
        return '[Stack: %s]' % self.stack       # print, repr(),...
    
    def __eq__(self, other):
        return self.stack == other.stack        # '==', '!='?
    
    def __len__(self):
        return len(self.stack)                  # len(instance), not instance
    
    def __add__(self, other):
        return Stack(self.stack + other.stack)  # instance1 + instance2
    
    def __mul__(self, reps):
        return Stack(self.stack * reps)         # instance * reps
    
    def __getitem__(self, offset):              # see also __iter__
        return self.stack[offset]               # instance[i], [i:j], in, for
    
    def __getattr__(self, name):
        return getattr(self.stack, name)        # instance.sort()/reverse()/...
    
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