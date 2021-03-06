#!/usr/bin/env python3

# Example 7-20
# Illustrates the concept of reusable GUI components with classes built up as 
# subclasses of imported objects
# Author: Mark Lutz
# Last modified: 

from tkinter import *

class Hello(Frame):                             # an extended Frame
    
    def __init__(self, parent=None):
        Frame.__init__(self, parent)            # do superclass init
        self.pack()
        self.data = 42
        self.make_widgets()                     # attach widgets to self
    
    def make_widgets(self):
        widget = Button(self, text='Hello frame world!', command=self.message)
        widget.pack(side=LEFT)
    
    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)

if __name__ == '__main__': Hello().mainloop()