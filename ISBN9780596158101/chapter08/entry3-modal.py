#!/usr/bin/env python3

# Example 8-21
# Utilises StringVars that were tied to Entry widgets to fetch input even after 
# their modal dialog has been dismissed
# Author: Mark Lutz
# Last modified: 

# can fetch values after destroy with stringvars

from tkinter import *
from entry3 import makeform, fetch, fields

def show(variables, popup):
    popup.destroy()                 # order doesn't matter here
    fetch(variables)                # variables live on after window destroyed

def ask():
    popup = Toplevel()             # show form in modal dialog window
    vars = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(vars, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()             # wait for destroy here

root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()