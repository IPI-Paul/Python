#!/usr/bin/env python3

# Example 8-24
# Illustrates that linked tkinter variables make the task of managing state 
# values easier, especially if you don't need to process check button states 
# until some time in the future
# Author: Mark Lutz
# Last modified: 

# check buttons, the easy way

from tkinter import *

root = Tk()
states = []
for i in range(10):
    var = IntVar()
    chk = Checkbutton(root, text=str(i), variable=var)
    chk.pack(side=LEFT)
    states.append(var)
root.mainloop()                         # let tkinter keep track
print([var.get() for var in states])    # show all states on exit (or map/lambda)