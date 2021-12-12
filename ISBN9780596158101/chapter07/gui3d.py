#!/usr/bin/env python3

# Example 7-15
# Shows a class that provides the required function-like interface for Python 
# class instance objects that can be called if they inherit a __call__ method
# Author: Mark Lutz
# Last modified: 

import sys
from tkinter import *

class HelloCallable:
    
    def __init__(self):                     # __ini__ run on object creation
        self.msg = 'Hello __call__ world'
    
    def __call__(self):
        print(self.msg)                     # __call__ run later when called
        sys.exit()                          # class object looks like a function

widget = Button(None, text='Hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()