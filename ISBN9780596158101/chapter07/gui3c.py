#!/usr/bin/env python3

# Example 7-14
# Shows Examples 7-12 and 7-13 rewritten to register a bound class method rather 
# than a function or a lambda result
# Author: Mark Lutz
# Last modified: 

import sys
from tkinter import *

class HelloClass:
    
    def __init__(self):
        widget = Button(None, text='Hello event world', command=self.quit)
        widget.pack()
    
    def quit(self):
        print('Hello class method world')       # self.quit is a bound method
        sys.exit()                              # retains the self+quit pair

HelloClass()
mainloop()