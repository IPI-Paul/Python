#!/usr/bin/env python3

# Example 7-13
# Illustrates using a lambda function to pass in extra data to a handler function
# by deferring the call to the real handler function and specifying extra data needs
# Author: Mark Lutz
# Last modified: 

import sys
from tkinter import *                           # lambda generates a function

widget = Button(None,                           # but contains just an expression
                text='Hello event world', 
                command=(lambda: print('Hello lambda world') or sys.exit()))
widget.pack()
widget.mainloop()