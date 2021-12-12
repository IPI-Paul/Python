#!/usr/bin/env python3

# Example 7-7
# Demonstrates that there are two additional ways to specify Label widget 
# configuration options. The Text option of the label is set after it is constructed,
# by assigning to the widget's text key. Widget objects overload (intercept) index
# operations such that options are also available as mapping keys, much like a
# dictionary
# Author: Mark Lutz
# Last modified: 

from tkinter import *
widget = Label()
widget['text'] = 'Hello GUI world!'
widget.pack(side=TOP)
mainloop()