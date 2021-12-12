#!/usr/bin/env python3

# Example 7-21
# Creates an instance of a class with a real parent widget passed in. Illustrates
# how subclasses of Frame and can be further extended and customized by  
# subclassing and being attached to enclosing widgets.
# Author: Mark Lutz
# Last modified: 

from sys import exit
from tkinter import *                       # get Tk widget classes
from gui6 import Hello                      # get the subframe class

parent = Frame(None)                        # make a container widget
parent.pack()
Hello(parent).pack(side=RIGHT)              # attach Hello instead of running it

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()