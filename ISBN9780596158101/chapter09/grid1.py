#!/usr/bin/env python3

# Example 9-18
# Lays out a table of Labels and Entry fields arrayed on a grid
# Author: Mark Lutz
# Last modified: 

from tkinter import *
colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

r = 0
for c in colors:
    Label(text=c, relief=RIDGE, width=25).grid(row=r, column=0)
    Entry(bg=c, relief=SUNKEN, width=50).grid(row=r, column=1)
    r += 1

mainloop()