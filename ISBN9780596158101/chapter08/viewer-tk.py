#!/usr/bin/env python3

# Example 8-42
# Uses tkinter to display a single image by attaching it to a label in the main
# application window
# Author: Mark Lutz
# Last modified: 

"""
show one image with standard tkinter photo object;
as is this handles GIF/PNG files, but not JPEG images; image filename listed in 
command line, or default; use a Canvas instead of label for scrolling, etc
"""

import os, sys
from tkinter import *                       # use standard tkinter photo object

imgdir = '../sourceFiles/images/'           # Gif/PNG works, but JPEG requires PIL
imgfile= 'queen-of-hearts.png'
if len(sys.argv) > 1:                       # cmdline argument given?
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)           # display photo on a label
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())     # show size in pixels before destroyed
win.mainloop()