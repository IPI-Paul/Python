#!/usr/bin/env python3

# Example 8-39
# Makes the canvas smaller or larger than its default size as needed, lets you 
# pass in a photo file's name on the command line, and can be used as a simple 
# image viewer utility
# Author: Mark Lutz
# Last modified: 

gifdir = '../sourceFiles/images/'
from sys import argv
from tkinter import *
filename = argv[1] if len(argv) > 1 else 'queen-of-hearts.png' # name on cmdline?

win = Tk()
img = PhotoImage(file=gifdir + filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())          # size to img size
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()