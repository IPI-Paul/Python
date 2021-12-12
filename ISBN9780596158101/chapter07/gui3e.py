#!/usr/bin/env python3

# Example 7-16
# Rewrites the prior section's GUI again to use bid, not the command keyword, to 
# catch button presses
# Author: Mark Lutz
# Last modified: 

import sys
from tkinter import *

def hello(event):
    print('Press twice to exit')                # on single-left click

def quit(event):                                # on double-left click
    print('Hello, I must be going...')          # event gives widget, x/y, etc
    sys.exit()

widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)                # bind left mouse clicks
widget.bind('<Double-1>', quit)                 # bind double-left clicks
widget.mainloop()