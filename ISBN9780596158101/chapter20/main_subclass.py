#!/usr/bin/env python3

# Example 20-21
# Extends the C++ class, adding an extra print call statement to the C++ add 
# method and defining a brand-new mul method. Because the shadow class is pure 
# Python, this works normally
# Author: Mark Lutz
# Last modified: 

"subclass C++ class in Python (generated shadow class)"

from number import Number                       # import shadow class

class MyNumber(Number):
    def add(self, other):                       # extend method
        print('in Python add...')
        Number.add(self, other)
    
    def mul(self, other):                       # add new method
        print('in Python mul..')
        self.data = self.data * other

num = MyNumber(1)                       # same tests as ch20_main.cxx, main.pyu
num.add(4)                              # using Python subclass of shadow class
num.display()                           # add() is specialized in Python
num.sub(2)
num.display()
print(num.square())

num.data = 99
print(num.data)
num.display()

num.mul(2)                              # mul() is implemented in Python
num.display()
print(num)                              # repr from shadow superclass
del num