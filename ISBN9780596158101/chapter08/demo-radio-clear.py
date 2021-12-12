#!/usr/bin/env python3

# Example 8-29
# Illustrates how a tkinter variable class may be reclaimed (garbage collected) 
# affection all radio buttons that rely on it
# Author: Mark Lutz
# Last modified: 

# hold on to your radio variables (an obscure thing, indeed)

from tkinter import *

root = Tk()

def radio1():                               # local vars are temporary
    #global tmp                             # making it global fixes the problem
    tmp = IntVar()
    for i in range(10):
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)                              # select 6th button

radio1()s
root.mainloop()
    