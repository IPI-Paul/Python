#!/usr/bin/env python3

# Example 7-4
# Demonstrates that it is usually easier to use * to import everything from a 
# module by name in one shot
# Author: Mark Lutz
# Last modified: 

from tkinter import *
root = Tk()
Label(root, text='Hello GUI world!').pack(side=TOP)
root.mainloop()