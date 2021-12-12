#!/usr/bin/env python3

# Example 7-12
# Defines a callback handler for a Button
# Author: Mark Lutz
# Last modified: 

import sys
from tkinter import *

def quit():                             # a custom callback handler
    print('Hello , I must be going...') # kill windows and process
    sys.exit()

widget = Button(None, text='Hello event world', command=quit)
widget.pack()
widget.mainloop()