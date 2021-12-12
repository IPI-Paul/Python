#!/usr/bin/env python3

# Example 8-1
# Introduces some of the configuration options available in tkinter
# Author: Mark Lutz
# Last modified: 

from tkinter import *

root = Tk()
labelfont = ('times', 20, 'bold')                   # family, size, style
widget = Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')              # yellow text on black label
widget.config(font=labelfont)                       # use a larger font
widget.config(height=3, width=20)                   # intialize size: lines, chars
widget.pack(expand=YES, fill=BOTH)
root.mainloop()