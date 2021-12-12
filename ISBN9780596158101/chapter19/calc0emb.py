#!/usr/bin/env python3

# Example 19-19
# Attaches the simple calculator's widget package, along with extras, to a 
# common parent
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from calc0 import CalcGui                           # add parent,no master calls

class Outer:
    def __init__(self, parent):                         # embed GUI
        Label(parent, text='Calc Attachment').pack()    # side=top
        CalcGui(parent)                                 # add calc frame
        Button(parent, text='Quit', command=parent.quit).pack()

root = Tk()
Outer(root)
root.mainloop()