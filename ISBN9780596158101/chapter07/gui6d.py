#!/usr/bin/env python3

# Example 7-23
# Illustrates extending the Hello class instead of attaching it by overriding 
# some of its methods in a new subclass (which itself becomes a specialised Frame 
# widget)
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from gui6 import Hello

class HelloExtender(Hello):
    
    def make_widgets(self):                     # extend method here
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)
    
    def message(self):
        print('hello', self.data)               # redefine method here

if __name__ == '__main__': HelloExtender().mainloop()