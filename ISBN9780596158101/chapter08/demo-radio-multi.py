#!/usr/bin/env python3

# Example 8-26
# Uses numbers 0to 9 to name its options and the remainder of division by 3 to 
# select options in its group
# Author: Mark Lutz
# Last modified: 

# see what happens when some buttons have same value

from tkinter import *
root = Tk()
var = StringVar()
for i in range(10):
    rad = Radiobutton(root, text=str(i), variable=var, value=str(i % 3))
    rad.pack(side=LEFT)
var.set(' ')                                        # deselect all initially
root.mainloop()