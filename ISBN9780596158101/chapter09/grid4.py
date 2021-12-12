#!/usr/bin/env python3

# Example 9-23
# Builds a five-row by four-column array of labels, where each label simply 
# displays its row and column number
# Author: Mark Lutz
# Last modified: 

# simple 2D table, in default Tk root window

from tkinter import *

for i in range(5):
    for j in range(4):
        lab = Label(text='%d.%d' % (i, j), relief=RIDGE)
        lab.grid(row=i, column=j, sticky=NSEW)

mainloop()