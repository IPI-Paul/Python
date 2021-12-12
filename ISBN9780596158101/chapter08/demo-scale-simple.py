#!/usr/bin/env python3

# Example 8-31
# Illustrates that tkinter variables aren't needed to program scales. Simply 
# register movement callbakcs or call the scale get method to fetch scale values
# on demand
# Author: Mark Lutz
# Last modified: 

from tkinter import *
root=Tk()
scl = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=YES, fill=Y)

def report():
    print(scl.get())

Button(root, text='State', command=report).pack(side=RIGHT)
root.mainloop()