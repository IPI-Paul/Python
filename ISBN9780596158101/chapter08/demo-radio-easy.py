#!/usr/bin/env python3

# Example 8-28
# Associates the buttons with an IntVar, the integer type sibling of StringVar,
# and initialises it to zero
# Author: Mark Lutz
# Last modified: 

# radio buttons, the easy way

from tkinter import *

root = Tk()                                             # IntVars work too
var = IntVar(0)                                         # select 0 to start
for i in range(10):
    rad = Radiobutton(root, text=str(i), value=i, variable=var)
    rad.pack(side=LEFT)
root.mainloop()
print(var.get())                                        # show state on exit