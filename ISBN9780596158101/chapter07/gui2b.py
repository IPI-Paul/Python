#!/usr/bin/env python3

# Example 7-11
# Demonstrates other ways to code buttons. this version packs the button in place
# without assigning it to a name, attaches it to the LEFT side of its parent window
# explicitly, and specifies root.quit as the callback handler
# Author: Mark Lutz
# Last modified: 

from tkinter import *
root = Tk()
Button(root, text='press', command=root.quit).pack(side=LEFT)
root.mainloop()