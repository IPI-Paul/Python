#!/usr/bin/env python3

# Example 8-11
# Provides a button that pops up color selectors that let users choose color 
# preferences on the fly. Simply pass the color string to widget config methods 
# in callback handlers
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from tkinter.colorchooser import askcolor

def setBgColor():
    (triple, hexstr) = askcolor()
    if hexstr:
        print(hexstr)
        push.config(bg=hexstr)

root = Tk()
push = Button(root, text='Set Background Colour', command=setBgColor)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.mainloop()